from flask import Flask, request
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(dbname='facebook', user='postgres', password='kirian', host='localhost')

USERS = [
    {
        'name': 'Кирилл',
        'age': 34
    },
    {
        'name': 'Маша',
        'age': 26
    },
    {
        'name': 'Димон',
        'age': 46
    },
]


@app.get('/users')
def get_users():
    cursor = conn.cursor()
    sql_create_database = "insert into users (name, age) values ('Леонид', 28)"
    cursor.execute(sql_create_database)
    conn.commit()
    filter_age = request.args.get('age')
    if filter_age:
        new_users = []
        for user in USERS:
            if user['age'] > int(filter_age):
                new_users.append(user)
            return new_users
    return USERS


@app.post('/users')
def create_users():
    cursor = conn.cursor()
    name = request.form.get('name')
    age = request.form.get('age')
    sql_create_database = f"insert into users (name, age) values ('{name}', {age})"
    cursor.execute(sql_create_database)
    conn.commit()
    return 'User created'


@app.get('/users')
def get_users():
    cursor = conn.cursor()
    sql_create_database = "select * from users"
    cursor.execute(sql_create_database)
    result = cursor.fetchall()
    return result


#
@app.post('/users')
def create_users():
    cursor = conn.cursor()
    name = request.form.get('name')
    age = request.form.get('age')
    sql_create_database = f"insert into users (name, age) values ('{name}', {age})"
    cursor.execute(sql_create_database)
    conn.commit()
    return 'User created'
