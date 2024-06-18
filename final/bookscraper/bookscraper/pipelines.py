from itemadapter import ItemAdapter
import sqlite3

class DatabasePipeline:

    def open_spider(self, spider):
        # Se connecter à la base de données
        # Créer la table si elle n'existe pas
        self.connection = sqlite3.connect('books.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                price TEXT,
                upc TEXT
            )
        ''')
        self.connection.commit()

    def close_spider(self, spider):
        # Fermer la connexion à la base de données
        self.connection.close()

    def process_item(self, item, spider):
        # Insérer les données dans la base de données
        self.cursor.execute('''
            INSERT INTO books(
                title, 
                price, 
                upc) 
                VALUES (?, ?, ?)
        ''', 
        (item['title'],
        item['price'],
        item['upc']))
        self.connection.commit()
        return item

class BookscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        price = adapter.get('price')
        cleaned_price = price.replace('£', '')
        adapter['price'] = float(cleaned_price)
        return item