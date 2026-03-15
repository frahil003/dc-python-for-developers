import random
# Import Dict and List from typing
from typing import Dict, List

# Type hint the roster of codenames and number of missions
roster: Dict[str, int] = {
  "Chuck": 37,
  "Devin": 2,
  "Steven": 4
}

# Unpack the values and add type hints for the new list
agents: List[str] = [
  f"Agent {agent}, {missions} missions" \
  for agent, missions in roster.items()
]

###############################################
print("#"*50)

class Agent:
  def __init__(self, codename: str, missions: int):
    self.codename: str = codename
    self.missions: int = missions

  def add_mission(self, location: str) -> None:
    self.missions += 1
    print(f"{self.codename} completed a mission in " + \
          f"{location}. This was mission #{self.missions}")

# Create an Agent object, add type hints
chuck: Agent = Agent("Charles Carmichael", 37)

# Create a list of locations, add a mission for each
locations: List[str] = ["Burbank", "Paris", "Prague"]
for location in locations:
  chuck.add_mission(location)

##############################################
print("#"*50)

class BankAccount:
  def __init__(self, balance):
    self.balance = balance

  @property
  def balance(self):
    return f"${round(self._balance, 2)}"

  @balance.setter
  def balance(self, new_balance):
    if new_balance > 0:
      self._balance = new_balance

  @balance.deleter
  def balance(self):
    print("Deleting the 'balance' attribute")
    del self._balance

checking_account = BankAccount(100)

# Output the balance of the checking_account object
print(checking_account.balance)

# Set the balance to 150, output the new balance
checking_account.balance = 150
print(checking_account.balance)

# Delete the balance attribute, attempt to print the balance
del checking_account.balance

##############################################
print("#"*50)

class BankAccount1:
  def __init__(self, email):
    self.email = email
    
  @property
  def email(self):
    return f"Email for this account is: {self._email}"
  
  @email.setter
  def email(self, new_email_address):
    if "@" in new_email_address:
      self._email = new_email_address
    else:
      print("Please make sure to enter a valid email.")
  
  # Define a method to be used when deleting the email attribute
  @email.deleter
  def email(self):
    del self._email
    print("Email deleted, make sure to add a new email!")

####################################################
print("#"*50)

class BankAccount1:
  def __init__(self, account_number):
    self.account_number = account_number
  
  # Define a magic method to handle references to attribute
  # not in an object's namespace
  def __getattr__(self, name):
    # Output a message to instruct further action
    print(f"""{name} is not defined in BankAccount object.
    	Please define this attribute if needed.""")
    
# Create a BankAccount object, reference routing_number
checking_account = BankAccount1("123456")
checking_account.routing_number

################################################
print("#"*50)

class BankAccount2:
  def __init__(self, account_number):
    self.account_number = account_number
  
  def __setattr__(self, name, value):
    if name in ["account_number", "balance"]:
      print(f"{name} is an allowed attribute.")
      self.__dict__[name] = value
    else:
      print(f"Invalid Attribute: {name}")

# Use savings_account and attempt to set attributes
savings_account = BankAccount2("12345678")
savings_account.balance = 100
savings_account.beneficiary = "Anna Wu"

###############################################
print("#"*50)

class Playlist:
  def __init__(self, songs, shuffle=False):
    self.songs = songs
    self.index = 0
    
    if shuffle:
      random.shuffle(self.songs)
    
  def __iter__(self):
    return self
  
  # Define a magic method to iterate through songs
  def __next__(self):
    if self.index >= len(self.songs):
      raise StopIteration
    
    # Pull the next song, increment index, and return
    song = self.songs[self.index]
    self.index += 1
    return song

# Shuffle a Playlist, use for loop to iterate through
favorite_songs = Playlist(["Ticking", "Tiny Dancer"], shuffle=True)
for song in favorite_songs:
  print(song)


################################################
print("#"*50)

class Playlist1:
  def __init__(self, songs, shuffle=False):
    self.songs = songs
    self.index = 0

    if shuffle:
      random.shuffle(self.songs)

  def __iter__(self):
    return self

  def __next__(self):
    if self.index >= len(self.songs):
      raise StopIteration

    print(f"Playing {self.songs[self.index]}")
    self.index += 1

# Create a classic rock playlist using the songs list
songs = ["Hooked on a Feeling", "Yesterday", "Mr. Blue Sky"]
classic_rock_playlist = Playlist1(songs, shuffle=True)

while True:
	try:
		# Play the next song in the playlist
		next(classic_rock_playlist)
		
	# If there is a StopIteration error, print a message and
    # stop the playlist
	except StopIteration:
		print("Reached end of playlist!")
		break

#############################################
print("#"*50)

class Lottery:
  def __init__(self, number_digits):
    self.number_digits = number_digits
    self.counter = 0
  
  # Create an iterator using a magic method
  def __iter__(self):
    return self
  
  # Check if the number of digits have been reached, or else
  # pull another number
  def __next__(self):
    if self.counter < self.number_digits:
      self.counter += 1
      return random.randint(0, 9)

    raise StopIteration
  
charity_lottery = Lottery(4)

# Announce all four numbers
while True:
  try:
    print(next(charity_lottery))
  
  # Handle the last element of the iterator, print a message
  except StopIteration:
    print("... is the winner!")
    break

  






