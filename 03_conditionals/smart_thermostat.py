device_status = "active"
temperature = 40

if device_status == "active":
    if temperature > 30:
        print("It's too hot! Turning on the AC.")
    else:
        print("Temperature is comfortable. No action needed.")
        