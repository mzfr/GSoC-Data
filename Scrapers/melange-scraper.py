"""
This is a scarper for google-melange GSoC archive
It only works for the year 2009-2015.
"""
import re
from os.path import join, basename
from common import getPage, dumper

melange = "https://www.google-melange.com"


def grab_project_links(soup):
    """Gets links of particular projects
    """
    project_urls = []
    valid_project_url = "/?archive/?gsoc/\d+[0-9]/orgs/[a-zA-Z]+/[a-zA-Z]+/[a-zA-Z]+.html"
    try:
        # Grab links to all the projects
        all_link = soup.find_all("a")
        for link in all_link:
            if re.match(valid_project_url, link.get("href")):
                project_urls.append(join(melange, link.get("href")[1:]))
    except TypeError:
        print(link)

    return project_urls


def org_info_above_14(orgs_urls14):
    """Scarpe information about orgs of year 2014 and 2015
        :orgs_urls14: list of urls of year 2014 and 2015
    """
    org_info_14 = []
    project_urls_from14 = []
    for url in orgs_urls14:
        try:
            soup = getPage(url)
            org_name = basename(url)
            org_info = soup.find_all('p')
            web_page = org_info[1].text.splitlines()[-1].strip()
            mailing_list = org_info[2].text.split(":")[-1].strip()
            description = soup.find('div', {'class': 'main mdl-cell mdl-cell--8-col\
                                             mdl-card mdl-shadow--4dp'})
            detail = description.find_all('p')[2].nextSibling
            org_info_14.append({'name': org_name, 'page': web_page,
                                'about': detail, 'mail': mailing_list,
                                'link': url})
            project_urls_from14.extend(grab_project_links(soup))
        except IndexError:
            print(url)

    return org_info_14, get_project_info(project_urls_from14)


def org_info_below_13(org_urls13):
    """Scrape information about the orgs from 2009-2013
        :org_urls13: list of urls for all the orgs
    """
    org_info_till13 = []
    project_urls_till13 = []
    for url in org_urls13:
        # General information about the org
        try:
            soup = getPage(url)
            org_name = basename(url)
            org_info = soup.find_all('p')
            web_page = org_info[0].text.splitlines()[-1].strip()
            mailing_list = org_info[1].text.split(":")[-1].strip()
            detail = org_info[2].text
            org_info_till13.append({'name': org_name, 'about': detail,
                                    'page': web_page, 'mail': mailing_list,
                                    'link': url})
            project_urls_till13.extend(grab_project_links(soup))

        except IndexError:
            print(url)

    return org_info_till13, get_project_info(project_urls_till13)


def get_project_info(project_urls):
    """Get detail information of projects from given links
        :project_urls: list of all the project urls
    """
    project_info = []
    for url in project_urls:
        soup = getPage(url)
        about = soup.find_all("p")
        title = soup.find("h3").text
        student = about[0].text.splitlines()[2].strip()
        details = about[1].text
        name = about[0].find("a").text
        project_info.append({'Organization': name, 'title': title,
                             'student': student, 'details': details,
                             'link': url})

    return project_info


def All_orgs():
    """Get links of all orgs from 2009 to 2015

        Makes two separate list:
        links_13 - links of all the Organization from 2009-2013
        links_14 - links of all the Organization 2014 and 2015
    """

    links_13 = []
    links_14 = []
    valid_url = "/?archive/?gsoc/\d+[0-9]/orgs/[a-zA-Z]+"
    for year in range(2009, 2016):
        year_url = melange + "/archive/gsoc/{}".format(year)
        soup = getPage(year_url)

        for url in soup.find_all('a'):
            if re.match(valid_url, url.get("href")):
                if year <= 2013:
                    links_13.append(join(melange, url.get("href")[1:]))
                else:
                    links_14.append(join(melange, url.get("href")[1:]))
    return links_13, links_14


def main():
    orgs_13, orgs_14 = All_orgs()
    org13, project13 = org_info_below_13(orgs_13)
    org14, projects14 = org_info_above_14(orgs_14)
    dumper(org13, "Organization_2009-2013.json")
    dumper(project13, "projects_2009-2013.json")
    dumper(org14, "Organization_2014-2015.json")
    dumper(projects14, "projects_2014-2015.json")


if __name__ == "__main__":
    main()
