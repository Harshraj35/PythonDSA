chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42


edit_chai(chai)
print(chai)

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Full Cream", "2 spoons")
make_chai(tea="Green", sugar="medium", milk="Skimmed") #keyword arguments    


def special_chai(*ingredients, **properties):
    print("Ingredients:", ingredients)
    print("Properties:", properties)

special_chai("Cardamom", "Cinnamon", flavor="Spicy", color="Brown")  

def chai_orders(order=None):
    if order is None:
        order = []
    print(order)    

chai_orders()  # Output: ['Masala']
chai_orders()  # Output: ['Masala', 'Masala'] - This is because