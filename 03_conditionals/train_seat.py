seat_type = input("Enter seat type (sleeper/AC/general/luxury)").lower()

match seat_type:
    case "sleeper":
        print("Slepper - No AC, beds available")
    case "ac":
        print("AC - Air conditioned, beds available")       
    case "general":
        print("General - No AC, no beds, only seats available")
    case "luxury":
        print("Luxury - Air conditioned, beds available, meals included")       
    case _:
        print("Invalid seat type")        
