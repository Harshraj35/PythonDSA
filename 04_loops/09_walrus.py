#value = 14
#remainder = value % 5

#if remainder:
#    print(f"Not divisible, remainder is {remainder}")


value = 14

if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")

available_size = ["samll", "medium", "large"] 

if (requested_size := input("Enter your chai cup size:")) in available_size:
    print(f"Serving {requested_size} chai")
else:
    print(f"Size is unavailable - {requested_size}")  




flavour = ["masala", "ginger", "cardamom", "tulsi", "lemon"]

print("available flavour: ", flavour)

while (flavour := input("Choose your flavour: ")) not in flavour:
    print(f"sorry {flavour} is not available")

print(f"You choose {flavour} chai")