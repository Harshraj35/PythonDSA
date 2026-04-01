def pure_chai(cups):
    return cups *10

total_chai = 0

def impure_chai(cups):
    global total_chai
    total_chai += cups * 10
    return total_chai


def pour_chai(n):
    if n == 0:
        return "All chai poured!"
    return pour_chai(n-1)

print(pour_chai(5))




chai_types = ["Masala Chai", "Ginger Chai", "Cardamom Chai"]


strong_chai = list(filter(lambda chai: "Strong" in chai, chai_types))

print(strong_chai)