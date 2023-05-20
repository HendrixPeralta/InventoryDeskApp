import sqlite3


def create_db():
    print("im here !!!! ####")
    conn = sqlite3.connect('InventoryApp_DB.db')
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS Tracks')
    cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

    cur.close()
    conn.close()


def add_track():
    conn = sqlite3.connect('InventoryApp_DB.db')
    cur = conn.cursor()

    cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
                ('Prueba 4', 12))
    cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
                ('prueba 3 ', 15))
    conn.commit()

    print('Tracks:')
    cur.execute('SELECT title, plays FROM Tracks')
    for row in cur:
        print(row)

    #   cur.execute('DELETE FROM Tracks WHERE plays < 100')
    conn.commit()

    cur.close()
    conn.close()


#add_track()
