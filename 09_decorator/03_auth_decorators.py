from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied: Admins only.")
            return
        return func(user_role)
    return wrapper

@require_admin
def acess_tea_inventory(user_role):
    print("Accessing tea inventory...")

acess_tea_inventory("user") 
acess_tea_inventory("admin")   