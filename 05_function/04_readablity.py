def calculate_bill(cups, price_per_cup):
    total = cups * price_per_cup
    return total

my_bill =calculate_bill(3, 2.5)
print(my_bill)

print("order for table 2: ", calculate_bill(4, 3.0))