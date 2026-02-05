from acceptance.rules import (
    has_required_fields,
    is_recent,
    matches_location,
    has_skills_or_category,
    matches_personal_skills,
    is_junior,
matches_remote_preference
)

def accept(job) -> bool:
    return (
        has_required_fields(job)
        and is_recent(job)
        and matches_location(job)
        and has_skills_or_category(job)
        and matches_personal_skills(job)
        and is_junior(job)
        and matches_remote_preference(job)
    )