essential_spices = ['cumin', 'coriander', 'turmeric', 'paprika', 'garam masala']
options_spices = ['cumin', 'coriander', 'turmeric', 'paprika', 'garam masala', 'cardamom', 'cloves']

all_spices = set(essential_spices) | set(options_spices)
print(f"All spices: {all_spices}")

common_spices = set(essential_spices) & set(options_spices)
print(f"Common spices: {common_spices}")

only_in_essential = set(essential_spices) - set(options_spices)
print(f"Spices only in essential: {only_in_essential}")

print(f"Only in essential spices? {'cumin' in only_in_essential}")
