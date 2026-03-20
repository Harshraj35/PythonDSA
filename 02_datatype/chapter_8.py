ingredients = ["Water", "Ginger", "Cardamom", "Cloves", "Cinnamon"]
ingredients.append("Tea Leaves")
print(f"Ingredients for making tea: {ingredients}")
ingredients.remove("Water")
print(f"Ingredients for making tea: {ingredients}")

spice_options = ["cumin", "coriander", "turmeric", "red chili powder"]
chai_ingredients = ["Water", "Ginger", "Cardamom", "Cloves", "Cinnamon", "Tea Leaves"]

chai_ingredients.extend(spice_options)
print(f"Ingredients for making chai: {chai_ingredients}")
chai_ingredients.insert(5, "Milk")
print(f"Ingredients for making chai: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f" {last_added}")
print(f" Ingredients for making chai: {chai_ingredients}")
chai_ingredients.reverse()
print(f"Ingredients for making chai: {chai_ingredients}")
chai_ingredients.sort()
print(f"Ingredients for making chai: {chai_ingredients}")

sugar_levels = [0.5, 1.0, 1.5, 2.0]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")

base_liquids = ["Water", "Milk", "Almond Milk", "Soy Milk"]
etra_liquids = ["Juice", "Soda", "Tea"]

full_liquid_mix = base_liquids + etra_liquids
print(f"Full liquid mix: {full_liquid_mix}")

strong_brew = ["Tea Leaves", "Coffee Grounds"]
print(f"Strong brew : {strong_brew}")