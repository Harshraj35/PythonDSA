chai_menu = {"masala": 20, "ginger": 25}

try:
    print(chai_menu["elaichi"])
except KeyError:
    print("Key not found")

print("Hello chai code")    