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
            external_code = f"Location {random.randint(1, 40)}"
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
    # Add your code here


def add_quantity():
    print("You selected option 3 - Add quantity")
    # Add your code here


def subtract_quantity():
    print("You selected option 4 - Subtract quantity")
    # Add your code here


def edit_item():
    print("You selected option 5 - Edit item")
    # Add your code here


def search_item():
    print("You selected option 6 - Search item")
    # Add your code here


def delete_logs():
    print("You selected option 98 - DELETE logs")
    # Add your code here


def delete_database():
    print("You selected option 99 - Delete database")
    # Add your code here


def trash():
    new_items = []
    for i in range(5):
        name = f"Item {i + 1}"
        description = f"Description {i + 1}"
        group = f"Group {random.randint(1, 10)}"
        model = f"Model {i + 1}"
        brand = f"Brand {i + 1}"
        external_code = f"Location {random.randint(1, 40)}"
        quantity = random.randint(50, 100)
        location = f"Location {random.randint(1, 10)}"
        seller = f"Seller {random.randint(1, 10)}"
        group2 = f"Group2 {i + 1}"
        des2 = f"Description2 {i + 1}"
        minimum = random.randint(1, 10)
        maximum = minimum * 10
        importance = f"Importance {i + 1}"
        photo = f"Photo {i + 1}"

        items = item(name=name, description=description, group=group, model=model, brand=brand,
                     external_code=external_code, quantity=quantity, location=location, seller=seller,
                     group2=group2, des2=des2, minimum=minimum, maximum=maximum,
                     importance=importance, photo=photo)
        new_items.append(items)

    # adding each item to the db
    for item in new_items:
        DB.add_item(item)

    for item in new_items:
        DB.subtract_quantity(new_items[random.randint(0, len(new_items) - 1)], random.randint(10, 50))
