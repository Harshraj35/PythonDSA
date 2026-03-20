is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling #upcasting
print(f"Total actions is {total_actions}")

milk_present = 0 # no milk
print(f"Is milk present? {bool(milk_present)}")

water_hot = True
tea_addad = False

can_server = water_hot and tea_addad
print(f"Can we serve tea? {can_server}")