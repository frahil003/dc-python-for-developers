def calculate_discount(price, discount_percent=15, round_result=True):
    # Add a single-line docstring
    """Calculate the discounted price of a product."""
    
    discounted_price = price - (price * (discount_percent / 100))
    if round_result == True:
        return round(discounted_price, 2)
    else:
        return discounted_price

# Access the docstring
print(calculate_discount.__doc__)