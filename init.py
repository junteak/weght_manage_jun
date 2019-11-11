'''

テーブルを作る
https://docs.python.org/ja/3/library/sqlite3.html

'''

import sqlite3


def main():
    # インスタンス化
    connection = sqlite3.connect('weight_manage.db')

    sql = """create table users (
                name text,  
                weight integer
        )"""

    cursor = connection.cursor()

    cursor.execute(sql)

    connection.commit()

    connection.close()


if __name__ == '__main__':
    main()
