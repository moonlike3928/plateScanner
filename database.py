import sqlite3
from datetime import datetime

conn = sqlite3.connect('plates.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS plates (
    id INTEGER PRIMARY KEY,
    plate TEXT,
    timestamp TEXT
)''')

def log_plate(plate):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT INTO plates (plate, timestamp) VALUES (?, ?)", (plate, timestamp))
    conn.commit()
