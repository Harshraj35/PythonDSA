tea_price_inr = {
    "green": 100,
    "black": 150,
    "oolong": 200,
}

tea_price_usd = {tea: price / 96 for tea, price in tea_price_inr.items()}