# Define classes for Users, Products and Reviews for the products,
# with the possibility to buy and sell them.

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.reviews = []
    def __str__(self):
        return f"{self.name}, id = {self.id}"
    def sell_product(self, name, description, price):
        return Product(name, description, price, seller = self.name,
                       available=True)
    def buy_product(self, product):
        product.available = False
    def write_review(self, review, product):
        new_review = Review(review, product.name, self.name)
        self.reviews.append(new_review)
        product.reviews.append(new_review)
        return new_review
    
class Product:
    def __init__(self, name, description, price, seller, available, reviews = []):
        self.name = name
        self.description = description
        self.price = price
        self.seller = seller
        self.reviews = reviews
        self.available = available
    def __str__(self):
        return f"{self.name}, at a price of {self.price} dollars, sold by {self.seller}"
    
class Review:
    def __init__(self, description, name, user):
        self.description = description
        self.name = name
        self.user = user
    def __str__(self):
        return f"{self.user} said: '{self.description}' about {self.name}"
        
brianna = User(1, 'Brianna')
mary = User(2, 'Mary')

keyboard = brianna.sell_product('Keyboard', 'A nice mechanical keyboard', 100)
print(keyboard.available)  # => True
mary.buy_product(keyboard)
print(keyboard.available)  # => False
review = mary.write_review('This is the best keyboard ever!', keyboard)
print(review in mary.reviews)  # => True
print(review in keyboard.reviews) 
