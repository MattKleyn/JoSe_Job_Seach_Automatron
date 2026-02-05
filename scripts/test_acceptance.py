# scripts/test_acceptance.py

from ingestion.transformers import transform_raw_job
from acceptance.gates import accept
from acceptance.rules import (
    has_required_fields,
    is_recent,
    matches_location,
    has_skills_or_category,
    matches_personal_skills,
    is_junior,
    matches_remote_preference,
)
from tests.test_jobs import test_jobs
from acceptance.seniority import detect_seniority

def debug_accept(job):
    """Return a dict showing which rules passed/failed."""
    return {
        "required_fields": has_required_fields(job),
        "recent": is_recent(job),
        "location": matches_location(job),
        "skills_or_category": has_skills_or_category(job),
        "personal_skills": matches_personal_skills(job),
        "junior": is_junior(job),
        "remote_preference": matches_remote_preference(job),
    }


def print_job_result(i, job, checks, final, seniority):
    print(f"\n=== Job {i}: {'ACCEPTED' if final else 'REJECTED'} ===")
    print(f"Title:       {job.get('title')}")
    print(f"Company:     {job.get('company')}")
    print(f"Location:    {job.get('location')}")
    print(f"Skills:      {job.get('skills')}")
    print(f"Posted At:   {job.get('posted_at')}")
    print(f"Seniority:   {seniority}")
    print("\nRule Breakdown:")
    for rule, result in checks.items():
        print(f"  {rule:20} → {'PASS' if result else 'FAIL'}")
    print("=" * 60)


def main():
    for i, raw in enumerate(test_jobs, start=1):
        normalized = transform_raw_job(raw)
        seniority = detect_seniority(normalized.get("title"), normalized.get("description"))
        checks = debug_accept(normalized)
        final = accept(normalized)
        print_job_result(i, normalized, checks, final, seniority)


if __name__ == "__main__":
    main()