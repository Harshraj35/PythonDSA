class Coffee:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


class Latte(Coffee):
    def __init__(self, type_, strength, milk):
        super().__init__(type_, strength)
        self.milk = milk


class Cappuccino(Coffee):
    def __init__(self, type_, strength, foam):
        Coffee.__init__(self, type_, strength)
        self.foam = foam   


class Americano(Coffee):
    def __init__(self, type_, strength, water):
        super().__init__(type_, strength)
        self.water = water                     