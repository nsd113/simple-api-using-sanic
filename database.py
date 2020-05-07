import sqlite3
import random
import string

# cur.execute("""CREATE TABLE IF NOT EXISTS userdata (
#                    user_name TEXT,
#                    password TEXT,
#                    object BLOB)""")

def db_connect():
    conn = sqlite3.connect('userdata.db')
    return conn

def db_close_connection(conn): # close when graceful shutdown
    cur = conn.cursor()
    conn.close()

def create_table():
    with db_connect() as conn:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS userdata (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           user_name TEXT NOT NULL,
           password TEXT NOT NULL,
           object BLOB,
           token TEXT)""")
        conn.commit()

def register_user_data_db(username, password):
    '''Add user to DB and check if it exist'''
    with db_connect() as conn:
        cur = conn.cursor()
        if not cur.execute("SELECT * FROM userdata WHERE user_name = :name", {'name':username}).fetchall(): #user not already exist   2. try with if not statment    3 mb try assert
            cur.execute("INSERT INTO userdata VALUES (:name, :pass)", {'name':username, 'pass':password})
            return 'User successfully registered'
        else:
            raise ValueError(f"User {username} already exist")

def login_user_db(username, password):
    '''User authorization'''
    token = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(13)) #check tokken is correct
    with db_connect() as conn:
        cur = conn.cursor()
        if not cur.execute('''SELECT * FROM userdata WHERE user_name = :name AND password = :pass''',
                           {'name':username, 'pass':password}).fetchall(): # ыозможно это надо сделать отдельной функцией
            raise ValueError('User name or password is not correct')
    print("f'User '{username}' successfully logged in'")
    return token

def insert_object_db(object, token):
    with db_connect() as conn:
        cur = conn.cursor()
        cur.execute('''UPDATE userdata SET object = :object 
                       WHERE token = :token''', {'object':object, 'token':token})
        return cur.fetchone()

def get_object_db(token):
    with db_connect() as conn:
        cur = conn.cursor()
        cur.execute('''SELECT object FROM userdata WHERE token = :token''', {'token':token})

def remove_object_db(token, object):
    '''manipulating objects in DB'''
    with db_connect() as conn:
        cur = conn.cursor()
        cur.execute('''DELETE object from userdata WHERE token = :token''', {'token':token})


#register_user_data_db('alyona', '12357')

