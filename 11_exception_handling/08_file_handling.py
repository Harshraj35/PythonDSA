#file = open("order.txt", "w")
#try:
#    file.write("Order details: 2 Lattes\n")
#except Exception as e:
#    print(f"Error writing to file: {e}")
#finally:
#        file.close()


with open("order.txt", "w") as file:
    try:
        file.write("Order details: 2 Lattes\n")
    except Exception as e:
        print(f"Error writing to file: {e}")