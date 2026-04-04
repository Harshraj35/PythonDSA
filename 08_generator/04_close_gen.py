def local_coffee():
    yield "Espresso"
    yield "Americano"


def import_coffee():
    yield "Cappuccino"
    yield "Latte"


def full_menu():
    yield from local_coffee()
    yield from import_coffee()

for coffee in full_menu():
    print(coffee)    

def coffee_shop():
    try:
        while True:
            order = yield "waiting for coffee"
    except:
        print("closing shop")


shop = coffee_shop()
print(next(shop))
shop.close()   #cleanup     