def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"total cost is {cost}")
    except KeyError:
        print(f"Sorry, we don't have {item} on the menu.")
    except TypeError:
        print("Quantity must be a number.")

process_order("ginger", 2)
process_order("elaichi", 2)
process_order("masala", "two")                