def fuel_price(litres, price_per_liter):
    return round(litres * max(price_per_liter-.25, price_per_liter-.05*(litres//2)),2)