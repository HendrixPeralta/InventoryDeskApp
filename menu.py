import random
import objects
import DB


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
            brand = f"Brand {i + 1}"
            external_code = f"code {random.randint(1, 40)}"
            quantity = random.randint(50, 100)
            location = f"Location {random.randint(1, 10)}"
            seller = f"Seller {random.randint(1, 10)}"
            group2 = f"Group2 {i + 1}"
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
        DB.add_item(item)


def delete_item():
    print("You selected option 2 - Delete an item")
    code = input("Add the code of the item to delete")
    item_id = DB.look_up_id(code)
    DB.delete_item(item_id)


def add_quantity():
    print("You selected option 3 - Add quantity")
    code = input("Add the code of the item you want to add the quantity")
    item_id = DB.look_up_id(code)
    if item_id is None:
        return
    new_quantity = input("Insert the amount to add")
    DB.add_quantity(item_id, int(new_quantity))


def subtract_quantity():
    print("You selected option 4 - Subtract quantity")
    code = input("Add the code of the item you want to add the quantity")
    item_id = DB.look_up_id(code)
    if item_id is None:
        return
    new_quantity = input("Insert the amount to add")
    DB.subtract_quantity(item_id, int(new_quantity))


def edit_item():
    print("You selected option 5 - Edit item")
    # Add your code here


def search_item():
    print("You selected option 6 - Search item")
    code = str(input("Add the code of the item to search"))
    DB.look_up_id(code)


def delete_log():
    print("You selected option 98 - DELETE logs")
    option = {
        "1": "Items",
        "2": "group1",
        "3": "group2",
        "4": "add_log",
        "5": "Subtract_log",
        "6": "seller",
        "7": "brand",
        "8": "location",
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
        """
    )
    button = input("Select the number of the table to delete")
    table = option.get(button)
    print("you selected ", table)
    DB.delete_log(table)


def delete_database():
    print("You selected option 99 - Delete database")
    # Add your code here
