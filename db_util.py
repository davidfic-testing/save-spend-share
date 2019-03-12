import sqlite3
from sqlite3 import Error

create_kids_table = """ CREATE TABLE IF NOT EXISTS kids (
                            id integer PRIMARY KEY,
                            name text NON NULL
                            );"""

create_spend_table = """ CREATE TABLE IF NOT EXISTS spend (
                             id integer PRIMARY KEY,
                             kid text NOT NULL,
                             amount integer NOT NULL,
                             date text NOT NULL,
                             FOREIGN KEY (kid) REFERENCES kids(id)
                             );"""

create_share_table = """ CREATE TABLE IF NOT EXISTS share (
                             id integer PRIMARY KEY,
                             kid text NOT NULL,
                             amount integer NOT NULL,
                             date text NOT NULL,
                             FOREIGN KEY (kid) REFERENCES kids(id)
                             );"""

create_save_table = """ CREATE TABLE IF NOT EXISTS save (
                             id integer PRIMARY KEY,
                             kid text NOT NULL,
                             amount integer NOT NULL,
                             date text NOT NULL,
                             FOREIGN KEY (kid) REFERENCES kids(id)
                             );"""

def create_connection(db):
    try:
        conn = sqlite3.connect(db)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)


def create_tables(conn, create_table_sql):
    """ create a table from the create_table_sql string
    :param conn: connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


db = 'sss.db'
if __name__ == '__main__':
    conn = create_connection(db)
    if conn is not None:
        create_tables(conn, create_kids_table)
        create_tables(conn, create_spend_table)
        create_tables(conn, create_save_table)
    else:
        print("error can't create db")
