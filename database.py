import sqlite3

DATABASE_NAME = "database.db"

def init_db():
    # Connect to the database (creates database.db if it doesn't exist)
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # 1. Users Table (For user registration & login)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # 2. Items Table (For lost & found posts, search, category, location, and status history)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT NOT NULL,
            type TEXT NOT NULL,         -- 'Lost' or 'Found'
            category TEXT NOT NULL,     -- Electronics, Keys, Documents, etc.
            location TEXT NOT NULL,     -- Library, Canteen, Hall, etc.
            description TEXT,
            status TEXT DEFAULT 'Open', -- 'Open' or 'Claimed'
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Database and tables initialized successfully!")

if __name__ == '__main__':
    init_db()