file_size = 2500
extra_space = 0.15

# Define a lambda function
calculate_total = lambda x: x * (1 + extra_space)

# Call the lambda function
print(calculate_total(file_size))