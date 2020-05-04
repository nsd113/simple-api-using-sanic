import  sqlite3
import random
import string


conn = sqlite3.connect('userdata.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS userdata (
           id INTEGER PRIMARY KEY,
           user_name TEXT NOT NULL,
           password TEXT NOT NULL,
           object BLOB NOT NULL)""")

conn.commit()
conn.close()


def register_user_data_db(username, password):
    '''Add user to DB and check if it exist'''
    with conn:
        if cur.execute("SELECT * FROM userdata WHERE user_name = :name", {'name':username}) == None: #user not already exist   2. try with if not statment    3 mb try assert
            cur.execute("INSERT INTO userdata VALUES (:name, :pass)", {'name':username, 'pass':password})
            return 'User successfully registered'
        else:
            raise ValueError(f"User {username} already exist")

def login_user_db(username, password):
    '''User authorization'''
    token = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(13)) #check tokken is correct
    with conn:
        if not cur.execute('''SELECT * FROM userdata WHERE user_name = :name AND password = :pass''',
                           {'name':username, 'pass':password}): # ыозможно это надо сделать отдельной функцией
            raise ValueError('User name or password is not correct')

    return "f'User '{username}' successfully logged in'"

def insert_object_db(username, password, object, operation, token):
    with conn:
        cur.execute('''UPDATE userdata SET object = :object 
                       WHERE token = :token''', {'object':object, 'token':token})
        return cur.fetchone()


def get_object_db(token):
    with conn:
        cur.execute('''SELECT object FROM userdata WHERE token = :token''', {'token':token})

def remove_object_db(token, object):
    '''manipulating objects in DB'''
    with conn:
        cur.execute('''DELETE object from userdata WHERE token = :token''', {'token':token})


