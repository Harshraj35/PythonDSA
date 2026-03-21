chai_order = dict(type='chai', price=10, quantity=2)
print(f"Chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe: {chai_recipe}")
del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")

print(f"Is 'liquid' in recipe? {'liquid' in chai_recipe}")

chai_order = {"type": "chai", "price": 50, "quantity": 5}

#

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")


extra_spices = {"cardamom": 5, "cloves": 3}
chai_recipe.update(extra_spices)

print(f"Updated chai recipe: {chai_recipe}")

customer_note  = chai_order.get("note", "NO note")
print(f"customer_note is: {customer_note}")