def add_vat(price, vat_rate):
    """Calculate the price including VAT."""
    return price * (100 + vat_rate)/100


orders = [100, 200, 300]

for price in orders:
    final_amount = add_vat(price, 20)
    print(f"Final amount for order {price} is {final_amount}")