"""Scraper for new summerofcode archive
Gets Get organizations and projects information of year 2016-2017
"""
from os.path import join
from common import getPage, dumper


URL = 'https://summerofcode.withgoogle.com'


def getList(soup):
    """Gets links for all the Organization
        :soup: bs4 object
    """
    links = []
    for link in soup.find('main', {'class': 'app-body lifted'}).find_all('a'):
        links.append(link.get('href'))
    print(links[-1])
    return links


def getDetails(pLinks: list):
    """Get all the information for specific porject
        :pLink: List of all the Organization on one page
    """
    project = []
    for pLink in pLinks:
        Link = URL + pLink
        soup = getPage(Link)
        title = soup.find('h3', {'class': 'banner__title'}).text
        orgData = soup.find(
            'main', {'class': 'app-body'}).find('div', {'class': 'org__meta'})
        try:
            org = orgData.find_all('div')[1].find('div').text
            studentName = orgData.find_all('div')[3].find('div').text
            mentors = orgData.find_all('div')[5].find('ul').find_all('li')
            mentors = [mentor.text for mentor in mentors]
            project.append({"Organization": org, "title": title,
                            "student": studentName, "mentors": mentors,
                            "link": pLink})
        except AttributeError:
            print(title)

    return project


def orgs_info():
    """Get name and links of org fro 2016-2018"""

    all_org = []
    for year in range(2016, 2018):
        orgs_url = join(URL, "archive/{yr}/organizations/".format(yr=year))
        soup = getPage(orgs_url)
        orgs = soup.findAll('li', attrs={'class': 'organization-card__container'})

        for org in orgs:
            name = org.find('h4').text
            link = org.find('a').get('href')
            about = org.find('div', {'class': "organization-card__tagline font-black-54"}).text
            all_org.append({'link': URL + link, 'name': name, 'about': about})

    return all_org


def main():
    projects = []
    for year in range(2016, 2018):
        for page in range(1, 12):
            url = URL + '/archive/{yr}/projects/?page={page}'.format(yr=year, page=page)
            soup = getPage(url)
            projectLinks = getList(soup)[1:-1]
            pDetails = getDetails(projectLinks)
            projects.extend(pDetails)
    dumper(projects, 'projects_2016-2017')
    dumper(orgs_info(), 'organizations_2016-2017.json')


if __name__ == '__main__':
    main()
