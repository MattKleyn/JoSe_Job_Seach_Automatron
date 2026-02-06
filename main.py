from ingestion.transformers import transform_raw_job
from ingestion.scraper_coordinator import crawl_listings_page, crawl_entrypoint, scrape_job
from acceptance.gates import accept
from core.jobs_repository import upsert_job


def run_ingestion():
    entrypoint = crawl_entrypoint()
    job_entries = crawl_listings_page(entrypoint)

    for job_entry in job_entries:
        raw = scrape_job(job_entry)

        if not raw:
            continue  # scraper failed, skip

        normalized = transform_raw_job(raw)

        if accept(normalized):
            upsert_job(normalized)

        # Optional: print for debugging
        print("---- RAW ----")
        print(raw)
        print("---- NORMALIZED ----")
        print(normalized)
        print("---- ACCEPTED ----" if accept(normalized) else "---- REJECTED ----")
        print()

run_ingestion()