**JoSe - Job Search Automatron:**
It's tough trying to prioritize between looking for work while also continuously learning and sharping my skills and while juggling all the projects that I want to build.
So to hit a few birds with a single stone Ive decided to build a simple (for now) web scraper using Python. This checks a few boxes for me, [1] it will help reduce the time looking for and sifting through job postings, [2] I will be abel to aggregate job listings from multiple sites, and track them so I can better follow where I've applied and what the statuses are, [2.5] a feature for once the MVP is complete is to automate the process a bit in terms of job application processes as they take a ridiculous amount of time per posting, [3] I will be able to put my python knowledge to the test and have a portfolio piece to show for it, [4] also a future feature, a freelance work aggregator, by ethically scraping freelance sites, i could hopefully identify oppertunites that matches my skillset while I look for permanent employment.

**Installation instructions:**
Currently a CLI tool, fork from github, then run locally from your terminal to utilise.

**Usage:**
The MVP will be a CLI tool, however later iterations will have a browser based UI written with Python and Flask.
Once downloaded, cd over to the root directory for the project, run from your terminal:
    python main.py scrape careers24 --term python --location johannesburg

**Features:**
Scrappy boi

**Tech Stack:**
Python

**Architecture Notes:**
Folder structure:
jose/
│
├── main.py
│
├── ingestion/
│   ├── __init__.py
│   ├── careers24_scraper.py
│   ├── transformers.py
│   ├── acceptance.py
│
├── core/
│   ├── __init__.py
│   ├── db.py
│   ├── jobs_repository.py
│
├── models/
│   ├── __init__.py
│   ├── raw_job.py
│   ├── normalized_job.py
│
├── utils/
│   ├── __init__.py
│   ├── http.py
│   ├── parsing.py
│
├── config/
│   ├── settings.py
│
└── tests/
    ├── test_scraper.py
    ├── test_transformer.py
    ├── test_acceptance.py

**Known Issues and Limitations:**
For the MVP the script will be run from the CLI and will only scrape a single job posting website. Respecting the /robots.txt for the site is a manual process at the moment. The MVP will also only have persistance through a PostgreSQL DB.

**Problems and Solutions:**
None atm.

**Future Plans:**
The MVP architecture and system is design to be extensible, so once it is complete the following features will be added (not an exhaustive list):
- Automatic respecting of /robots.txt,
- Additional scrapers for job posting sites,
- Job posting ranking and filtering prior to saving on DB,
- Includes incremental load to DB by checking post states,
- Browser based UI (Python backend),
- Job list extracting to .txt file and send via email,
- Automated job applications where relevancy scores above certain percentage.

**Contributing:**
If you would like to contribute to the project, feel free to fork and let me know what your plans are before PR.
I would appreciate any code reviews or suggestions, feel free to get in touch in Github or even LinkedIn (links below).

**License:**
This is a project I'm building for my self to help with my job search, if you are also looking for work or just want to play around with the code and experiment, feel free to do so.
Please do not use this for commercial purposes or for resale to any persons. 

**Contact:**
Matthew kleynhans
[Github](https://github.com/MattKleyn)
[LinkedIn](https://www.linkedin.com/in/matthew-kleynhans-00242195)