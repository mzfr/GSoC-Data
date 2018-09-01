# GSoC Data

All the data from [GSoC-archive](https://developers.google.com/open-source/gsoc/past-summers) in JSON format.

# Directories

* `Data/`
    + `orgs/` - all orgs that have been a part of GSoC from 2005 to 2017

    + `projects/` - all projects that are completed under GSoC program from year 2005-2017

* `Scrapers/`
    - Contains all the scrapers used for scraping the data

# Data

### `orgs/`

* `organiztion_2005.json` - `organization_2008`
    - `link`: URL of the org
    - `name`: Name of the org

*  organization_2009-2013.json
    -  `about`: Work that org do
    -  `link`: URL of the org
    -  `mail`: Mailing list of the org
    -  `name`: Name of the org
    -  `page`: Idea page of the org

* organization_2014-2015.json
    - `link`: URL of the org
    - `mail`: Mailing list of the org
    - `page`: Idea page of the org
    - `name`: Name of the org selected

* organization_2016-2017.json
    - `about`: Info about the organization
    - `link`: URL of the org
    - `name`: Name of the org

### `projects/`

* `project_2005.json` - `project_2008.json`
    - `Mentor`: Name of the mentor of the project
    - `project`: Name of the project
    - `student`: Name of the student

* `project_2009-2013.json` & `project_2014-2015.json`
    - `Organization`: Name of the organization
    - `detail`: Detail about the project
    - `link`: Link to the project
    - `student`: Name of the student selected
    - `title`: Name of the project

* `project_2016-2017.json`
    - `Organization`: Name of the organization
    - `link`: Link to the project
    - `mentors`: Name of all the students
    - `student`: Name of the students
    - `title`: Name of the project


# Usage

This data will be used for improving functionality of [Soccer](http://dufferzafar.github.io/Soccer/)
