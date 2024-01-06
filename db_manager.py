import sqlite3

class ManageDB:
    def __init__(self, post_db_path):
        self.conn = sqlite3.connect(post_db_path)
        self.cursor = self.conn.cursor()
        self._setup_database()
    
    def _setup_database(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS html_files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category_id INTEGER,
                domain TEXT,
                html TEXT
            )
        ''') 
        self.conn.commit()

    def _collect_data(self):
        conn = sqlite3.connect("C:/Users/bruker/Desktop/WebScraperDriftDesignV010/website.db")
        cursor = conn.cursor()
        cursor.execute('SELECT category_id, domain_name FROM domains')
        result = cursor.fetchall()

        domains = {}
        print("Collected data")
        print(len(result))
        start_index = 5569

        for index, row in enumerate(result):
            if index > start_index:
                category_id, domain_name = row
                if category_id not in domains:
                    domains[category_id] = []
                domains[category_id].append(domain_name)
            else:
                print(index)
        return domains

    def _insert_data(self, post_db_path, category_id, domain, html):
        self.conn = sqlite3.connect(post_db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute('INSERT INTO html_files (category_id, domain, html) VALUES (?, ?, ?)', (category_id, domain, html))
        self.conn.commit()
    
    def _close_database(self):
        self.conn.close()
