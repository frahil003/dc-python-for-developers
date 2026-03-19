class Node:
  def __init__(self, data):
    self.value = data
    # Leave the node initially without a next value
    self.next = None

class LinkedList:
  def __init__(self):
    # Set the head and the tail with null values
    self.head = None
    self.tail = None

  def insert_at_beginning(self, data):
    # Create the new node
    new_node = Node(data)
    # Check whether the linked list has a head node
    if self.Head:
      # Point the next node of the new node to the head
      new_node.next = self.head
      self.head = new_node
    else:
      self.tail = new_node      
      self.head = new_node
  
  def remove_at_beginning(self):
    # The "next" node of the head becomes the new head node
    self.head = self.head.next

  def search(self, data):
    current_node = self.head
    while current_node:
        if current_node.data == data:
            return True
        else:
            current_node = current_node.next
    return False

#################################################################
print('#'*50)

colors = ['green', 'yellow', 'blue', 'pink']

def linear(colors):
  # Iterate the elements of the list
  for color in colors:
    # Print the current element of the list
    print(color)	

linear(colors)

###################################################
print("#"*50)

class Stack:
  def __init__(self):
    self.top = None
    self.size = 0
    
  def push(self, data):
    # Create a node with the data
    new_node = Node(data)
    if self.top:
      new_node.next = self.top
    # Set the created node to the top node
    self.top = new_node
    # Increase the size of the stack by one
    self.size += 1

  def pop(self):
    # Check if there is a top element
    if self.top is None:
      return None
    else:
      popped_node = self.top
      # Decrement the size of the stack
      self.size -= 1
      # Update the new value for the top node
      self.top = self.top.next
      popped_node.next = None
      return popped_node.data 

################################################################
print("#"*50)
    
# Import the module to work with Python's LifoQueue
import queue

# Create an infinite LifoQueue
my_book_stack = queue.LifoQueue(maxsize=0)

# Add an element to the stack
my_book_stack.put("Don Quixote")

# Remove an element from the stack
my_book_stack.get()

