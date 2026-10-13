
def calculate_total_price(quantity, price_per_car):
    if quantity <= 0:
        raise ValueError("Quantity must be positive")

    if price_per_car < 0:
        raise ValueError("Price cannot be negative")

    return round(quantity * price_per_car, 2)


if __name__ == "__main__":
    print(calculate_total_price(2, 500000))