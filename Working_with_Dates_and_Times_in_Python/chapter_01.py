# Import date from datetime
from datetime import date
from repo import datesflorida

florida_hurricane_dates = [date(dates[0], dates[1], dates[2]) for dates in datesflorida]
print("Type of datesfloria: " + str(type(datesflorida)))
#print(datesflorida)



# Create a date object
hurricane_andrew = date(1992, 8, 24)

# Which day of the week is the date?
print("Weekday(number): " + str(hurricane_andrew.weekday()))

###################################################

# Counter for how many before June 1
early_hurricanes = 0

# We loop over the dates
for hurricane in florida_hurricane_dates:
  # Check if the month is before June (month number 6)

  if hurricane.month < 6:
    early_hurricanes = early_hurricanes + 1
    
print("Early hurricanes (total): " + str(early_hurricanes))


################################################################

# Create a date object for May 9th, 2007
start = date(2007, 5, 9)

# Create a date object for December 13th, 2007
end = date(2007, 12, 13)

# Subtract the two dates and print the number of days
print(f"Days from {end} - {start} : {(end - start).days} days!")

######################################

# A dictionary to count hurricanes per calendar month
hurricanes_each_month = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6:0,
		  				 7: 0, 8:0, 9:0, 10:0, 11:0, 12:0}

# Loop over all hurricanes
for hurricane in florida_hurricane_dates:
  # Pull out the month
  month = hurricane.month
  # Increment the count in your dictionary by one
  hurricanes_each_month[month] += 1
  
print(hurricanes_each_month)

#########################################
dates_scrambled = florida_hurricane_dates # just a copy. NOT scrambled

# Print the first and last scrambled dates
print(dates_scrambled[0])
print(dates_scrambled[-1])

# Put the dates in order
dates_ordered = sorted(dates_scrambled)

# Print the first and last ordered dates
print(dates_ordered[0])
print(dates_ordered[-1])