import queue

class PrinterTasks:
  def __init__(self):
    self.queue = queue.Queue()
      
  def add_document(self, document):
    # Add the document to the queue
    self.queue.enqueue(document)
      
  def print_documents(self):
    # Iterate over the queue while it has elements
    while self.queue.has_elements():
      # Remove the document from the queue
      print("Printing", self.queue.dequeue())

#################################################################
print("#"*50)

import queue

# Create the queue
my_orders_queue = queue.SimpleQueue()

# Add an element to the queue
my_orders_queue.put("samosas")

# Remove an element from the queue
my_orders_queue.get()