# create a customer class
class Customer:
    def __init__(self, *args, tier = ('free', 0)):
        self.name = ' '.join(args)
        self.cost = tier[1]
        self.tier = tier[0]
    @classmethod
    def premium(cls, *args):
        return cls(*args, tier = ('premium', 10))
    def can_access(self, content):
        return content['tier'] == 'free' or content['tier'] == self.tier
    def bill_for(self, months):
        return self.cost * int(months)
        
marco = Customer.premium('Marco', 'Polo')
marco.tier

marco = Customer('Marco', 'Polo')  # Defaults to the free tier
print(marco.name)  # Marco Polo
print(marco.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
print(marco.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # False

victoria = Customer.premium("Alexandrina", "Victoria")  # Build a customer around the ('premium', 10$/mo) streaming plan.
print(victoria.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
print(victoria.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # True
print(victoria.bill_for(5))  # => 50 (5 months at 10$/mo)
print(victoria.name)  # Alexandrina Victoria
    
    
# magic methods
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __add__(self, point2):
        return Point(self.x + point2.x, self.y + point2.y)
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
point1 = Point(1, 3)
point2 = Point(-3, 6)
point3 = point1 + point2 

print(point3)
