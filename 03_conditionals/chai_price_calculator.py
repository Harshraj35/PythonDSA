# A tea stall offers different prices for different cup sozes. Write a program that calculate the price based on size

size = input("Choose your cup size (small/medium/large): ").lower()  

if size == "small":
    price = 10
elif size == "medium":
    price = 15
elif size == "large":
    price = 20
else:
    print("Invalid cup size. Please choose from small, medium, or large.")
    price = 0

if price > 0:
    print(f"The price for a {size} cup of chai is ${price:.2f}.")