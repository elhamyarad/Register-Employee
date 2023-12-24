import sqlite3


def loginFunction(username, password):
    connectionString = 'DB/pyadv.db'
    commandText = 'SELECT UserName, Password, FirstName, LastName, isAdmin' \
                  ' FROM Users WHERE UserName = ? AND Password = ?'
    params = (username, password)
    with sqlite3.Connection(connectionString) as connection:
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        rows = cursor.fetchall()

    if len(rows) > 0:
        return rows[0]
    else:
        return None
