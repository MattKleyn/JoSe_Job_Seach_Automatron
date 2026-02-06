import re
from bs4 import BeautifulSoup
import requests

def crawl_entrypoint():
    region = "south-africa"
    sector = "it"
    entrypoint = "https://www.careers24.com/jobs/lc-gauteng/se-it/sf-12000/su-4/rmt-incl/?sort=dateposted"
    # entrypoint = f"https://www.careers24.com/jobs/lc-{region}/se-{sector}/rmt-incl/?sort=dateposted"
    return entrypoint


def crawl_listings_page(crawl_entrypoint):
    res = requests.get(crawl_entrypoint)
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
        res = requests.get(job_entry[0])
        soup = BeautifulSoup(res.text, 'html.parser')
        title = soup.find("h1").contents[2].getText()
        details_list = soup.select(".detailsList")
        details = details_list[0]
        location_li = details.select_one("li")
        location_text = location_li.get_text(separator=" ", strip=True)
        salary_li = details.find("li", class_="elipses")
        salary_text = salary_li.get_text(" ", strip=True)
        ref_li = details.select(" li")[4].getText()
        external_id = re.sub(r"(?i)reference:", "", ref_li)
        company = soup.find("strong").getText()
        description1 = soup.select_one(".v-descrip")
        description2 = soup.select_one(".c24-vacancy-details")
        if description1:
            paragraphs = description1.find_all("p")
            description_text = "\n".join(
                p.get_text(" ", strip=True) for p in paragraphs
            )
        elif description2:
            paragraphs = description2.find_all("p")
            description_text = "\n".join(
                p.get_text(" ", strip=True) for p in paragraphs
            )
        else:
            description_text = None

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
