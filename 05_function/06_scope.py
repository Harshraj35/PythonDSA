def serve_chai():
    chai_type = "Masala Chai"
    print(f"Inside function {chai_type}")

chai_type = "Green Tea"
serve_chai()
print(f"Outside function {chai_type}")    


def chai_counter():
    chai_order = "Green Tea" #Enclosing scope

    def print_order():
        print("Inner:", chai_order)
    print_order()
    print("Outer:", chai_order)

chai_order = "TUlsi"  #Global scope
print("Outer:", chai_order)       