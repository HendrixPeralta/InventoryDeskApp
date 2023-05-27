import sqlite3
import DB
import random


class item:
    def __init__(self, name, description, group, model, brand, external_code, quantity, location, seller,
                 group2=None, des2=None, minimum=None, maximum=None, importance=None, photo=None):
        self.name = name
        self.description = description
        self.group = group
        self.model = model
        self.brand = brand
        self.ext_code = external_code
        self.quantity = quantity
        self.location = location
        self.group2 = group2
        self.des2 = des2
        self.min = minimum
        self.max = maximum
        self.importance = importance
        self.seller = seller
        self.photo = photo

    def __str__(self):
        return f"Item: {self.name}\n" \
               f"Description: {self.description}\n" \
               f"Group: {self.group}\n" \
               f"Model: {self.model}\n" \
               f"Brand: {self.brand}\n" \
               f"External Code: {self.ext_code}\n" \
               f"Quantity: {self.quantity}\n" \
               f"Location: {self.location}\n" \
               f"Seller: {self.seller}\n" \
               f"Group2: {self.group2}\n" \
               f"Description2: {self.des2}\n" \
               f"Minimum: {self.min}\n" \
               f"Maximum: {self.max}\n" \
               f"Importance: {self.importance}\n" \
               f"Photo: {self.photo}"


DB.delete_all_items()
DB.create_db()


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
    DB.subtract_quantity(new_items[random.randint(0, len(new_items)-1)], random.randint(50, 100))


