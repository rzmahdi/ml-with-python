import mysql.connector

config = {
    'user': 'root',
    'password': '11228mahdi',
    'host': 'localhost',
    'database': 'firstdb'
}
connection = mysql.connector.connect(**config)
cursor = connection.cursor()

def read():
    cursor.execute('SELECT * FROM car')
    return cursor.fetchall()

def write(model, year, mile, price):
    cursor.execute(f"INSERT INTO car(model, year, mile_age, price) VALUES('{model}', '{year}', '{mile}', '{price}')")
    connection.commit()

