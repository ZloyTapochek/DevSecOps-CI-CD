from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

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

def get_fine_by_number(number):
    connection = sqlite3.connect('fines.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM fines WHERE number = ?", (number,))
    fine = cursor.fetchone()
    connection.close()
    return fine

@app.route('/', methods=['GET', 'POST'])
def index():
    fine = None
    if request.method == 'POST':
        number = request.form['number']
        fine = get_fine_by_number(number)
    return render_template('index.html', fine=fine)

if __name__ == '__main__':
    create_database()  # Создаем базу данных при запуске
    app.run(host='0.0.0.0', debug=True)  # Указываем хост для доступа извне
