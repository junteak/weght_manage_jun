'''

表を表示させる
https://docs.python.org/ja/3/library/sqlite3.html

'''

import sqlite3


def display_users():
    connection = sqlite3.connect('weight_manage.db')
    cursor = connection.cursor()
    sql = f"SELECT * FROM users"
    users = cursor.execute(sql).fetchall()  # users はtuple
    connection.close()  # close前に値をとらないといけない。close後だと値をとれない。なので変数に入れなければいけない。
    n = 1
    for indvidual_list in users:
        list(indvidual_list)
        print(f' {n}. {indvidual_list[0]} / {indvidual_list[1]}Kg')
        n += 1
