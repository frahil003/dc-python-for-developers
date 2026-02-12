original_price = 899.99

# Define the function with default arguments
def calculate_discount(price, discount_percent=15, round_result=True):
    discounted_price = price - (price * (discount_percent / 100))
    
    if round_result == True:
        # Round the result to two decimal places
        return round(discounted_price, 2)
    else:
        return discounted_price

# Call the function with keyword arguments
final_price = calculate_discount(price=original_price, discount_percent=25, round_result=False)
print(final_price)