def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai")
        if flavor == "unknown":
            raise ValueError("We don't know that flavor")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"{flavor} chai is ready!")
    finally:
        print("Thank you for visiting our chai shop!")

serve_chai("masala")
serve_chai("unknown")                