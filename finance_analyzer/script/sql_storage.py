import sqlite3

def get_connection(name='finance'):
    conn = sqlite3.connect(f'db/{name}.db')
    return conn

