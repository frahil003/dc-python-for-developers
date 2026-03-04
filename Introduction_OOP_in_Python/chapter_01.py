#############################################
print("#"*50)

ratio = 12 / 8

# List all attributes and methods for the ratio object
print(dir(ratio))

#############################################
print("#"*50)

# List all attributes and methods for the float class
print(dir(float))

#############################################
print("#"*50)

class Employee:
  
  # Include a set_name method
  def set_name(self, new_name):
    self.name = new_name

emp = Employee()

# Use set_name() on emp to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')
print(emp.name)

#############################################
print("#"*50)

class Employee:
  def set_name(self, new_name):
    self.name = new_name
  
  # Add set_salary() method  
  def set_salary(self, new_salary):
    self.salary = new_salary 

emp = Employee()

# Use set_name to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Set the salary of emp to 50000
emp.set_salary(50000)

# Print the emp object's salary
print(emp.salary)

#############################################
print("#"*50)

class Employee:
  def set_name(self, new_name):
    self.name = new_name

  def set_salary(self, new_salary):
    self.salary = new_salary 

  # Add a give_raise() method with amount as an argument
  def give_raise(self, amount):
    self.salary = self.salary + amount

# Create the emp object
emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Print the salary
print(emp.salary)

# Give emp a raise of 1500
emp.give_raise(1500)
print(emp.salary)

#############################################
print("#"*50)

class Employee:
  def __init__(self, name, salary=0):
    self.name = name
    # Check if salary is positive
    if salary > 0:
      self.salary = salary
    else:
      self.salary = 0
      print("Invalid salary!")

  def give_raise(self, amount):
    self.salary += amount

  def monthly_salary(self):
    return self.salary / 12
      
emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)

#############################################
print("#"*50)

# Define and initialize the Calculator class
class Calculator:
  def __init__(self, num_one, num_two):
    self.num_one = num_one
    self.num_two = num_two
  
  # Create the addition method
  def addition(self, num_one, num_two):
    return self.num_one + self.num_two
  
  # Create the subtraction method
  def subtraction(self, num_one, num_two):
    return self.num_one - self.num_two
  
  # Create the multiplication method
  def multiplication(self, num_one, num_two):
    return self.num_one * self.num_two   