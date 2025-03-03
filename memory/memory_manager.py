import sqlite3
from config import SQLITE_DB_PATH

def init_db():
    conn = sqlite3.connect(SQLITE_DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY,
                        task_text TEXT,
                        status TEXT)''')
    conn.commit()
    conn.close()

def save_task(task_text, status="pending"):
    conn = sqlite3.connect(SQLITE_DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task_text, status) VALUES (?, ?)", (task_text, status))
    conn.commit()
    conn.close()
