class Tealeaf:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value


leaf = Tealeaf("Green Tea", 10)
print(leaf.name, leaf.price)
leaf.price = 12
print(leaf.name, leaf.price)        