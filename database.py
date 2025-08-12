# database.py
import sqlite3
import os

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

# Connect to database in 'data/' directory
conn = sqlite3.connect("data/athletes.db", check_same_thread=False)
c = conn.cursor()

# Create table
def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS profiles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    sport TEXT,
                    location TEXT,
                    bio TEXT,
                    achievements TEXT,
                    skills TEXT
                )''')
    conn.commit()

# Insert new profile
def add_profile(name, sport, location, bio, achievements, skills):
    c.execute('''INSERT INTO profiles (name, sport, location, bio, achievements, skills)
                 VALUES (?, ?, ?, ?, ?, ?)''',
              (name, sport, location, bio, achievements, skills))
    conn.commit()

# Retrieve all profiles
def get_profiles():
    c.execute('SELECT * FROM profiles')
    return c.fetchall()

# Retrieve single profile by name (optional)
def get_profile_by_name(name):
    c.execute('SELECT * FROM profiles WHERE name = ?', (name,))
    return c.fetchone()
import sqlite3

def create_table():
    conn = sqlite3.connect('data/athlete_db.sqlite')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS profiles (
        athlete_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        sport TEXT,
        skills TEXT,
        location TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS training_data (
        athlete_id INTEGER,
        strength INTEGER,
        endurance INTEGER,
        flexibility INTEGER,
        PRIMARY KEY (athlete_id),
        FOREIGN KEY (athlete_id) REFERENCES profiles (athlete_id)
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS milestones (
        athlete_id INTEGER,
        description TEXT,
        date DATE,
        PRIMARY KEY (athlete_id, description),
        FOREIGN KEY (athlete_id) REFERENCES profiles (athlete_id)
    )
    """)
    conn.commit()
    conn.close()


def get_profile():
    conn = sqlite3.connect('data/athlete_db.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM profiles WHERE athlete_id = ?", (1,))
    profile = cursor.fetchone()  # Assuming athlete_id = 1 for demo
    conn.close()

    if profile is None:
        return None  # Return None if no profile is found

    return {
        "name": profile[1],
        "sport": profile[2],
        "skills": profile[3],
        "location": profile[4]
    }


def get_training_data():
    conn = sqlite3.connect('data/athlete_db.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM training_data WHERE athlete_id = ?", (1,))
    data = cursor.fetchone()  # Fetching training data for athlete_id = 1
    conn.close()
    return {
        "strength": data[1],
        "endurance": data[2],
        "flexibility": data[3]
    }

def get_milestones():
    conn = sqlite3.connect('data/athlete_db.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM milestones WHERE athlete_id = ?", (1,))
    milestones = cursor.fetchall()
    conn.close()
    return [m[1] for m in milestones]  # Return the description of each milestone
