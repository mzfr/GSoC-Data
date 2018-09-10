"""Scraper for new summerofcode archive
Gets Get organizations and projects information of year 2016-2017
"""
import re
import asyncio
from os.path import join
from common import get_page, dumper


URL = 'https://summerofcode.withgoogle.com'


async def project_details(project_links: list):
    """Get all the information for specific project

    :project_links: List of all the Organization on one page
    """
    project = []
    for projects in project_links:
        link = join(URL, projects[1:-1])
        soup = await get_page(link)
        title = soup.find('h3', {'class': 'banner__title'}).text
        org_data = soup.find(
            'main', {'class': 'app-body'}).find('div', {'class': 'org__meta'})
        try:
            org = org_data.find_all('div')[1].find('div').text
            student_name = org_data.find_all('div')[3].find('div').text
            mentors = org_data.find_all('div')[5].find('ul').find_all('li')
            mentors = [mentor.text for mentor in mentors]
            project.append({"Organization": org, "title": title,
                            "student": student_name, "mentors": mentors,
                            "link": projects})
        except AttributeError:
            print(title)

    return project


async def orgs_information(orgs_list: list):
    """Get all the information about an organizations
    Also grabs links for the project under each org.

    :orgs_list: List of urls for each org
    """

    orgs_info = []
    project_links = []
    project_valid_url = '/?archive/\d+/projects/\d+[0-9]/'

    for org in orgs_list:
        topics = []
        techs = []

        url = join(URL, org[1:-1])
        soup = await get_page(url)

        name = soup.find('h2', {'class': 'md-display-1'}).text
        about = soup.find('div', {'class': 'org__long-description'}).text
        idea = soup.find('md-button', {'target': '_blank'}).get('href')
        # mailing_list = soup.find('md-button', {'class': })
        for topic in soup.find_all('li', {'class': 'organization__tag organization__tag--topic'}):
            topics.append(topic.text)

        for tech in soup.find_all('li', {'class': 'organization__tag organization__tag--technology'}):
            techs.append(tech.text)

        for i in soup.find_all('md-button'):
            info = i.get('href')
            if info:
                if info.endswith('IRC') or 'gitter' in info or 'slack' in info or 'irc' in info:
                    irc = info
                else:
                    print(url)
                    irc = ""
                if 'list' in info:
                    mailing_list = info
                elif info.startswith('mailto'):
                    contact = info

        # Get projects links of an orgs
        for links in soup.find_all('a'):
            if re.match(project_valid_url, links.get('href')):
                project_links.append(links.get('href'))

        orgs_info.append({'Organization': name, 'About': about, 'URL': url,
                          'Technologies': techs, 'Topics': topics, 'Mailing-list': mailing_list,
                          'IRC': irc, 'contact': contact, 'Idea-page': idea})

    return orgs_info, project_links


async def orgs_links():
    """Get links of all the organizations from 2016-2017"""

    orgs_list = []
    valid_urls = "/?[a-z]+/?\\d+[0-9]/[a-z]+/?\\d+[0-9]/"

    for year in range(2016, 2018):
        orgs_url = join(URL, "archive/{yr}/organizations/".format(yr=year))
        soup = await get_page(orgs_url)
        for link in soup.find_all('a'):
            if re.match(valid_urls, link.get('href')):
                orgs_list.append(link.get('href'))

    return orgs_list


def main():
    """Maintains all the other functions and generates JSON file"""
    loop = asyncio.get_event_loop()
    all_orgs = loop.run_until_complete(orgs_links())
    organizations, project_links = loop.run_until_complete(orgs_information(all_orgs))
    projects = project_details(project_links)

    dumper(organizations, 'orgs_2016-2017.json')
    dumper(projects, '2016-2017.json')


if __name__ == '__main__':
    main()
