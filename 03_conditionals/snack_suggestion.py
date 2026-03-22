# A local cafe wants a program that suggests a snack. If a customer asks for cookies or samosa, it confirms the order. Otherwise, it says its not available.

snack = input("Enter your preferred snack: ").lower()

if snack == "cookies" or snack == "samosa":
    print("Order confirmed!")
else:
    print("Sorry, that's not available.")