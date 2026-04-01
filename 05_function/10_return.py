def make_chai():
    #return "Chai is ready!"
    print("Chai is ready!")

return_value = make_chai()

#print(make_chai())

def ideal_chaiwala():
    pass

print(ideal_chaiwala())

def sold_cups():
    return 120

total = sold_cups()
print(total)

def chai_status(cups_left):
    if cups_left > 0:
        return "Chai is available!"
    else:
        return "Chai is sold out!"
    
print(chai_status(10))
print(chai_status(0))  


def chai_report():
    return 100, 20 #sold, remaining

sold, remaining = chai_report()
print(f"Sold: {sold}, Remaining: {remaining}")