jerb = {
    'source': 'career24',
    'external_id': "25684",
    'title': "snr. Head Clown",
    'company': "No More Funny Bussiness",
    'location': " New Circus",
    'is_remote': False,
    'description': "Dance for senior executives",
    'url': "www.ratemyclown.com",
    'posted_at': None,
    'salary_min': 5,
    'salary_max': 5,
    'currency': "The feeling of a job well done",
    'language': "Clownish",
    'skills': {"Frontend": ["juggling", "balloon making"], "Backend": ["feeding all animals", "Manning ticketbooth"]},
}

test_jobs = [

    # 1 — Clean, normal job
    {
        "source": "linkedin",
        "external_id": "1311556",
        "title": "Senior Python Developer",
        "company": "ACME Corp",
        "location": "Johannesburg, South Africa",
        "description": "We need a Python developer with Django, Docker, AWS. Fully remote.",
        "posted_date": "6 days ago",
        "salary": "R60k - R80k per month",
        "url": "https://example.com/job1",
        "language": "English",
    },

    # 2 — Messy punctuation, emojis, missing company
    {
        "source": "career24",
        "external_id": "2786756",
        "title": "🔥🔥!?  Data Analyst  !?🔥🔥",
        "company": None,
        "location": "Cape Town",
        "description": "SQL, Python, Pandas. Office-based role.",
        "posted_date": "🔥  !?🔥  11 January  🔥!?  🔥",
        "salary": "R30000 - R40000",
        "url": "https://example.com/job2",
        "language": "English",
    },

    # 3 — Remote via location only
    {
        "source": "indeed",
        "external_id": "7871556",
        "title": "Frontend Engineer",
        "company": "Tech Solutions",
        "location": "Remote",
        "description": "React, JavaScript, HTML, CSS.",
        "posted_date": "28 / 01",
        "salary": "Negotiable",
        "url": "https://example.com/job3",
        "language": "English",
    },

    # 4 — Remote via description only
    {
        "source": "pnet",
        "external_id": "221556",
        "title": "DevOps Engineer",
        "company": "CloudWorks",
        "location": "USA",
        "description": "AWS, Docker, Kubernetes. Work from home available.",
        "posted_date": "01/09/25",
        "salary": "$120k per annum",
        "url": "https://example.com/job4",
        "language": "English",
    },

    # 5 — Missing description, missing salary
    {
        "source": "linkedin",
        "external_id": "2236356",
        "title": "Junior IT Support",
        "company": "HelpDesk Co",
        "location": "Durban",
        "description": None,
        "posted_date": None,
        "salary": None,
        "url": "https://example.com/job5",
        "language": "English",
    },

    # 6 — Salary with single value
    {
        "source": "career24",
        "external_id": "2217856",
        "title": "Backend Developer",
        "company": "ByteForge",
        "location": "Pretoria",
        "description": "Python, Flask, SQL, Docker.",
        "posted_date": "🔥  !?🔥  01/ 06/ 25  !?🔥  🔥",
        "salary": "R50k",
        "url": "https://example.com/job6",
        "language": "English",
    },

    # 7 — Salary with yearly ZAR
    {
        "source": "indeed",
        "external_id": "984984",
        "title": "Machine Learning Engineer",
        "company": "AI Labs",
        "location": "Cape Town",
        "description": "Python, TensorFlow, PyTorch, AWS.",
        "posted_date": "06 / 01",
        "salary": "R900k per annum",
        "url": "https://example.com/job7",
        "language": "English",
    },

    # 8 — No title (should be rejected later by acceptance logic)
    {
        "source": "linkedin",
        "external_id": "364648546",
        "title": None,
        "company": "Unknown",
        "location": "South Africa",
        "description": "General IT role. Python and SQL helpful.",
        "posted_date": "yesterday",
        "salary": "Market related",
        "url": "https://example.com/job8",
        "language": "English",
    },

    # 9 — Non-English language
    {
        "source": "glassdoor",
        "external_id": "3558",
        "title": "Software Engineer",
        "company": "GlobalSoft",
        "location": "Germany",
        "description": "Java, Spring Boot, AWS. Remote möglich.",
        "posted_date": "3 days ago",
        "salary": "€70k - €90k per year",
        "url": "https://example.com/job9",
        "language": "German",
    },

    # 10 — Everything messy at once
    {
        "source": "pnet",
        "external_id": "3546",
        "title": "🔥🔥!?  Full Stack Dev  !?🔥🔥",
        "company": "🔥!?  CodeWorks  !?🔥",
        "location": "🔥 Remote 🔥",
        "description": "React, Node, Docker, AWS. 🔥🔥!?  Work from anywhere  !?🔥🔥",
        "posted_date": "🔥  !?🔥  6 January  🔥!?  🔥",
        "salary": "🔥  !?🔥  R70 000 – R90 000 p/m  🔥!?  🔥",
        "url": "https://example.com/job10",
        "language": "English",
    },
]