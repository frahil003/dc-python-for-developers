# Import the re module
import re

sentiment_analysis ="@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%"

# Write the regex
regex = r"(@robot\d\W)"

# Fund all matches of regex
print(re.findall(regex, sentiment_analysis))

##################################################
print('#'*50)

sentiment_analysis ="Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, number of retweets: 78"

# Write a regex to obtain user mentions
print(re.findall(r"User_mentions:\d", sentiment_analysis))

# Write a regex to obtain number of likes
print(re.findall(r"likes:\s\d", sentiment_analysis))

# Write a regex to obtain number of retweets
print(re.findall(r"number\sof\sretweets:\s\d", sentiment_analysis))

###########################################

sentiment_analysis = "He#newHis%newTin love with$newPscrappy. #8break%He is&newYmissing him@newLalready"

# Write a regex to match pattern separating sentences
regex_sentence = r"\W\dbreak\W"

# Replace the regex_sentence with a space
sentiment_sub = re.sub(regex_sentence, " ", sentiment_analysis)

# Write a regex to match pattern separating words
regex_words = r"\Wnew\w"

# Replace the regex_words and print the result
sentiment_final = re.sub(regex_words, " ", sentiment_sub)
print(sentiment_final)

##########################################
print("#"*50)

sentiment_analysis = "ITS NOT ENOUGH TO SAY THAT IMISS U #MissYou #SoMuch #Friendship #Forever"

# Write a regex matching the hashtag pattern
regex = r"#\w+"

# Replace the regex by an empty string
no_hashtag = re.sub(regex, "", sentiment_analysis)
print(no_hashtag)

# Get tokens by splitting text
print(re.split(r"\s+", no_hashtag))

##################################################
print("#"*50)

emails = ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']

# Write a regex to match a valid email address
regex = r"[A-Za-z0123456789!#%&*$.]+@\w+\.com"

for example in emails:
  # Match the regex to the string
  if re.match(regex, example):
    # Complete the format method to print out the result
    print("The email {email_example} is a valid email".format(email_example=example))
  else:
   	print("The email {email_example} is invalid".format(email_example=example))   

###########################################
print("#"*50)

passwords = ['Apple34!rose', 'My87hou#4$', 'abc123']

# Write a regex to check if the password is valid
regex = r"[a-zA-Z0123456789*#$%!&.]{8,20}"

for example in passwords:
  	# Scan the strings to find a match
    if re.match(regex, example):
      # Complete the format method to print out the result
      print("The password {pass_example} is a valid password".format(pass_example=example))
    else:
      print("The password {pass_example} is invalid".format(pass_example=example))   

###########################################
print("#"*50)

string = "I want to see that <strong>amazing show</strong> again!"

# Write a regex to eliminate tags
#regex = r"<\w+>|</\w+>"
regex = r"<.+?>"

string_notags = re.sub(regex, "", string)

# Print out the result
print(string_notags)

############################################
print("#"*50)

sentiment_analysis = "Was intending to finish editing my 536-page novel manuscript tonight, but that will probably not happen. And only 12 pages are left"

# Write a lazy regex expression 
numbers_found_lazy = re.findall(r"\d+?", sentiment_analysis)

# Print out the result
print(numbers_found_lazy)

# Write a greedy regex expression 
numbers_found_greedy = re.findall(r"\d+", sentiment_analysis)

# Print out the result
print(numbers_found_greedy)

############################################
print("#"*50)

sentiment_analysis = "Put vacation photos online (They were so cute) a few yrs ago. PC crashed, and now I forget the name of the site (I'm crying)."

# Write a greedy regex expression to match 
sentences_found_greedy = re.findall(r"\(.+\)", sentiment_analysis)

# Print out the result
print(sentences_found_greedy)

# Write a lazy regex expression
sentences_found_lazy = re.findall(r"\(.+?\)", sentiment_analysis)

# Print out the results
print(sentences_found_lazy)





