import sqlite3
import datetime


def create_db():
    print("im here !!!! ####")
    conn = sqlite3.connect('InventoryApp_DB.db')
    cur = conn.cursor()

    # Drops all tables
    # -------------------------------------------

    # Get the list of table names excluding 'sqlite_sequence'
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name != 'sqlite_sequence';")
    table_names = cur.fetchall()

    # Iterate over the table names and drop each table
    for table in table_names:
        cur.execute(f"DROP TABLE {table[0]};")

    # -------------------------------------------

    # Creates Main table ITEMS
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

    # Creates Groups 1 table
    try:
        cur.execute('''CREATE TABLE group1 (
                                            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                                            name TEXT, 
                                            description Text)''')
    except sqlite3.Error as e:
        print("An error occurred:", e)

    # Creates Groups 2 Table
    try:
        cur.execute('''CREATE TABLE group2 (
                                            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                                            name TEXT, 
                                            description Text)''')
    except sqlite3.Error as e:
        print("An error occurred:", e)

    # Creates Location table
    try:
        cur.execute('''CREATE TABLE location (
                                            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                                            name TEXT, 
                                            description Text)''')
    except sqlite3.Error as e:
        print("An error occurred:", e)

    # Creates Brands table
    try:
        cur.execute('''CREATE TABLE brand (
                                            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                                            name TEXT)''')
    except sqlite3.Error as e:
        print("An error occurred:", e)

    # Creates Seller table
    try:
        cur.execute('''CREATE TABLE seller (
                                            id  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                                            name TEXT)''')
    except sqlite3.Error as e:
        print("An error occurred:", e)

    # Creates added table
    try:
        cur.execute('''CREATE TABLE add_log (
                                            id  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                                            item_id Integer,
                                            old_quantity Integer,
                                            added_quantity Integer,
                                            new_quantity Integer,
                                            year Integer,
                                            month Integer,
                                            day Integer)''')
    except sqlite3.Error as e:
        print("An error occurred:", e)

    # Creates subtracted table
    try:
        cur.execute('''CREATE TABLE subtract_log (
                                            id  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                                            item_id Integer,
                                            old_quantity Integer,
                                            subtracted_quantity Integer,
                                            new_quantity Integer,
                                            year Integer,
                                            month Integer,
                                            day Integer)''')
    except sqlite3.Error as e:
        print("An error occurred:", e)

    cur.close()
    conn.close()


# Deletes all the items from the tables
def delete_all_items():
    conn = sqlite3.connect('InventoryApp_DB.db')
    cur = conn.cursor()

    cur.execute('DELETE FROM Items')
    cur.execute('DELETE FROM group1')
    cur.execute('DELETE FROM group2')
    cur.execute('DELETE FROM seller')
    cur.execute('DELETE FROM brand')
    cur.execute('DELETE FROM location')
    cur.execute('DELETE FROM add_log')
    cur.execute('DELETE FROM subtract_log')

    conn.commit()

    print('All items deleted.')

    cur.close()
    conn.close()


# ----------------------------------------------------------------------------------


def add_item(item):
    item_id = check_item(item)

    # Check of Group 1 exist if it does retrieve the row id

    if item_id is None:

        item.group = check_group1(item)
        item.location = check_location(item)
        item.brand = check_brand(item)
        item.seller = check_seller(item)

        conn = sqlite3.connect('InventoryApp_DB.db')
        cur = conn.cursor()

        cur.execute('''INSERT INTO Items (name, description, group1_id, model, brand_id, external_code, 
                        quantity, location_id,  seller_id, group2_id, descr2, maximum, minimum, Importance,
                        photo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (item.name, item.description, item.group, item.model, item.brand, item.ext_code,
                     item.quantity, item.location, item.seller, item.group2, item.des2, item.max,
                     item.min, item.importance, item.photo))

        conn.commit()
        cur.close()
        conn.close()

        item_id = check_item(item)
        add_log(item_id, 0, item.quantity, item.quantity)

    else:
        print("item check* This item already exist")


def delete_item(item):
    if item is not None:
        conn = sqlite3.connect('InventoryApp_DB.db')
        cur = conn.cursor()

        cur.execute('''Delete FROM Items WHERE id = ?''', (item[0],))
        print("Item deleted successfully")

        conn.commit()
        cur.close()
        conn.close()

    else:
        print("Item not Found")


def delete_table_content(table):
    print("im deleting content on ", table)

    if table == "all":
        delete_all_items()

    else:
        conn = sqlite3.connect('InventoryApp_DB.db')
        cur = conn.cursor()

        cur.execute(f'''Delete FROM {table}''')
        print(f"The contents in the {table} table were deleted successfully")

        conn.commit()
        cur.close()
        conn.close()


def add_quantity(item_id, add):
    conn = sqlite3.connect('InventoryApp_DB.db')
    cur = conn.cursor()

    cur.execute('''Select quantity from Items where id =?''', (item_id,))
    old_quantity = cur.fetchone()
    print("$" * 30, "old quantity!!!:", old_quantity)
    print("+" * 30, add)

    new_quantity = int(old_quantity[0]) + add

    print("$" * 30, "NEW quantity!!!:", new_quantity)
    cur.execute("UPDATE items SET quantity = ? WHERE id = ?", (new_quantity, item_id))
    conn.commit()
    cur.close()
    conn.close()

    add_log(item_id, old_quantity[0], add, new_quantity)


def subtract_quantity(item_id, subtract):
    conn = sqlite3.connect('InventoryApp_DB.db')
    cur = conn.cursor()

    cur.execute('''Select quantity from Items where id =?''', (item_id,))
    old_quantity = cur.fetchone()
    print("$" * 30, "old quantity!!!:", old_quantity)
    print("-" * 30, subtract)

    new_quantity = int(old_quantity[0]) - subtract

    if new_quantity >= 0:
        print("$" * 30, "NEW quantity!!!:", new_quantity)
        cur.execute("UPDATE items SET quantity = ? WHERE id = ?", (new_quantity, item_id))
        conn.commit()
        cur.close()
        conn.close()
        subtract_log(item_id, old_quantity[0], subtract, new_quantity)
        return

    else:
        option = input("There is no enough items to subtract this quantity. Do you still want to proceed? Y/N")
        if option.lower() == "n" or option.lower() == "no":
            print("Subtraction cancelled")
            return
        elif option.lower() == "y" or option.lower() == "yes":
            print("Item Quantity will be set to zero")
            new_quantity = 0
            print("$" * 30, "NEW quantity!!!:", new_quantity)
            cur.execute("UPDATE items SET quantity = ? WHERE id = ?", (new_quantity, item_id))
            conn.commit()
            cur.close()
            conn.close()
            subtract_log(item_id, old_quantity[0], old_quantity[0], new_quantity)
            return
        else:
            print("This is not a valid option")
            subtract_quantity(item_id, subtract)


# ===========================================================================
#  supporting FUNCTIONS

def look_up_id(code):
    conn = sqlite3.connect('InventoryApp_DB.db')
    cur = conn.cursor()

    code_int = None
    if isinstance(code, str) and code.isdigit():
        code_int = int(code)

    cur.execute('''Select i.id, i.name, l.name as location, external_code, model, quantity
         FROM Items as i 
         LEFT JOIN location AS l
         ON location_id = l.name 
        
        WHERE i.id = ?''', (code_int,))
    rows = cur.fetchone()

    cur.close()
    conn.close()

    return rows[0]


def filter_by(variable, table, look):
    conn = sqlite3.connect("InventoryApp_DB.db")
    cur = conn.cursor()

    query = f'''SELECT Items.name, description, location_id, quantity, t.name
            FROM Items 
            LEFT JOIN {table}  as t
            ON {table}_id = t.id  
            WHERE t.{variable} LIKE ?'''
    cur.execute(query, ("%" + look + "%",))
    rows = cur.fetchall()

    cur.close()
    conn.close()

    for row in rows:
        print(row)

    return rows


def check_item(item):
    conn = sqlite3.connect('InventoryApp_DB.db')
    cur = conn.cursor()

    cur.execute('''Select * From Items where external_code = ?''', (item.ext_code,))
    row = cur.fetchone()

    if row:
        print("whe found the Items: ", (item.name,))
        cur.close()
        conn.close()
        return row[0]

    else:
        print("the ITEM doesnt exist")
        return None


def subtract_log(item_id, old_quantity, subtracted_quantity, new_quantity):
    conn = sqlite3.connect('InventoryApp_DB.db')
    cur = conn.cursor()

    current_date = datetime.date.today()
    year_value = current_date.year
    month_value = current_date.month
    day_value = current_date.day

    print("*" * 30, "ID!!!!!")
    print(item_id)
    cur.execute('''INSERT INTO subtract_log (item_id, old_quantity, subtracted_quantity, new_quantity, year, month, day) 
                    VALUES (?, ?, ?, ?, ?,?,?)''',
                (item_id, old_quantity, subtracted_quantity, new_quantity, year_value, month_value, day_value))
    conn.commit()

    cur.close()
    conn.close()


def add_log(item_id, old_quantity, added_quantity, new_quantity):
    conn = sqlite3.connect('InventoryApp_DB.db')
    cur = conn.cursor()

    current_date = datetime.date.today()
    year_value = current_date.year
    month_value = current_date.month
    day_value = current_date.day

    print("*" * 30, "ID!!!!!")
    print(item_id)
    cur.execute('''INSERT INTO add_log (item_id, old_quantity, added_quantity, new_quantity, year, month, day) 
                VALUES (?, ?, ?, ?, ?, ?, ?)''',
                (item_id, old_quantity, added_quantity, new_quantity, year_value, month_value, day_value))
    conn.commit()

    cur.close()
    conn.close()


# Check of Group 1 exist if it does retrieve the row id if not insert it in the table
# Receives an item object
def check_group1(item):
    conn = sqlite3.connect('InventoryApp_DB.db')
    cur = conn.cursor()

    cur.execute('''Select * From group1 where name = ?''', (item.group,))
    row = cur.fetchone()

    if row:
        print("whe found the group: ", (item.group,))
        cur.close()
        conn.close()
        return row[0]

    else:
        print("the group doesnt exist")
        cur.execute('''Insert into group1 (name) Values (?)''', (item.group,))
        conn.commit()

        cur.execute('''Select * From group1 where name =?''', (item.group,))
        row = cur.fetchone()
        print("a new item was created ", item.group, row[0])
        cur.close()
        conn.close()
        return row[0]


# Check of Group 2 exist if it does retrieve the row id if not insert it in the table
# Receives an item object
def check_group2(item):
    conn = sqlite3.connect('InventoryApp_DB.db')
    cur = conn.cursor()

    cur.execute('''Select * From group2 where name = ?''', (item.group2,))
    row = cur.fetchone()

    if row:
        print("whe found the group2: ", (item.group,))
        cur.close()
        conn.close()
        return row[0]

    else:
        print("the group2 doesnt exist")
        cur.execute('''Insert into group2 (name) Values (?)''', (item.group,))
        conn.commit()

        cur.execute('''Select * From group2 where name =?''', (item.group,))
        row = cur.fetchone()
        print("a new item was created ", item.group2, row[0])
        cur.close()
        conn.close()
        return row[0]


# Check of LOCATION exist if it does retrieve the row id if not insert it in the table
# Receives an item object
def check_location(item):
    conn = sqlite3.connect('InventoryApp_DB.db')
    cur = conn.cursor()

    cur.execute('''Select * From location where name = ?''', (item.location,))
    row = cur.fetchone()

    if row:
        print("whe found the location: ", (item.location,))
        cur.close()
        conn.close()
        return row[0]

    else:
        print("the location doesnt exist")
        cur.execute('''Insert into location (name) Values (?)''', (item.location,))
        conn.commit()

        cur.execute('''Select * From location where name =?''', (item.location,))
        row = cur.fetchone()
        print("a new item was created ", item.location, row[0])
        cur.close()
        conn.close()
        return row[0]


# Check of BRAND exist if it does retrieve the row id if not insert it in the table
# Receives an item object
def check_brand(item):
    conn = sqlite3.connect('InventoryApp_DB.db')
    cur = conn.cursor()

    cur.execute('''Select * From brand where name = ?''', (item.brand,))
    row = cur.fetchone()

    if row:
        print("whe found the brand: ", (item.brand,))
        cur.close()
        conn.close()
        return row[0]

    else:
        print("the brand doesnt exist")
        cur.execute('''Insert into brand (name) Values (?)''', (item.brand,))
        conn.commit()

        cur.execute('''Select * From brand where name =?''', (item.brand,))
        row = cur.fetchone()
        print("a new brand was created ", item.brand, row[0])
        cur.close()
        conn.close()
        return row[0]


# Check of Seller exist if it does retrieve the row id if not insert it in the table
# Receives an item object
def check_seller(item):
    conn = sqlite3.connect('InventoryApp_DB.db')
    cur = conn.cursor()

    cur.execute('''Select * From seller where name = ?''', (item.seller,))
    row = cur.fetchone()

    if row:
        print("whe found the seller: ", (item.seller,))
        cur.close()
        conn.close()
        return row[0]

    else:
        print("the seller doesnt exist")
        cur.execute('''Insert into seller (name) Values (?)''', (item.seller,))
        conn.commit()

        cur.execute('''Select * From seller where name =?''', (item.seller,))
        row = cur.fetchone()
        print("a new seller was created ", item.seller, row[0])
        cur.close()
        conn.close()
        return row[0]
