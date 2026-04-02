menu = [
    "masala chai",
    "Iced lemaon tea",
    "ginger tea",
    "green tea",
    "lemon tea",
]

iced_tea = [my_tea for my_tea in menu if "iced" in my_tea.lower()]

print(iced_tea)