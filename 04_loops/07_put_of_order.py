flavours = ["vanilla", "out of stock", "strawberry"]

for flavour in flavours:
    if flavour == "out of stock":
        continue
    if flavour == "strawberry":
        print(f"{flavour} item found")
        break   
    print(f"{flavour} item found")


print("out side of loop")    