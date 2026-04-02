daily_sales = [100, 150, 200, 250, 300]

total_cups = sum(sale for sale in daily_sales if sale > 100)

print(total_cups)  