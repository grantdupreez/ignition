__import__('pysqlite3')
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("db.sqlite")
cursor = conn.cursor()

# Create 'chat' table
cursor.execute('CREATE TABLE IF NOT EXISTS chat (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, 
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP, updated_at DATETIME DEFAULT CURRENT_TIMESTAMP);')

# Create 'sources' table
cursor.execute('CREATE TABLE IF NOT EXISTS sources (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, source_text TEXT,
        type TEXT DEFAULT "document", chat_id INTEGER, FOREIGN KEY (chat_id) REFERENCES chat(id));')


# Create 'messages' table
cursor.execute('CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, chat_id INTEGER NOT NULL,
        sender TEXT NOT NULL, content TEXT NOT NULL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY(chat_id) REFERENCES chat(id));')

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

print("Tables created successfully.")
