#wordcount.py display the 10 most used words in the story of little red riding hood (wording retreived from chatGPT)
# all punctuation has been removed.  All words are being lowercased


# Set up dictionary of words and counts
count = dict()
with open("littleredridinghood.txt", "r") as file:
	words = file.read().split()
	for word in words:
		lower_case = word.lower()
		count[lower_case] = count.get(lower_case, 0) + 1
#create a list of tuples with words and count of words and sort the list reversed by count of word

word_count = sorted([(v,k) for k,v in count.items()], reverse = True)

print(word_count[:10])

