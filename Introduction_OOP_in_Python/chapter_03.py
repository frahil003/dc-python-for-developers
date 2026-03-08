class BankAccount:
  # Modify to initialize a number attribute
  def __init__(self, number, balance=0):
    self.balance = balance
    self.number = number
      
  def withdraw(self, amount):
    self.balance -= amount 
    
  # Define __eq__ that returns True if the number attributes are equal 
  def __eq__(self, other):
    return (self.number == other.number)   

# Create accounts and compare them       
acct1 = BankAccount(123, 1000)
acct2 = BankAccount(123, 1000)
acct3 = BankAccount(456, 1000)
print(acct1 == acct2)
print(acct1 == acct3)

###################################################
print("#"*50)

# Modify the function to catch exceptions
def invert_at_index(x, ind):
  try:
    return 1/x[ind]
  except ZeroDivisionError:
    print("Cannot divide by zero!")
  except IndexError:
    print("Index out of range!")
 
a_list = [5,6,0,7]

# Works okay
print(invert_at_index(a_list, 1))

# Potential ZeroDivisionError
print(invert_at_index(a_list, 2))

# Potential IndexError
print(invert_at_index(a_list, 5))

###################################################
print("#"*50)

class SalaryError(ValueError): 
  pass
class BonusError(SalaryError): 
  pass

class Employee:
  MIN_SALARY = 30000
  MAX_BONUS = 5000

  def __init__(self, name, salary = 30000):
    self.name = name    
    if salary < Employee.MIN_SALARY:
      raise SalaryError("Salary is too low!")      
    self.salary = salary
    
  # Raise exceptions  
  def give_bonus(self, amount):
    if amount > Employee.MAX_BONUS:
      raise BonusError("The bonus amount is too high!")  
        
    elif self.salary + amount <  Employee.MIN_SALARY:
      raise SalaryError("The salary after bonus is too low!")
      
    self.salary += amount
    