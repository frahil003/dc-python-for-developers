class Computer:
  def __init__(self, storage = 0, serial_number = "12345", device_id = "asdf", software_version = "0.0.0"):
    self.device_id = device_id
    self.serial_number = serial_number
    self.storage = storage
    self.software_version = software_version

  # Overload the == operator using a magic method
  def __eq__(self, other):
    # Return a boolean based on the value of device_id
    return self.device_id == other.device_id  

  def add_external_drive(self, external_storage):
    self.storage += external_storage
    print(f"Your computer now has {self.storage} GB of storage.")

  def install_app(self, app_name, app_store):
    if app_store:
      print(f"Installing {app_name} from App Store.")
    else:
      print(f"Installing {app_name} from other provider.")

  def update_software(self, new_software_version):
      self.software_version = new_software_version

  @classmethod
  def power_on(cls):
    print("Your computer is starting up!")

my_computer = Computer(512)

# Add an external drive of 256 GB
my_computer.add_external_drive(256)

#############################################
print("#"*50)

class Tablet(Computer):
  # Override the install_app() method
  def install_app(self, app_name):
    print(f"{app_name} is being installed from the Tablet App Store.")
    

# Create the my_tablet instance
my_tablet = Tablet("1.1.1")

# Update my_tablet's software to version 1.1.2
my_tablet.update_software("1.1.2")
print(my_tablet.software_version)

# Call the new install_app() method
my_tablet.install_app("DataCamp")

pre_upgrade_computer = Computer(256, "Y391Hky6")
post_upgrade_computer = Computer(1024, "Y391Hky6")

# Create two instances of Computer, compare using ==
print(pre_upgrade_computer == post_upgrade_computer)

#################################################
print("#"*50)

class Storage:
  def __init__(self, capacity):
    self.capacity = capacity
  
  def __add__(self, other):  # Overload the + operator
    # Create a Storage object with the sum of capacity
    return Storage(self.capacity + other.capacity)

onboard_storage = Storage(128)
external_drive = Storage(64)

# Add the two Storage objects, show the total capacity
total_storage = onboard_storage + external_drive
print(f"Total storage capacity: {total_storage.capacity} GB")

###############################################
print("#"*50)

class Network:
  def __init__(self, ip_addresses):
    self.ip_addresses = ip_addresses

class Computer1:
  def __init__(self, operating_system, ip_address):
    self.operating_system = operating_system
    self.ip_address = ip_address
  
  # Overload the + operator to create a Network of devices 
  # if the operating_systems are the same
  def __add__(self, other):
    if self.operating_system == other.operating_system:
      return Network([self.ip_address, other.ip_address])
    raise Exception("Incompatible operating systems.")

# Build a network using Morgan and Jenny's Computers
morgans_computer = Computer1("Windows", "182.112.81.991")
jennys_computer = Computer1("Windows", "177.511.64.162")
network = morgans_computer + jennys_computer
print(network.ip_addresses)

#############################################
print("#"*50)

class Computer3:
  def __init__(self, brand):
    self.brand = brand

  def browse_internet(self):
    print(f"Using {self.brand}'s default internet browser.")

class Telephone:
  def __init__(self, phone_number):
    self.phone_number = phone_number

  def make_call(self, recipient):
    print(f"Calling {recipient} from {self.phone_number}")

class Smartphone(Computer3, Telephone):
  def __init__(self, brand, phone_number, music_app):
    Computer3.__init__(self, brand)
    Telephone.__init__(self, phone_number)
    self.music_app = music_app
    
  def play_music(self, song):
    print(f"Playing {song} using {self.music_app}")

personal_phone = Smartphone("Macrosung", "801-932-7629", "Dotify")

# Browse the internet, make a call to Alex, and play music
personal_phone.browse_internet()
personal_phone.make_call("Alex")
personal_phone.play_music("Creeks and Highways")

################################################
print("#"*50)

class Tablet(Computer3):
  def __init__(self, brand, apps):
    Computer3.__init__(self, brand)
    self.apps = apps

  def uninstall_app(self, app):
    if app in self.apps:
      self.apps.remove(app)

# Create a Smartphone class that inherits from Tablet
class Smartphone2(Tablet):
  def __init__(self, brand, apps, phone_number):
    Tablet.__init__(self, brand, apps)
    self.phone_number = phone_number
  
  # Create send_text to send a message to a recipient
  def send_text(self, message, recipient):
    print(f"Sending {message} to {recipient} from {self.phone_number}")

# Create an instance of Smartphone, call methods in each class
personal_phone = Smartphone2("Macrosung", ["Weather", "Camera"], "801-932-7629")    
personal_phone.browse_internet()
personal_phone.uninstall_app("Weather")
personal_phone.send_text("Time for a new mission!", "Chuck")

