from datetime import datetime, timedelta
from acceptance.config import MY_TECH_SKILLS, MAX_JOB_AGE_DAYS, ACCEPT_COUNTRY, BE_REMOTE
from acceptance.categories import detect_category
from acceptance.seniority import detect_seniority


def has_required_fields(job):
    return all([
        job.get("title"),
        job.get("external_id"),
        job.get("description"),
    ])


def matches_remote_preference(job):
    if not BE_REMOTE:
        return True
    return job.get("is_remote") is True


def is_recent(job):
    posted = job.get("posted_at")
    if not posted:
        return False
    return posted >= datetime.today() - timedelta(days=MAX_JOB_AGE_DAYS)


def matches_location(job):
    loc = (job.get("location") or "").lower()
    return ACCEPT_COUNTRY in loc


def has_skills_or_category(job):
    skills = job.get("skills", [])
    if skills:
        return True

    category = detect_category(job.get("title"))
    return category is not None


def matches_personal_skills(job):
    skills = job.get("skills", [])
    return any(s in MY_TECH_SKILLS for s in skills)


def is_junior(job):
    seniority = detect_seniority(job.get("title"), job.get("description"))
    return seniority in ("junior", "unknown")