import sqlite3


def create_db():
    print("im here !!!! ####")
    conn = sqlite3.connect('InventoryApp_DB.db')
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS Items')
    try:
        cur.execute('''CREATE TABLE Items (
                                            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                                            name TEXT, 
                                            description Text, 
                                            group1_id Integer,
                                            model Text, 
                                            brand_id Integer, 
                                            external_code Text,
                                            quantity Integer, 
                                            location_id Integer, 
                                            group2_id Integer, 
                                            descr2 Text,
                                            minimum Integer, 
                                            maximum Integer, 
                                            Importance Integer, 
                                            seller_id Integer, 
                                            photo Text)''')
    except sqlite3.Error as e:
        print("An error occurred:", e)

    try:
        cur.execute('''CREATE TABLE group1 (
                                            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                                            name TEXT, 
                                            description Text)''')
    except sqlite3.Error as e:
        print("An error occurred:", e)

    try:
        cur.execute('''CREATE TABLE group2 (
                                            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                                            name TEXT, 
                                            description Text)''')
    except sqlite3.Error as e:
        print("An error occurred:", e)

    try:
        cur.execute('''CREATE TABLE location (
                                            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                                            name TEXT, 
                                            description Text)''')
    except sqlite3.Error as e:
        print("An error occurred:", e)

    try:
        cur.execute('''CREATE TABLE brand (
                                            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                                            name TEXT)''')
    except sqlite3.Error as e:
        print("An error occurred:", e)


    try:
        cur.execute('''CREATE TABLE seller (
                                            id  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                                            name TEXT)''')
    except sqlite3.Error as e:
        print("An error occurred:", e)

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
