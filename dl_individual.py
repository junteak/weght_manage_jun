import sqlite3


def dl_indvidual():
    connection = sqlite3.connect('weight_manage.db')
    cursor = connection.cursor()
    sql = f"SELECT * FROM users"
    users = cursor.execute(sql).fetchall()  # users はtuple
    connection.close()

    key_users = list(
        dict(users))  # タプルのリストであるusersを 辞書化→リスト化 でキー値が得られる。 http://ututel.blog121.fc2.com/blog-entry-45.html

    num_dlt_indvisual = int(input('\n 削除する人を選んでください。> \n'))
    name_dlt_indvisual = key_users[num_dlt_indvisual - 1]

    connection = sqlite3.connect('weight_manage.db')
    cursor = connection.cursor()
    sql = f"DELETE FROM users WHERE name = '{name_dlt_indvisual}'"
    cursor.execute(sql).fetchall()
    connection.commit()
    connection.close()

    print(f' {name_dlt_indvisual}を削除しました。\n')
