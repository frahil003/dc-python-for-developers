from urllib.request import urlopen

with urlopen('http://localhost:3000/lyrics/') as response:
  
  # Use the correct function to read the response data from the response object
  data = response.read()
  encoding = response.headers.get_content_charset()

  # Decode the response data so you can print it as a string later
  string = data.decode(encoding)
  
  print(string)


  ################################################################

  # Import the requests package
import requests

# Pass the API URL to the get function
response = requests.get("http://localhost:3000/lyrics")

# Print out the text attribute of the response object
print(response.text)


########################################

# Add the `include_track` parameter
query_params = {'artist': 'Deep Purple', 'include_track' : True}

response = requests.get('http://localhost:3000/lyrics/random', params=query_params)

# Print the response URL
print(response.url)

# Print the lyric
print(response.text)

###########################################

response = requests.get('http://localhost:3000/movies')

# Check if the response.status_code is equal to the requests.codes value for "200 OK"
if (response.status_code == requests.codes.ok):
  print('The server responded succesfully!')
  
# Or if the request was not successful because the API did not exist
elif (response.status_code == requests.codes.not_found):
  print('Oops, that API could not be found!')

  ####################################

  # Add a header to use in the request
headers = {'accept': 'application/xml'}
response = requests.get('http://localhost:3000/lyrics', headers=headers)

# Check if the server did not accept the request
if (response.status_code == 406):
  print('The server can not respond in XML')
  
  # Print the accepted content types
  print('These are the content types the server accepts: ' + response.headers['accept'])
else:
  print(response.text)

