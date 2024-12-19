
import sqlite3

class Database:
    def __init__(self, db_path = "C:/Users/safro/PycharmProjects/gigachat_bot/project/database/database.database"):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self._create_tables()

    def _create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                state TEXT,
                preferences TEXT
            )
        ''')
        self.connection.commit()

    def add_user(self, user_id, username, state=None, preferences=None):
        self.cursor.execute('''
            INSERT OR IGNORE INTO users (user_id, username, state, preferences) 
            VALUES (?, ?, ?, ?)
        ''', (user_id, username, state, preferences))
        self.connection.commit()

    def get_user(self, user_id):
        self.cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        return self.cursor.fetchone()

    def update_user_state(self, user_id, state):
        self.cursor.execute('''
            UPDATE users SET state = ? WHERE user_id = ?
        ''', (state, user_id))
        self.connection.commit()

    def close(self):
        self.connection.close()
