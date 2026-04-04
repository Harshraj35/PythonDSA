class coffee:
    origin = "Ethiopia"

print(coffee.origin)

coffee.is_hot = True
print(coffee.is_hot)

#creating an instance of coffee

americano = coffee()
print(f"americano is from {americano.origin}")
print(f"americano is hot: {americano.is_hot}") 
americano.is_hot = False

print("Class: ", coffee.is_hot)
print(f"americano is hot: {americano.is_hot}")
americano.flavor = "bitter"
print(f"americano flavor: {americano.flavor}")