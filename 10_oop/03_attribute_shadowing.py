class coffee:
    temperature = "hot"
    strength = "strong"


half_coffee = coffee()
print(half_coffee.temperature)  # hot

half_coffee.temperature = "cold"
half_coffee.strength = "weak"
print("After changing:", half_coffee.temperature)  # cold
print("After changing strength:", half_coffee.strength)  # weak
print("Direct look at class attribute:", coffee.temperature)  # hot

del half_coffee.temperature
del half_coffee.strength
print(half_coffee.temperature)  # hot
print(half_coffee.strength)  # strong 