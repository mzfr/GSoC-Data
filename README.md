# GSoC Data

All the data from [GSoC-archive](https://developers.google.com/open-source/gsoc/past-summers) in JSON format.


__NOTE__
For running the scrapers you must install the following dependencies
* asyncio
* aiohttp

You can do that by running: `pip install ayncio aiohttp`

# Directories

* `Data/`
    + `orgs/` - all orgs that have been a part of GSoC from 2005 to 2017

    + `projects/` - all projects that are completed under GSoC program from year 2005-2017

* `Scrapers/`
    - Contains all the scrapers used for scraping the data

# Data

### `orgs/`

* `2005.json` - `2008.json`
    - `link`: URL of the org
    - `name`: Name of the org

* `2009-2013.json`
    -  `about`: Work that org do
    -  `link`: URL of the org
    -  `mail`: Mailing list of the org
    -  `name`: Name of the org
    -  `page`: Idea page of the org

* `2014-2015.json`
    - `link`: URL of the org
    - `mail`: Mailing list of the org
    - `page`: Idea page of the org
    - `name`: Name of the org selected

* `2016-2017.json`
    - `about`: Info about the organization
    - `link`: URL of the org
    - `name`: Name of the org

### `projects/`

* `2005.json` - `2008.json`
    - `Mentor`: Name of the mentor of the project
    - `project`: Name of the project
    - `student`: Name of the student

* `2009-2013.json` & `2014-2015.json`
    - `Organization`: Name of the organization
    - `detail`: Detail about the project
    - `link`: Link to the project
    - `student`: Name of the student selected
    - `title`: Name of the project

* `2016-2017.json`
    - `Organization`: Name of the organization
    - `link`: Link to the project
    - `mentors`: Name of the mentors
    - `student`: Name of the student
    - `title`: Name of the project


# What can be done with the data?

This data will be used for improving the functionality of [Soccer](http://github.com/dufferzafar/Soccer/).

It can also be used to generate various stats, plots or answer data-related questions like:

- Who did the most number of GSoCs? under which org?
- Which org has the highest sutdent-to-mentor conversion rate? (students who first did GSoC under the org, and then became mentors)
- Run some magic on the descriptions of projects over the years to find out if there is a trend of ML related projects.

etc. etc.

---

Feel free to open issues to discuss any more ideas!
