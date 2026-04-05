class coffeecup:
    size = 250 #ml

    def describe(self):
        return f"This is a {self.size}ml coffeec up."
    

cup = coffeecup()
print(cup.describe())    
print(coffeecup.describe(cup))

cup_two = coffeecup()
cup_two.size = 500
print(coffeecup.describe(cup_two))