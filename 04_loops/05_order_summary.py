names = ["harsh", "omkar", "ritesh", "rishi"]
bills = [100, 200, 300, 400]

for name, amount in zip(names, bills):
    print(f"{name} has to pay {amount}")