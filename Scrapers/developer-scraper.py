"""
Scraper for developer-google GSoC archive
Get organizations and projects information from 2005-2008
"""

from os.path import join, basename
from common import getPage, dumper

developer = "https://developers.google.com"


def get_info(soup):
    """Gets information about orgs and projects from year 2005-2008
    """
    organizations, proj = [], []

    org_sections = soup.find(
        'div', {'itemprop': 'articleBody'}).find_all('section')[1:]

    try:
        for orgs in org_sections:
            org_name = orgs.find('h2').text
            link = orgs.find('a').text
            projects = orgs.find('ul').find_all('li')
            for p in projects:
                project = p.find('h4')
                details = project.nextSibling.strip().split(',')
                student = details[0].replace('by ', '')
                mentor = details[1].replace(' mentored by ', '')
                proj.append({'project': project.text, 'student': student,
                              'mentor': mentor})
            organizations.append({'name': org_name, 'link': link})

    except AttributeError:
        print(link)

    return organizations, proj


def main():
    orgs_data = {}
    projects_data = {}
    for year in range(2005, 2009):
        url = developer + '/open-source/gsoc/{yr}/'.format(yr=year)
        soup = getPage(url)
        orgs, projects = get_info(soup)
        orgs_data[year] = orgs
        projects_data[year] = projects
    dumper(orgs_data, "orgs_2005-2008.json")
    dumper(projects_data, "projects_2005-2008.json")


if __name__ == '__main__':
    main()
