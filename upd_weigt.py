import sqlite3


def upd_weight():
    connection = sqlite3.connect('weight_manage.db')
    cursor = connection.cursor()
    sql = f"SELECT * FROM users"
    users = cursor.execute(sql).fetchall()  # users はtuple
    connection.close()

    key_users = list(dict(users))  # タプルのリストであるusersを 辞書化→リスト化 でキー値が得られる。
    # http://ututel.blog121.fc2.com/blog-entry-45.html

    num_upd_indvisual = int(input('\n 更新する人を選んでください。> '))
    name_upd = key_users[num_upd_indvisual - 1]
    upd_weight = int(input(' 更新する体重を入力してください > '))

    connection = sqlite3.connect('weight_manage.db')
    cursor = connection.cursor()
    sql = f"UPDATE users SET weight ='{upd_weight}' WHERE name = '{name_upd}' "
    cursor.execute(sql)
    connection.commit()
    connection.close()

    print(f'\n {name_upd}を更新しました。\n')
