import random
import objects
import DB


# TEST
def item_data_entry():
    new_items = []
    quantity_items = int(input("How many items you want to create: "))
    if quantity_items == 1:
        name = input("Name: ")
        description = input("Description: ")
        group = input("Group: ")
        model = input("Model: ")
        brand = input("Brand: ")
        external_code = input("External Code: ")
        quantity = input("Quantity: ")
        location = input("Location: ")
        group2 = input("Group 2: ")
        des2 = input("Description 2: ")
        minimum = input("Minimum: ")
        maximum = input("maximum: ")
        importance = input("Importance: ")
        seller = input("Seller: ")
        photo = input("Photo: ")

        item = objects.item(name=name, description=description, group=group, model=model, brand=brand,
                            external_code=external_code, quantity=quantity, location=location, seller=seller,
                            group2=group2, des2=des2, minimum=minimum, maximum=maximum,
                            importance=importance, photo=photo)

        new_items.append(item)

        print(new_items)

        return new_items

    elif quantity_items > 1:
        print("n:", quantity_items)
        print("range: ", range(quantity_items))
        for i in range(quantity_items):
            name = f"Item {i + 1}"
            description = f"Description {i + 1}"
            group = f"Group {random.randint(1, 10)}"
            model = f"Model {i + 1}"
            brand = f"Brand {random.randint(1, 10)}"
            external_code = f"code {random.randint(1, 40)}"
            quantity = random.randint(50, 100)
            location = f"Location {random.randint(1, 10)}"
            seller = f"Seller {random.randint(1, 10)}"
            group2 = f"Group2 {random.randint(1, 10)}"
            des2 = f"Description2 {i + 1}"
            minimum = random.randint(1, 10)
            maximum = minimum * 10
            importance = f"Importance {i + 1}"
            photo = f"Photo {i + 1}"

            items = objects.item(name=name, description=description, group=group, model=model, brand=brand,
                                 external_code=external_code, quantity=quantity, location=location, seller=seller,
                                 group2=group2, des2=des2, minimum=minimum, maximum=maximum,
                                 importance=importance, photo=photo)
            new_items.append(items)
            # adding each item to the d
            print("size of item", len(new_items))
        return new_items


def add_item():
    print("You selected option 1 - Add new item")
    new_items = item_data_entry()
    print("size of item 2", len(new_items))
    for item in new_items:
        DB.add_item(item[0])


def delete_item():
    print("delete_item()")
    # ------------------------

    print("You selected option 2 - Delete an item")
    item = look_up()
    if item is None:
        print("Action is not possible - Item NOT found")
        return
    DB.delete_item(item[0])


def add_quantity():
    print("add_quantity()")
    # ------------------------

    print("You selected option 3 - Add quantity")
    item = look_up()
    if item is None:
        print("Action is not possible - Item NOT found")
        return
    print("add_quantity()")
    print(item)
    new_quantity = input("Insert the amount to add")
    DB.add_quantity(item[0], int(new_quantity))


def subtract_quantity():
    print("subtract_quantity()")
    # ------------------------

    print("You selected option 4 - Subtract quantity")
    item = look_up()
    if item is None:
        print("Action is not possible - Item NOT found")
        return
    new_quantity = input("Insert the amount to subtract")
    DB.subtract_quantity(item[0], int(new_quantity))


def edit_item():
    print("edit_item()")
    # ------------------------
    print("You selected option 5 - Edit item")
    # Add your code here


def search_item():
    print("You selected option 6 - Search item")
    item = look_up()
    if item is None:
        print("Action is not possible - Item NOT found")

    return None


def delete_table_content():
    print("You selected option 98 - DELETE logs")
    table_list = {
        "1": "Items",
        "2": "group1",
        "3": "group2",
        "4": "add_log",
        "5": "Subtract_log",
        "6": "seller",
        "7": "brand",
        "8": "location",
        "0": "all"
    }
    print(
        """
        1 = Items
        2 = Group 1
        3 = Group 2
        4 = add logs
        5 = Subtract logs
        6 = Seller
        7 = Brand
        8 = Location
        -----------------
        0 = All
        """
    )
    button = input("Select the number of the table to delete")
    table = table_list.get(button)
    print("You selected ", table)
    DB.delete_table_content(table)


def look_up():
    options = {
        # '1': DB.look_up_extcode,
        # '2': DB.look_up_name,
        # '3': DB.look_up_description,
        # '0': None,
        '1': "external_code",
        '2': "name",
        '3': "description",
        '0': None,
    }

    button = None

    while button != '0':
        print(
            """
            1 = Look Up by External Code
            2 = look Up by name
            3 = Look Up by Description 
            0 = CANCEL
            """
        )
        button = input("Enter your choice: ")

        # Get the corresponding action based on user input
        look_up_method = options.get(button)
        if look_up_method:
            print("button selected: ", button)
            print(options[button])
            name = input(f"What is the {look_up_method} of the item you are looking for")
            items = DB.look_up(look_up_method, name)

            if items:

                i = 0
                print("1, Items found by the Look up name function:")
                print("| No  |     Name     |     External Code     |     Description     |     Location     |     Model     |     Quantity     |")
                for item in items:
                    print(
                        f"| {i + 1}  |     {item[1]}     |     {item[3]}     |     {item[6]}     |     {item[2]}     |     {item[4]}     |     {item[5]}     |")

                choice = int(input("input the item number of the desired item"))
                return items[choice - 1]

            else:
                print("Item not found")
                return None

            # return item

        elif button == '0':
            # Quit the program
            print("Quitting the program...")
            # Add any necessary cleanup or exit code here
        else:
            # Handle invalid input
            print("Invalid choice. Please enter a valid option.")

        print("Program exited.")


def delete_database():
    print("You selected option 99 - Delete database")
    # Add your code here


def filter_by():
    print("You selected option 7 - Filter_by")
    table_name = str(input("NAME OF THE TABLE"))
    list_distinct = DB.filter_by(table_name)

    i = 0
    for item in list_distinct:
        print("#", i, " Name:", item[0])
        i = i + 1
    i = 0
    selected = int(input("Select the # to filter"))
    look = list_distinct[selected]
    print(look[1])
    filter_result = DB.look_up_id(str(look[1]))

    for result in filter_result:
        print(result)

    return None
