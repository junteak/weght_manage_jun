'''

ユーザーを登録する
https://docs.python.org/ja/3/library/sqlite3.html

'''

import sqlite3


def add_menbers(name, weight):
    connection = sqlite3.connect('weight_manage.db')
    cursor = connection.cursor()
    sql = f"INSERT INTO users (name, weight) VALUES (?, ?)"
    cursor.execute(sql, (name, weight))
    connection.commit()
    connection.close()
