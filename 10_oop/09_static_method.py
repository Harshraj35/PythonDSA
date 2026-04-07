class coffeeUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    

raw = "milk, sugar, coffee powder"

cleaned = coffeeUtils.clean_ingredients(raw)
print(cleaned)