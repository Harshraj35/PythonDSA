users = [
    {"id": 1, "total": 100, "coupon": "p20"},
    {"id": 2, "total": 200, "coupon": "p30"},
    {"id": 3, "total": 300, "coupon": "p40"}
]

discounts = {
    "p20": (0.2, 0),
    "p30": (0.3, 0),
    "p40": (0.4, 0)
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fixed
    print(f"{user["id"]} paid {user["total"]} and got discount for next visit of rupees {discount}")