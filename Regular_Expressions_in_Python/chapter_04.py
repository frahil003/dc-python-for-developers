import re

sentiment_analysis = [
  'Just got ur newsletter, those fares really are unbelievable. Write to statravelAU@gmail.com or statravelpo@hotmail.com. They have amazing prices',

  'I should have paid more attention when we covered photoshop in my webpage design class in undergrad. Contact me Hollywoodheat34@msn.net.',

  'hey missed ya at the meeting. Read your email! msdrama098@hotmail.com']

# Write a regex that matches email
regex_email = r"([a-zA-Z0-9]+)@\S+"

for tweet in sentiment_analysis:
    # Find all matches of regex in each tweet
    email_matched = re.findall(regex_email, tweet)

    # Complete the format method to print the results
    print("Lists of users found in this tweet: {}".format(email_matched))

#########################################
print("#"*50)

flight = "Subject: You are now ready to fly. Here you have your boarding pass IB3723 AMS-MAD 06OCT"

# Import re
import re

# Write regex to capture information of the flight
regex = r"([A-Z]{2})(\d{4})\s([A-Z]{3})-([A-Z]{3})\s(\d{2}[A-Z]{3})"

# Find all matches of the flight information
flight_matches = re.findall(regex, flight)
print(flight_matches)
    
#Print the matches
print("Airline: {} Flight number: {}".format(flight_matches[0][0], flight_matches[0][1]))
print("Departure: {} Destination: {}".format(flight_matches[0][2], flight_matches[0][3]))
print("Date: {}".format(flight_matches[0][4]))

##########################################
print("#"*50)

sentiment_analysis = [
    'I totally love the concert The Book of Souls World Tour. It kinda amazing!',
    'I enjoy the movie Wreck-It Ralph. I watched with my boyfriend.',
    "I still like the movie Wish Upon a Star. Too bad Disney doesn't show it anymore."]

# Write a regex that matches sentences with the optional words
regex_positive = r"(love|like|enjoy).+?(movie|concert)\s(.+?)\."

for tweet in sentiment_analysis:
	# Find all matches of regex in tweet
    positive_matches = re.findall(regex_positive, tweet)
    
    # Complete format to print out the results
    print("Positive comments found {}".format(positive_matches))

###########################################
print("#"*50)

sentiment_analysis = [
'That was horrible! I really dislike the movie The cabin and the ant. So boring.',
"I disapprove the movie Honest with you. It's full of cliches.",
'I dislike very much the concert After twelve Tour. The sound was horrible.']

# Write a regex that matches sentences with the optional words
regex_negative = r"(hate|dislike|disapprove).+?(?:movie|concert)\s(.+?)\."

for tweet in sentiment_analysis:
	# Find all matches of regex in tweet
    negative_matches = re.findall(regex_negative, tweet)
    
    # Complete format to print out the results
    print("Negative comments found {}".format(negative_matches))