import sqlite3

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# Users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone TEXT,
    skills TEXT,
    experience TEXT,
    education TEXT,
    resume_path TEXT
)
""")

# Custom answers
cursor.execute("""
CREATE TABLE IF NOT EXISTS custom_answers (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    question TEXT,
    answer TEXT
)
""")
# Jobs table
cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY,
    url TEXT,
    company TEXT,
    role TEXT,
    ats TEXT,
    status TEXT,
    failure_reason TEXT
)
""")
cursor.execute("""
INSERT INTO users (name, email, phone, skills, experience, education, resume_path)
VALUES (
    'Demo User',
    'demo@example.com',
    '9999999999',
    'Python, ML, NLP',
    'Fresher with ML projects',
    'B.Tech IT',
    'resume.pdf'
)
""")

conn.commit()
conn.close()