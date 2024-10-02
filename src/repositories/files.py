import sqlite3

class FileRepository:
    def __init__(self):
        # Initialize SQLite DB
        self._init_db()
        
    def _init_db(self):
        self.conn = sqlite3.connect('local.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS arquivo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                notion_id TEXT,
                data_atualizacao DATETIME,
                pasta_id INTEGER
            )
        ''')

        self.conn.commit()
        
    def insert_file(self, name, notion_id, updated_at, folder_id):
        self.cursor.execute('''
            INSERT INTO arquivo (nome, notion_id, data_atualizacao, pasta_id)
            VALUES (?, ?, ?, ?)
        ''', (name, notion_id, updated_at, folder_id))
        self.conn.commit()
    
    def get_files(self):
        self.cursor.execute('SELECT * FROM arquivo')
        return self.cursor.fetchall()
    
    def get_file(self, file_id):
        self.cursor.execute('SELECT * FROM arquivo WHERE id = ?', (file_id,))
        return self.cursor.fetchone()