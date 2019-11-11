import sqlite3


def delete_all():
    connection = sqlite3.connect('weight_manage.db')
    cursor = connection.cursor()
    sql = f"DELETE FROM users"
    cursor.execute(sql).fetchall()
    connection.commit()
    connection.close()
