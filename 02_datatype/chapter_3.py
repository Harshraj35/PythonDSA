# Integer

black_tea_grams = 100
ginger_grams = 20

total_grams = black_tea_grams + ginger_grams
print(f"Total grams of tea is {total_grams}")

remaing_tea = black_tea_grams - ginger_grams
print(f"Total grams of remaing tea is {remaing_tea}")

milk_liters = 7
serving = 4
milk_per_serving = milk_liters / serving
print(f"Milk per serving is {milk_per_serving}")

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"Tea bags per pot is {bags_per_pot}")

total_cadamom_pods = 10
pods_per_tea = 3
leftover_pods = total_cadamom_pods % pods_per_tea
print(f"Leftover C pods {leftover_pods}")

base_flavor_strength = 2
scale_factor = 3
powerful_flavor = base_flavor_strength ** scale_factor
print(f"scaled flavour strength is {powerful_flavor}")
#2**3 = 2*2*2 = 8

total_tea_leaves_harvested = 1_000_000_000
print(f"tea leaves: {total_tea_leaves_harvested}")
