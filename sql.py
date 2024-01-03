import mysql.connector

config = {
    'user': 'user',
    'password': 'password',
    'host': 'host',
    'database': 'database'
}
connection = mysql.connector.connect(**config)
cursor = connection.cursor()

def read():
    cursor.execute('SELECT * FROM table_name')
    return cursor.fetchall()

def write(model, year, mile, price):
    cursor.execute(f"INSERT INTO table_name(model, year, mile_age, price) VALUES('{model}', '{year}', '{mile}', '{price}')")
    connection.commit()