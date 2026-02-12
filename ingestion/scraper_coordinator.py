import re
from bs4 import BeautifulSoup
import requests
from ingestion.scraper_fallbacks import extract_with_fallback, FIELD_SELECTORS


def crawl_entrypoint():
    region = "south-africa"
    sector = "it"
    entrypoint = f"https://www.careers24.com/jobs/lc-{region}/se-{sector}/rmt-incl/?sort=dateposted"
    return entrypoint


def crawl_listings_page(crawl_entrypoint):
    res = requests.get(crawl_entrypoint, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, 'html.parser')

    job_entries = []

    job_cards = soup.select(".job-card")
    for card in job_cards:
        job_url = card.select_one("a")["href"]
        full_url = "https://www.careers24.com" + job_url
        posted_li = card.select_one(".job-card-left").select("li")[2].contents[0].strip()
        posted_raw = posted_li.replace("Posted:", "").strip()
        job_entries.append((full_url, posted_raw))

    return job_entries


def scrape_job(job_entry):
    try:
        res = requests.get(job_entry[0], timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(res.text, 'html.parser')

        external_id = extract_with_fallback(soup, FIELD_SELECTORS["external_id"])
        title = extract_with_fallback(soup, FIELD_SELECTORS["title"])
        company = extract_with_fallback(soup, FIELD_SELECTORS["company"])
        location_text = extract_with_fallback(soup, FIELD_SELECTORS["location"])
        description_text = extract_with_fallback(soup, FIELD_SELECTORS["description"])
        salary_text = extract_with_fallback(soup, FIELD_SELECTORS["salary"])

        return {
            "source": "Careers24",
            "external_id": external_id,
            "title_raw": title,
            "company_raw": company,
            "location_raw": location_text,
            "description_raw": description_text,
            "posted_raw": job_entry[1],
            "salary_raw": salary_text,
            "url": job_entry[0]
        }
    except Exception as e:
        print("Something went wrong while scraping:", e)


# job_entrypoint = crawl_entrypoint()
# job_url = crawl_listings_page(job_entrypoint)
#
# for job in job_url:
#     job_details = scrape_job(job)
#     print(job_details)
