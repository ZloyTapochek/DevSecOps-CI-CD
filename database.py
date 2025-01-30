import sqlite3

def create_database():
    connection = sqlite3.connect('fines.db')
    cursor = connection.cursor()
    
    # Создаем таблицу для штрафов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            number TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT NOT NULL
        )
    ''')
    
    # Пример данных
    cursor.execute("INSERT INTO fines (number, amount, description) VALUES ('123456', 100.0, 'Штраф за превышение скорости')")
    cursor.execute("INSERT INTO fines (number, amount, description) VALUES ('654321', 150.0, 'Штраф за неправильную парковку')")
    
    connection.commit()
    connection.close()

if __name__ == '__main__':
    create_database()
