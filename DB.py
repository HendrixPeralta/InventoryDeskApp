import sqlite3


def start_db():
    conn = sqlite3.connect('InventoryApp_DB')
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS Tracks')
    cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

    cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
                ('Thunderstruck', 20))
    cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
                ('My Way', 15))
    conn.commit()

    print('Tracks:')
    cur.execute('SELECT title, plays FROM Tracks')
    for row in cur:
        print(row)

    cur.execute('DELETE FROM Tracks WHERE plays < 100')
    conn.commit()

    cur.close()
    conn.close()
