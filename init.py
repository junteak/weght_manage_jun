'''

テーブルを作る
https://docs.python.org/ja/3/library/sqlite3.html

'''

import sqlite3


def main():
    connection = sqlite3.connect('weight_manage.db')  # インスタンス化して引数名 sqlite3 が開いて weight_manage がテーブル名になる

    sql = """create table users (
                name text,  
                weight integer
        )"""

    cursor = connection.cursor()  # カーソルを出す。マウスのポインタのような。

    cursor.execute(sql)  # 引数sqlコマンドを実行する。

    connection.commit()  # 保存する

    connection.close()  # 閉じる


if __name__ == '__main__':
    main()
