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
        
    def update_file(self, file_id, updated_at):
        self.cursor.execute('''
            UPDATE arquivo
            SET data_atualizacao = ?
            WHERE id = ?
        ''', (updated_at, file_id))
        self.conn.commit()
    
    def get_file_by_pasta_id_and_nome(self, folder_id, name):
        self.cursor.execute('SELECT * FROM arquivo WHERE pasta_id = ? AND nome = ?', (folder_id, name))
        return self.cursor.fetchone()