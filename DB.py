import sqlite3


def create_db():
    print("im here !!!! ####")
    conn = sqlite3.connect('InventoryApp_DB.db')
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS Items')
    cur.execute('''CREATE TABLE Items (name TEXT, description Text, group1 Text,
                model Text, brand Integer, external_code Text,
                quantity Integer, location Integer, group2 Integer, descr2 Integer,
                min Integer, max Integer, Importance Integer, seller Integer, photo Text)''')

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

    cur.close()
    conn.close()


def add_items(name):
    conn = sqlite3.connect('InventoryApp_DB.db')
    cur = conn.cursor()

    cur.execute('DELETE FROM Tracks WHERE name = ?', name)
    conn.commit()

    cur.close()
    conn.close()

# add_track()
