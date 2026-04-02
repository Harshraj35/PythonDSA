favourite_chais = [
    "masala chai", "Iced lemaon tea", "ginger tea", "green tea", "lemon tea"
]


unique_chais = {chai for chai in favourite_chais if len(chai) > 8}
print(unique_chais)


recipes = {
    "Masala chai": ["ginger", "cardamom", "clove", "cinnamon"],
    "Iced lemaon tea": ["lemon", "sugar", "water"], 
    "Spicy chai": ["ginger", "cardamom", "clove", "cinnamon", "pepper"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)