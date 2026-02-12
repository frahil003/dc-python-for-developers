def clean_text(text):
  # Check the data type
  if type(text) == str:
    return text.replace(" ", "_").lower()
  else:
    # Return a TypeError error if the wrong data type was used
    raise TypeError("The clean_text() function expects a string as an argument, please check the data type provided!")
    
clean_text("User Name 187")