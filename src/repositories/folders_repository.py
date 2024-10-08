import sqlite3

class FolderRepository:
    def __init__(self):
        # Initialize SQLite DB
        self._init_db()
    
    def _init_db(self):
        self.conn = sqlite3.connect('local.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS pasta (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                caminho TEXT,
                notion_id TEXT,
                configuracao_id INTEGER
            )
        ''')

        self.conn.commit()
        
    def insert_folder(self, path, notion_id, config_id):
        self.cursor.execute('''
            INSERT INTO pasta (caminho, notion_id, configuracao_id)
            VALUES (?, ?, ?)
        ''', (path, notion_id, config_id))
        self.conn.commit()
        
    def get_paths(self):
        self.cursor.execute('SELECT caminho FROM pasta')
        return self.cursor.fetchall()
    
    def get_folder_by_path(self, path):
        self.cursor.execute('SELECT * FROM pasta WHERE caminho = ?', (path,))
        return self.cursor.fetchone()