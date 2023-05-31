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