class BaseCoffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_description(self):
        return f"{self.name} costs ${self.price}"   
    
class americano(BaseCoffee):
    def __init__(self, price):
        super().__init__("Americano", price)
        print("Americano created")


class coffeeshop:
    coffee_cls = BaseCoffee

    def __init__(self):
        self.coffee = self.coffee_cls("Regular")

    def serve(self):
        print(f"Serving {self.coffee.get_description()}")
        self.coffee.prepare()
    
class CustomCoffeeShop(coffeeshop):
    coffee_cls = americano    

shop = coffeeshop()
shop.serve()
custom_shop = CustomCoffeeShop()
custom_shop.serve()    
