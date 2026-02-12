# Define a function called concat
def concat(**kwargs):
  """Concatenates keyword arguments into a single string with spaces."""
  
  result = ""
  
  # Iterate over the Python kwargs
  for kwarg in kwargs.values():
    result += " " + kwarg
  return result

# Call the function
print(concat(start="Python", middle="is", end="great!"))