# Import the ABC class and abstractmethod decorator from abc
from abc import ABC, abstractmethod

# Define an abstract base class called Company
class Company(ABC):
  # Create an abstract method called create_budget()
  @abstractmethod
  def create_budget(self):
    pass
  
  # Create a concrete method with name hire_employee()
  def hire_employee(self, name):
    print(f"Welcome to the team, {name}!")

###################################################
print("#"*50)

# Create a class with the name "Technology"
class Technology(Company):
  def __init__(self, name):
    self.name = name

  # Define a create_budget() method
  def create_budget(self, year, expenses):
    for expense, amount in expenses.items():
      print(f"{year} budget for {expense} is {amount}")
  
# Create an instance of the Technology class, call methods
t = Technology("Tina's Tech Advisors")
t.create_budget(2024, {"Salaries": 10000, "Supplies": 500})
t.hire_employee("Christian")


####################################################
print("#"*50)

# Define a Company abstract base class with a pay_taxes() method
class Company1(ABC):
  @abstractmethod
  def pay_taxes(self):
    pass
  
  def report_revenue(self):
    print(f"{self.name} is reporting ${self.revenue} of revenue")

class Manufacturing(Company1):
  def __init__(self, name, revenue):
    self.name = name
    self.revenue = revenue

  # Implement the pay_taxes() method
  def pay_taxes(self, tax_rate):
    tax_amount = self.revenue * tax_rate
    print(f"{self.name} is paying ${tax_amount} of taxes")

# Create an instance of the Manufacturing class
m = Manufacturing("Morgan's Manufacturing", 5000)

# Make call to the pay_taxes() method, observe report_revenue()
m.pay_taxes(0.10)
m.report_revenue()

#####################################################
print("#"*50)

class Supplier:
  def take_order(self, product_name, quantity):
    pass

  def make_delivery(self, order_id, location):
    pass

class YogurtSupplier:
  def __init__(self):
    self.orders = {}
  
  # Finish defining the take_order() method
  def take_order(self, product_name, quantity):
    self.orders[f"{product_name}_{quantity}"] = {
      "product_name": product_name, "quantity": quantity
    }
  
  # Implement a make_delivery() abstract method
  def Xmake_delivery(self, order_id, location):
    print(f"Delivering order: {order_id} to {location}")
    del self.orders[order_id]

#####################################################
print("#"*50)

# Create a Product interface
class Product(ABC):
  
  # Define a purchase() abstract method
  @abstractmethod
  def purchase(self, quantity):
    pass
  
  # Create an update_price() abstract method
  @abstractmethod
  def update_price(self, new_price):
    pass

#####################################################
print("#"*50)

class Business(ABC):
  @abstractmethod
  def sell_product(self, product_name, price, quantity):
    pass

class Bakery(Business):
  def __init__(self, business_name):
    self.business_name = business_name
  
  # Provide a definition of the sell_product() method 
  def sell_product(self, product_name, price, quantity):
    total_revenue = price * quantity
    print(f"""{self.business_name} sold {quantity} {product_name} for a total of ${total_revenue}""")
    
# Attempt to create a Bakery object
blue_eyed_baker = Bakery("Blue Eyed Baker")

blue_eyed_baker.sell_product("cupcakes", 3, 20)

#####################################################
print("#"*50)

class Customer(ABC):
  @abstractmethod
  def make_payment(self, price):
    pass

class RewardsMember(Customer):
  def make_payment(self, price):
    print(f"""Total price for rewards member is 
          ${price * .90}, which is 10% off""")

class NewCustomer(Customer):
  def make_payment(self, price):
    print(f"""Total price for new customer is ${price}""")


class Checkout:
  # Create a _get_customer() factory method 
  def _get_customer(self, customer_type):
    if customer_type == "Rewards Member":
      return RewardsMember()
    elif customer_type == "New Customer":
      return NewCustomer()
  
  # Define the complete_transaction() method
  def complete_transaction(self, customer_type, price):
    customer = self._get_customer(customer_type)
    customer.make_payment(price)

######################################################
print("#"*50)

class DataPipeline:
  def _get_database(self, provider):
    if provider == "Postgres":
      return Postgres()
    elif provider == "Redshift":
      return Redshift()

  def extract_data(self, provider, query):
    database = self._get_database(provider)
    dataset = database.query_data(query)
    print(f"Extracted dataset from {provider} database")
    return dataset

####################################################
print("#"*50)

# Create an ETL DataPipeline, query using Redshift
items_pipeline = DataPipeline()
items_pipeline.extract_data("Redshift", "SELECT * FROM items;")

# Now, switch the pipeline to Postgres
items_pipeline.extract_data("Postgres", "SELECT * FROM items;")

# Finally, create an etl_pipeline with Redshift
etl_pipeline = DataPipeline()
etl_pipeline.extract_data("Redshift", "SELECT * FROM sales;")

######################################################
print("#"*50)

class LLM(ABC):
  @abstractmethod
  def complete_sentence(self, prompt):
    pass

class OpenAI(LLM):
  def complete_sentence(self, prompt):
    return prompt + " ... OpenAI end of sentence."
  
class Anthropic(LLM):
  def complete_sentence(self, prompt):
    return prompt + " ... Anthropic end of sentence."

class ChatBot:
  def _get_llm(self, provider):
    if provider == "OpenAI":
      return OpenAI()
    elif provider == "Anthropic":
      return Anthropic()
      
  def chat(self, prompt, provider):
    # Return an llm object, then call complete_sentence()
    llm = self._get_llm(provider)
    return llm.complete_sentence(prompt)





