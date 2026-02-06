import psycopg2
from psycopg2.extras import Json
from core.db import get_connection
from models.normalized_job import NormalizedJob
from ingestion.transformers import transform_raw_job
from acceptance.gates import accept


def upsert_job(job: NormalizedJob) -> None:
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
        '''
        INSERT INTO jobs (source, external_id, title, company, location, is_remote, description, url, posted_at, salary_min, salary_max, currency, language, skills)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (source, external_id)
        DO UPDATE SET
            title = EXCLUDED.title,
            company = EXCLUDED.company,
            location = EXCLUDED.location,
            is_remote = EXCLUDED.is_remote,
            description = EXCLUDED.description,
            url = EXCLUDED.url,
            posted_at = EXCLUDED.posted_at,
            salary_min = EXCLUDED.salary_min,
            salary_max = EXCLUDED.salary_max,
            currency = EXCLUDED.currency,
            language = EXCLUDED.language,
            skills = EXCLUDED.skills,
            updated_at = NOW();
            ''', (job["source"], job["external_id"], job["title"], job["company"], job["location"], job["is_remote"], job["description"], job["url"], job["posted_at"], job["salary_min"], job["salary_max"], job["currency"], job["language"], Json(job["skills"])))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print("Upsert failed:", e)

# for raw_job in scraper:
#     normalized = transform_raw_job(raw_job)
#     if accept(normalized):
#         upsert_job(normalized)