def clean_text(text):
  # Attempt to clean the text
  try:
    return text.replace(" ", "_").lower()
  # Run this code if an error occurs
  except:
    print("The clean_text() function expects a string as an argument, please check the data type provided!")
    
clean_text(187)