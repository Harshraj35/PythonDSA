def chai_flavor(flavor='masala'):
    """Returns the flavor of chai."""
    chai="ginger"
    return flavor


print(chai_flavor.__doc__)
print(chai_flavor.__name__)

help(len)

def generate_bill(chai=0, samosa=0, idli=0):
    """Generates the bill for the given items."""
    total = chai*10 + samosa*20 + idli*15
    return total

print(generate_bill.__doc__)
print(generate_bill.__name__)