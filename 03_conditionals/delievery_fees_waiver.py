order_amount = int(input("Enter the order amount: "))

delivery_fees = 0 if order_amount > 500 else 50

print(f"Delivery fees: ${delivery_fees:.2f}")