import requests
from pprint import pprint

response = requests.get('http://franks-divecenter.de')

print("#"*50)
print(response.status_code)

print("#"*50)
pprint(dict(response.headers))

print("#"*50)
#print(response.text)
