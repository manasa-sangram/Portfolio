"""
content.py  -  ALL the text of your website lives here.

The templates (HTML) decide HOW things look. This file decides WHAT they say.
To change a sentence, a link, a book or a photo caption, edit this file only.

Everything marked TODO is a placeholder for YOU to fill in. I only used facts
from your resume and from what you told me; I did not invent anything personal.

The sections appear on the site in the same order as the QUESTS list below.
"""

# ---------------------------------------------------------------------------
# Basic identity (sidebar, page title, footer)
# ---------------------------------------------------------------------------
SITE = {
    "name": "Manasa Sangram Ashok",
    "short_name": "Manasa",
    "tagline": "Data & ML engineer building reliable pipelines and learning from time-series data.",
    "location": "Rostock, Germany (open to relocation / remote)",
    # TODO: replace with your real profile links
    "linkedin": "https://www.linkedin.com/in/manasa-sangram-ashok-807a731b2/",
    "github": "https://github.com/manasa-sangram",
    "substack": "https://substack.com/@manasasangram",
    "loom": "https://www.loom.com/share/YOUR-VIDEO-ID",
    # Put your resume PDF in the static/ folder with exactly this name.
    # The "Resume" buttons only appear once the file exists.
    "resume_file": "Manasa_Resume.pdf",
}

# The sidebar menu. (id, label). The id must match the id of the section in
# templates/sections/. Order here = order in the menu.
QUESTS = [
    {"id": "highlights", "label": "Highlights"},
    {"id": "work", "label": "Work & Projects"},
    {"id": "lookbook", "label": "Personal Lookbook"},
    {"id": "corner", "label": "My Corner"},
    {"id": "german", "label": "German Journey"},
    {"id": "videos", "label": "Videos"},
    {"id": "education", "label": "Education"},
    {"id": "offduty", "label": "When I'm not working"},
    {"id": "contact", "label": "Write to me"},
]

# ---------------------------------------------------------------------------
# 1. Highlights about me
# ---------------------------------------------------------------------------
HIGHLIGHTS = {
    "headline": "Hi, I'm Manasa.",
    # The "I love ..." line rotates through these
    "loves": [
        "building data pipelines",
        "finding anomalies in ocean data",
        "dancing",
        "reading",
        "hitting the gym",
        "running",
        "journalling",
    ],
    "welcome": "welcome to my little web packet",
    "intro": (
        "I'm a 25 year old Data and Machine Learning Engineer based in "
        "Rostock. I believe that we are lucky to be having a front row seat "
        "in this new AI revolution"
    ),
    "looking_for": "Open to Data Engineer and Machine Learning Engineer roles (full time). Open to relocation and remote.",
    # The skills list under the intro: a group name and the skills in it
    "skills": [
        {"group": "Data & ML", "items": ["Python", "SQL", "Pandas", "Machine learning" , "Time Series analysis" , "Anamoly Detection"]},
        {"group": "Pipelines & APIs", "items": ["FastAPI", "RabbitMQ", "Docker", "Streamlit"]},
        {"group": "Testing & delivery", "items": ["Playwright", "TypeScript", "Git", "CI/CD"]},
    ],
    # "At a glance": the key facts
    "stats": [
        {"label": "Role", "value": "Data & ML Engineer"},
        {"label": "Location", "value": "Rostock, Germany"},
        {"label": "Experience", "value": "2+ years"},
        {"label": "Languages", "value": "English C1 · German B1"},
        {"label": "Currently", "value": "Master's thesis at IOW"},
        {"label": "Looking for", "value": "Full-time Data / ML Engineer role"},
    ],
}

# ---------------------------------------------------------------------------
# 2. Work (tab 1) and Projects (tab 2)
# ---------------------------------------------------------------------------
WORK = [
    {
        "role": "Master's Thesis: Anomaly Detection in CTD Data using Machine Learning",
        "where": "Leibniz Institute for Baltic Sea Research Warnemünde (IOW), Rostock",
        "dates": "Sep 2026 - present",
        "current": True,  # shows "Current" next to the dates
        "bullets": [
            "The Oceanographic sensors collect high frequency data (CTD) which is prone to errors",
            "I am building a machine learning pipeline to detect these errors and anamolies using Isolation Forests , TS2Vec and Chronos-2"
            "I am Comparing unsupervised methods, self-supervised learning (TS2Vec embeddings) and a foundation model (Chronos-2) for automated data quality assessment.",
            "Goal: find errors in high-frequency oceanographic time series automatically.",
        ],
        # TODO: add links when you publish. Leave "" to hide the button.
        "links": [
            {"label": "Read the write-up (Substack)", "url": ""},
            {"label": "Watch the walkthrough (Loom)", "url": ""},
        ],
    },
    {
        "role": "Working Student, Data Engineering & Software Automation",
        "where": "Suzlon Energy, Rostock",
        "dates": "Mar 2025 - present",
        "bullets": [
            "I built a multithreaded Python framework which fetches around 800 workitems from the Polarion API and renders them into text files",
            "I developed a YAML-configured Streamlit dashboard so PLC engineers can add configurations and start the FLEX5 application.",
            "I documented pipelines and set up Git version control, code-quality standards and CI/CD across teams.",
        ],
    },
    {
        "role": "Software Engineer, Quality Assurance & Test Engineer",
        "where": "Oracle Corporation, Bengaluru",
        "dates": "Sep 2023 - Nov 2024",
        "bullets": [
            "I helped in building test suites for Oracle MyLearn Platform",
            "Debugged root causes of production pipeline in agile, cross-functional teams.",
            "Kept zero critical vulnerabilities across 4 enterprise releases by adding automated security scans to CI.",
        ],
    },
]

PROJECTS = [
    {
        "name": "Polarion Parameter File Generator",
        "stack": ["Python", "Multithreading", "Polarion API"],
        "text": "A multithreaded Python framework that fetches workitems from Polarion API and renders them into text files ",
        "link": "",  
    },
        {
                            "name": "NutriQuest- Calculate yourProtein goals from grocery list and have meal suggestions",
                            "stack": ["Python", "Flet", "XP Engine" , "OPENAI API" , "USDA API"],
                            "text": "Instead of tracking nutrition only after preparing a meal, NutriQuest aims to help users make more informed grocery choices, understand their nutritional progress, and discover meals they can prepare with the ingredients they buy ",
                            "link": "https://github.com/manasa-sangram/NutriQuest-Flet",  # 
                    },
        
        {
            "name": "My Wardrode - Outfit Recommendor based on Season and Occasion",
            "stack": ["CNN", "ResNet", "Data Augmentation" ],
            "text": "A smart, personalized outfit‑recommendation application built using Streamlit and a PyTorch‑based image classification model ",
            "link": "https://github.com/manasa-sangram/My_Wardrode",  # 
            },
            

    {
        "name": "Automatic Identification System (GPS for ships)",
        "stack": ["Python", "FastAPI", "RabbitMQ", "Streamlit", "Docker"],
        "text": "Decrypted the AIS NMEA messages using RabbitMQ , stored it in PostgreSQL and visualized it on a Streamlit dashboard.",
        "link": "",  # TODO: GitHub link
    },
    {
        "name": "AI Invoice Tracker Agent - Used to track expenses",
        "stack": ["n8n", "Python", "REST APIs", "Google APIs"],
        "text": " Payment receipts arrive through Telegram, an LLM extracts the fields, and verified data is written to Excel tables.",
        "link": "https://github.com/manasa-sangram/AI_Invoice_Agent",  
    },
]

# ---------------------------------------------------------------------------
# 3. Personal Lookbook: tab "Travel" and tab "New things I'm trying"
# "file" = a file name inside static/photos/. Until the file exists, a coloured
# placeholder is shown. Add or remove entries freely.
# ---------------------------------------------------------------------------
LOOKBOOK_TRAVEL = [
    {"file": "munich.jpg", "caption": "Munich 2025"},
    {"file": "host.jpg", "caption": "I like hosting events"},
    {"file": "locking.jpg", "caption": " Dance club"},
    {"file": "dance.jpg", "caption": "My dance floor"},
]
LOOKBOOK_NEW = [
    {"file": "kashmir.webp", "caption": "Kashmir trip 2024"},
    {"file": "new2.jpg", "caption": "TODO new thing"},
    {"file": "new3.jpg", "caption": "TODO new thing"},
    {"file": "new4.jpg", "caption": "TODO new thing"},
]
COMMUNITIES = [
    {"file": "kashmir.webp", "caption": "Kashmir trip 2024"},
    {"file": "new2.jpg", "caption": "TODO new thing"},
    {"file": "new3.jpg", "caption": "TODO new thing"},
    {"file": "new4.jpg", "caption": "TODO new thing"},
]

# ---------------------------------------------------------------------------
# 4. My Corner: Substack, podcasts, books, what excites me, music, lessons
# "entries" is a list of short lines. "link" is optional.
# ---------------------------------------------------------------------------
CORNER = [
    {"file": "substack.md", "title": "Substack",
     "text": "My writing lives on Substack. I write about Book reviews and what i notice in my day to day life.",
     "link": SITE["substack"], "link_label": "Read on Substack"},
    {"file": "podcasts.txt", "title": "Podcasts I listen to",
     "entries": ["https://www.youtube.com/watch?v=4Vz6L8B73i4", "https://www.youtube.com/@theschooloflifetv"]},
    {"file": "books.txt", "title": "Books I read",
     "entries": ["The World I see - Dr Fei Fei Li", "White Nights - Fyodor Dostoyevsky", "Norweigeen Wood - Haruki Murakami"]},
    {"file": "curious_about.txt", "title": "New things that excite me",
     "entries": ["Neuroplasticity", "Game engines"]},
    {"file": "music.txt", "title": "Music I listen to",
     "entries": ["https://open.spotify.com/track/0wHYuCTWPntEgWiUVED4wB?si=xXz8fBVvS4KRHOVKsevvEQ&utm_source=native-share-menu"]},
    {"file": "lessons_2026.txt", "title": "Lessons I learnt this year",
     "entries": ["You write your own story", "Be grateful"]},
]

# ---------------------------------------------------------------------------
# 5. My German language journey
# Your resume says German B1 (conversational), so A1 and A2 are marked done.
# "state" can be: done, current, next, later
# ---------------------------------------------------------------------------
GERMAN = {
    "intro": "TODO: tell the story. Why you started learning German, what was hardest, what helped.",
    "levels": [
        {"code": "A1", "name": "Beginner", "state": "done"},
        {"code": "A2", "name": "Elementary", "state": "done"},
        {"code": "B1", "name": "Intermediate", "state": "current"},
        {"code": "B2", "name": "Upper-intermediate", "state": "next"},
        {"code": "C1", "name": "Advanced", "state": "later"},
    ],
    "milestones": [
        {"when": "TODO: date", "text": "TODO: a milestone, e.g. first conversation, passed an exam"},
        {"when": "TODO: date", "text": "TODO: another milestone"},
        {"when": "TODO: date", "text": "TODO: another milestone"},
    ],
}

# ---------------------------------------------------------------------------
# 6. Videos. Leave "url" empty and the row shows "Coming soon".
# ---------------------------------------------------------------------------
VIDEOS = [
    {
        "title": "AI agents, explained",
        "text": "I learnt about AI agents and explained them in my own words.",
        "url": "",  # TODO: paste your Loom link here
    },
    {
        "title": "More Loom videos",
        "text": "New self-explaining videos will land here.",
        "url": "",
    },
]

# ---------------------------------------------------------------------------
# 7. Education: Cluny Convent -> SJCIT -> University of Rostock
# ---------------------------------------------------------------------------
EDUCATION = [
    {"school": "Cluny Convent", "what": "TODO: e.g. school", "years": "2017"},
    {"school": "SJCIT", "what": "Bachelors of Engineering - Computer Science", "years": "2019 - 2023"},
    {"school": "University of Rostock", "what": "M.Sc. Computer Science (AI focus)", "years": "Oct 2024 - present",
     "note": "Focus: machine learning, advanced software architectures, computer vision."},
]

# ---------------------------------------------------------------------------
# 8. When I'm not working: dance, read, gym, run, journal
# ---------------------------------------------------------------------------
HOBBIES = [
    {"title": "Dance", "text": "I've tried many styles.",
     "tags": ["Locking", "Hip-hop", "Jazz", "K-pop"]},
    {"title": "Reading", "text": "Reading Good Material - Dolly Alderton", "tags": []},
    {"title": "Gym", "text": "My only source of endorphins.", "tags": []},
    {"title": "Running", "text": "I like running near the harbour.", "tags": []},
    {"title": "Journalling", "text": "I journal to reflect on my thoughts and experiences.", "tags": []},
]
