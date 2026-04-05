class CoffeeOrder:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size


    def summary(self):
        return f"You ordered a {self.size}ml {self.type}."

order = CoffeeOrder("Latte", 250)
print(order.summary())

order_two = CoffeeOrder("Espresso", 100)
print(order_two.summary())