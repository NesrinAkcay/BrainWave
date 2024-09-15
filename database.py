import sqlite3

def create_database():
    conn = sqlite3.connect('brainwave.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, username TEXT, email TEXT, password_hash TEXT)''')
    
   
    
    conn.commit()
    conn.close()

create_database()



def create_additional_tables():
    conn = sqlite3.connect('brainwave.db')
    c = conn.cursor()

    # Topics tablosu
    c.execute('''CREATE TABLE IF NOT EXISTS topics
                 (id INTEGER PRIMARY KEY, title TEXT, description TEXT, created_by INTEGER,
                 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                 FOREIGN KEY(created_by) REFERENCES users(id))''')

    # Posts tablosu
    c.execute('''CREATE TABLE IF NOT EXISTS posts
                 (id INTEGER PRIMARY KEY, user_id INTEGER, topic_id INTEGER,
                 content TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                 FOREIGN KEY(user_id) REFERENCES users(id),
                 FOREIGN KEY(topic_id) REFERENCES topics(id))''')

    # Friendships tablosu
    c.execute('''CREATE TABLE IF NOT EXISTS friendships
                 (id INTEGER PRIMARY KEY, user_id1 INTEGER, user_id2 INTEGER,
                 status TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                 FOREIGN KEY(user_id1) REFERENCES users(id),
                 FOREIGN KEY(user_id2) REFERENCES users(id))''')

    # Notifications tablosu
    c.execute('''CREATE TABLE IF NOT EXISTS notifications
                 (id INTEGER PRIMARY KEY, user_id INTEGER, content TEXT,
                 is_read BOOLEAN, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                 FOREIGN KEY(user_id) REFERENCES users(id))''')

    conn.commit()
    conn.close()

create_additional_tables()


def create_chat_table():
    conn = sqlite3.connect('brainwave.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS chats (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        message TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        is_user BOOLEAN
    )
    ''')
    conn.commit()
    conn.close()
create_chat_table()