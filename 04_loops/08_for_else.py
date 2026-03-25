staff = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

for name, age in staff:
    if age < 30:
        print(f"{name} is under 30.")
        break
else:
    print(f"No one is under 30")    