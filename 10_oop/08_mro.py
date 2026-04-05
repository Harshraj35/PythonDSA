class A:
    label = "A: Base class"

class B:
    label = "B: Derived class"

class C:
    label = "C: HHerbal class"

class D(B, C):
    pass

cup = D()
print(cup.label)  # Output: "B: Derived class"
print(D.__mro__)