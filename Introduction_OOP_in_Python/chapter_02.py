##################################################
print("#"*50)

# Create a Player class
class Player:
  
  # Create MAX_POSITION class attribute
  MAX_POSITION = 10
  
  # Add a constructor, setting position to zero
  def __init__(self):
    self.position = 0

# Create a player p and print its MAX_POSITION
p = Player()
print(p.MAX_POSITION)

##################################################
print("#"*50)

class Player:
  MAX_POSITION = 10
  
  # Define a constructor
  def __init__(self, position):
    
    # Check if position is less than the class-level attribute value
    if position <= Player.MAX_POSITION:
      self.position = position
    
    # If not, set equal to the class-level attribute
    else:
      self.position = Player.MAX_POSITION

# Create a Player object, p, and print its MAX_POSITITON
p = Player(6)
print(p.MAX_POSITION)

##################################################
print("#"*50)

# Create Players p1 and p2
p1 = Player(9)
p2 = Player(5)

print("MAX_POSITION of p1 and p2 before assignment:")
# Print p1.MAX_POSITION and p2.MAX_POSITION
print(p1.MAX_POSITION)
print(p2.MAX_POSITION)

# Assign 7 to p1.MAX_POSITION
p1.MAX_POSITION = 7

print("MAX_POSITION of p1 and p2 after assignment:")
# Print p1.MAX_POSITION and p2.MAX_POSITION
print(p1.MAX_POSITION)
print(p2.MAX_POSITION)

##################################################
print("#"*50)

class Person:
  CURRENT_YEAR = 2024
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  # Add a class method decorator
  @classmethod
  # Define the from_birth_year method
  def from_birth_year(cls, name, birth_year):
    # Create age
    age = Person.CURRENT_YEAR - birth_year
    # Return the name and age
    return cls(name, age)

bob = Person.from_birth_year("Bob", 1990)

###############################################
print("#"*50)

class BetterDate:
  def __init__(self, year, month, day):
    self.year, self.month, self.day = year, month, day
    
  # Define a class method from_str
  @classmethod
  def from_str(cls, datestr):
    # Split the string at "-"
    parts = datestr.split("-")
    year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
    # Return the class instance
    return cls(year, month, day)

# Create the xmas object      
xmas = BetterDate.from_str("2024-12-25")   
print(xmas.year)
print(xmas.month)
print(xmas.day)

##############################################
print("#"*50)

class Employee:
    MIN_SALARY = 30000    

    def __init__(self, name, salary=MIN_SALARY):
        self.name = name
        if salary >= Employee.MIN_SALARY:
            self.salary = salary
        else:
            self.salary = Employee.MIN_SALARY
        
    def give_raise(self, amount):
        self.salary += amount      
        
# Define a new class Manager inheriting from Employee
class Manager(Employee):
    # Add a keyword to leave this class empty
    pass

# Define a Manager object
mng = Manager("Debbie Lashko", 86500)

# Print mng's name
print(mng.name)

##############################################
print("#"*50)

class Employee:
  def __init__(self, name, salary=30000):
    self.name = name
    self.salary = salary

  def give_raise(self, amount):
    self.salary += amount

class Manager(Employee):
  # Add a constructor 
  def __init__(self, name, salary=50000, project=None):
    
    # Call the parent's constructor   
    Employee.__init__(self, name, salary)
    
    # Assign project attribute
    self.project = project

  def display(self):
    print("Manager ", self.name)

#######################################################
print("#"*50)

class Employee:
  def __init__(self, name, salary=30000):
    self.name = name
    self.salary = salary

  def give_raise(self, amount):
    self.salary += amount

class Manager(Employee):
  def display(self):
    print("Manager ", self.name)

  def __init__(self, name, salary=50000, project=None):
    Employee.__init__(self, name, salary)
    self.project = project

  # Add a give_raise method
  def give_raise(self, amount, bonus=1.05):
    new_amount = amount * bonus
    Employee.give_raise(self, new_amount)
    
mngr = Manager("Ashta Dunbar", 78500)
mngr.give_raise(2000, bonus=1.03)
print(mngr.salary)

###############################################
print("#"*50)

# Create a Racer class inheriting from Player
class Racer(Player):
  # Create MAX_POSITION with a value of 15
  MAX_POSITION = 15
  
# Create a Player and a Racer objects
p = Player()
r = Racer()

print("p.MAX_POSITION = ", p.MAX_POSITION)
print("r.MAX_POSITION = ", r.MAX_POSITION)