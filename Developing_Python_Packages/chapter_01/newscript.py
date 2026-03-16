from textanalysis.textanalysis import count_words

filepath = "data/hotel-reviews.txt"

# Count the number of positive words
nb_positive_words = count_words(filepath, ["good", "great"])

# Count the number of negative words
nb_negative_words = count_words(filepath, ["bad", "awful"])

print("{} positive words.".format(nb_positive_words))
print("{} negative words.".format(nb_negative_words))
