masala_spices = ("cumin", "coriander", "turmeric", "red chili powder")

(spice1, spice2, spice3, spice4) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}, and {spice4}")

ginger_ratio, cadramom_ratio, cloves_ratio, cinnamon_ratio = (0.2, 0.3, 0.1, 0.4)
print(f"Ginger: {ginger_ratio}, Cardamom: {cadramom_ratio}, Cloves: {cloves_ratio}, Cinnamon: {cinnamon_ratio}")
ginger_ratio, cardamom_ratio, cloves_ratio, cinnamon_ratio = cadramom_ratio, ginger_ratio, cloves_ratio, cinnamon_ratio
print(f"Ratio is G :{ginger_ratio}, C :{cardamom_ratio}, CL :{cloves_ratio}, CI :{cinnamon_ratio}")

# membership testing

print(f"Is cumin in the masala spices? {'cumin' in masala_spices}")