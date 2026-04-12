class InvalidCoffeeError(Exception):
    pass

def bill(flavor, cups):
    menu = {"Espresso": 20, "Latte": 25, "Cappuccino": 30}
    try:
        if flavor not in menu:
            raise InvalidCoffeeError("Invalid coffee flavor")
        if not isinstance(cups, int) or cups <= 0:
            raise ValueError("Number of cups must be a positive integer")
        total = menu[flavor] * cups
        print(f"Your total bill for {cups} {flavor}(s) is: {total} units.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Thank you for your order!")

bill("Latte", 2)  # Valid order
bill("Mocha", 1)   # Invalid flavor
bill("Espresso", -1)  # Invalid number of cups
bill("Cappuccino", "two")  # Invalid number of cups        