import sqlite3
from sqlite3 import Error

db_name = 'sss.db'


def connect_to_db():
    """ connects to sqlite db specified as `db` 
        and returns a cursor to it 
    """
    try:
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        return c
    except Error as e:
        print(e)


def get_kids():
    cursor = connect_to_db()
    cursor.execute('SELECT name from kids')
    kids = []
    rows = cursor.fetchall()
    for row in rows:
        kids.append(row)

    return kids

def add_money(amount,name):
    pass

