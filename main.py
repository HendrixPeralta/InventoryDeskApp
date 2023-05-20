
import sqlite3
import DB


class item():
    def __init__(self, name, description, group, model, brand, external_code, quantity, location,
                 group2=None, descr2=None, minimum=None, maximum=None, importance=None, seller=None, photo=None):
        self.name = name
        self.description = description
        self.group = group
        self.model = model
        self.brand = brand
        self.ext_code = external_code
        self.quantity = quantity
        self.location = location
        self.group2 = group2
        self.des2 = descr2
        self.min = minimum
        self.max = maximum
        self.importance = importance
        self.seller = seller
        self.photo = photo

    def add_quantity(self, quantity):
        self.quantity = self.quantity + quantity

    def substract_quantity(self, quantity):
        self.quantity = self.quantity - quantity
        if self.quantity < 0:
            self.quantity = 0


DB.create_db()


a = item("n", "d", "g", "m", "b", "c", 1, 2)
print(a.quantity)
# print(a.description)
# print(a.model)
# print(a.brand)
# print(a.quantity)
# print(a.location)

b = item("n", "d", "g", "m", "b", "c", 3, 2)
print(b.quantity)
# print(a.description)
# print(a.model)
# print(a.brand)
# print(a.quantity)
# print(a.location)

a.add_quantity(4)
print(a.quantity)

a.substract_quantity(7)
print(a.quantity)
