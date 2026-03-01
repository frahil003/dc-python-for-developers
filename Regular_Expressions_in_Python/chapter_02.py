print('#'*50)

wikipedia_article = "In computer science, artificial intelligence (AI), sometimes called machine intelligence, is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals."

my_list = []

# Assign the substrings to the variables
first_pos = wikipedia_article[3:20].lower()
second_pos = wikipedia_article[21:45].lower()
print(first_pos)
print(second_pos)

# Define string with placeholders 
my_list.append("The tool {} is used in {}")

# Define string with rearranged placeholders
my_list.append("The tool {1} is used in {0}")

# Use format to print strings
for my_string in my_list:
  	print(my_string.format(first_pos, second_pos))

##################################################
print('#'*50)

courses = ['artificial intelligence', 'neural networks']

# Create a dictionary
plan = {
  		"field": courses[0],
        "tool": courses[1]
}

# Complete the placeholders accessing elements of field and tool keys in the data dictionary
my_message = "If you are interested in {data[field]}, you can take the course related to {data[tool]}"

# Use the plan dictionary to replace placeholders
print(my_message.format(data=plan))

#################################################
print('#'*50)

# Import datetime 
from datetime import datetime

# Assign date to get_date
get_date = datetime.now()

# Add named placeholders with format specifiers
message = "Good morning. Today is {today:%B %d, %Y}. It's {today:%H:%M} ... time to work!"

# Use the format method replacing the placeholder with get_date
print(message.format(today=get_date))


##############################################
print('#'*50)

field1 ="sexiest job"
field2 = "data is produced daily"
field3 = "Individuals"
fact1 = 21
fact2 = 2500000000000000000
fact3 = 72.41415415151
fact4 = 1.09

# Complete the f-string
print(f"Data science is considered {field1!r} in the {fact1:d}st century")

# Complete the f-string
print(f"About {fact2:e} of {field2} in the world")

# Complete the f-string
print(f"{field3} create around {fact3:.2f}% of the data but only {fact4:.1f}% is analyzed")

#########################################
print("#"*50)

number1 = 120
number2 = 7
string1 = "httpswww.datacamp.com"
list_links = ['www.news.com', 'www.google.com', 'www.yahoo.com', 'www.bbc.com', 'www.msn.com', 'www.facebook.com', 'www.news.google.com']

# Include both variables and the result of dividing them 
print(f"{number1} tweets were downloaded in {number2} minutes indicating a speed of {number1/number2:.1f} tweets per min")

# Replace the substring https by an empty string
print(f"{string1.replace('https', '')}")

# Divide the length of list by 120 rounded to two decimals
print(f"Only {len(list_links)*100/120:.2f}% of the posts contain links")

#########################################
print("#"*50)

east = {'date': datetime(2007, 4, 20, 0, 0), 'price': 1232443}
west = {'date': datetime(2006, 5, 26, 0, 0), 'price': 1432673}

# Access values of date and price in east dictionary
print(f"The price for a house in the east neighborhood was ${east['price']} in {east['date']:%m-%d-%Y}")

# Access values of date and price in west dictionary
print(f"The price for a house in the west neighborhood was ${west['price']} in {west['date']:%m-%d-%Y}.")

########################################
print("#"*50)

tool1 = "Natural Language Toolkit"
tool2 = "TextBlob"
tool3 = "Gensim"
description1 = "suite of libraries and programs for symbolic and statistical natural language processing (NLP) for English written in the Python programming language. It was developed by Steven Bird and Edward Loper in the Department of Computer and Information Science at the University of Pennsylvania."
description2 = "Python library for processing textual data. It provides a simple API for diving into common natural language processing tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more."
description3 = "robust open-source vector space modeling and topic modeling toolkit implemented in Python. It uses NumPy, SciPy and optionally Cython for performance. Gensim is specifically designed to handle large text collections, using data streaming and efficient incremental algorithms, which differentiates it from most other scientific software packages that only target batch and in-memory processing."

# Import Template
from string import Template

# Create a template
wikipedia = Template("$tool is a $description")

# Substitute variables in template
print(wikipedia.substitute(tool=tool1, description=description1) + "\n")
print(wikipedia.substitute(tool=tool2, description=description2) + "\n")
print(wikipedia.substitute(tool=tool3, description=description3) + "\n")

##################################################################
print("#"*50)

tools = ['Natural Language Toolkit', '20', 'month']

# Import template
from string import Template

# Select variables
our_tool = tools[0]
our_fee = tools[1]
our_pay = tools[2]

# Create template
course = Template("We are offering a 3-month beginner course on $tool just for $$ $fee ${pay}ly")

# Substitute identifiers with three variables
print(course.substitute(tool=our_tool, fee=our_fee, pay=our_pay))

###########################################
print("#"*50)

answers = {'answer1': 'I really like the app. But there are some features that can be improved'}

# Import template
from string import Template

# Complete template string using identifiers
the_answers = Template("Check your answer 1: $answer1, and your answer 2: $answer2")

# Use safe_substitute to replace identifiers
try:
    print(the_answers.safe_substitute(answers))
except KeyError:
    print("Missing information")
