import sqlite3

class ConfigRepository:
    def __init__(self):
        # Initialize SQLite DB
        self._init_db()
    
    def _init_db(self):
        self.conn = sqlite3.connect('local.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS configuracao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                notion_key TEXT,
                notion_id TEXT
            )
        ''')

        self.conn.commit()
        
    def insert_config(self, notion_key, notion_id):
        self.cursor.execute('DELETE FROM configuracao')
        self.conn.commit()
        
        self.cursor.execute('''
            INSERT INTO configuracao (notion_key, notion_id)
            VALUES (?, ?)
        ''', (notion_key, notion_id))
        self.conn.commit()
        
    def get_config(self):
        self.cursor.execute('SELECT notion_key, notion_id FROM configuracao ORDER BY id DESC LIMIT 1')
        return self.cursor.fetchone()
    
    def get_config_id(self):
        self.cursor.execute('SELECT id FROM configuracao')
        row = self.cursor.fetchone()
        if row:
            return row[0]
        else:
            return None
    
    def get_notion_id(self):
        self.cursor.execute('SELECT notion_id FROM configuracao ORDER BY id DESC LIMIT 1')
        row = self.cursor.fetchone()
        if row:
            return row[0]
        else:
            return None
    
    def get_headers(self):
        self.cursor.execute('SELECT notion_key FROM configuracao')
        
        row = self.cursor.fetchone()
        
        if row:
            notion_key = row[0]
            
            headers = {
                'Authorization': f'Bearer {notion_key}',
                'Content-Type': 'application/json',
                'Notion-Version': '2022-06-28'
            }
            
            return headers
        else:
            return None