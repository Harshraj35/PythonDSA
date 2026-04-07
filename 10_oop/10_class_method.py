class coffeeOrder:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    @classmethod
    def from_dict(cls, order_dict):
        return cls(order_dict["name"], order_dict["size"])
    
    @classmethod
    def from_string(cls, order_string):
        name, size = order_string.split("-")
        return cls(name.strip(), size.strip())

class coffeeUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]    

order1 = coffeeOrder("Latte", "Medium")
print(order1.name, order1.size)

order2 = coffeeOrder.from_dict({"name": "Espresso", "size": "Small"})
print(order2.name, order2.size)

order3 = coffeeOrder.from_string("Cappuccino-Small")
print(order3.name, order3.size)


print(coffeeOrder.__dict__)
print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)