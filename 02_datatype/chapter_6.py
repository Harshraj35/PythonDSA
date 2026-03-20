chai_type = "chai"
customer_name = "John Doe"

print(f"Order for {customer_name}: {chai_type } please !")

chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[:8]}")
print(f"Last word: {chai_description[12:]}")
print(f"last word: {chai_description[::-2]}")

label_text = "Chai Special"
encoded_lable = label_text.encode("utf-8")
print(f"Encoded label: {encoded_lable}")
print(f"Non encoded label: {label_text}")
decoded_label = encoded_lable.decode("utf-8")
print(f"Decoded label: {decoded_label}")