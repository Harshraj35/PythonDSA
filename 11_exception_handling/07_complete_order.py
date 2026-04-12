class InvalidCoffeeError(Exception):
    pass

def bill(flavor, cups):
    menu = {"Espresso": 20, "Latte": 25, "Cappuccino": 30}
    try:
        if flavor not in menu:
            raise InvalidCoffeeError("Invalid coffee flavor")
        if not isinstance(cups, int) or cups <= 0:
            raise ValueError("Number of cups must be a positive integer")
    except InvalidCoffeeError as e:
        print(f"Error: {e}")
        return 0
    except ValueError as e:
        print(f"Error: {e}")
        return 0
    return menu[flavor] * cups