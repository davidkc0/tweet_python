import re

def main():
	file = open("corpus.txt")
	text_string = file.read()
	good_words = re.findall("[A-z]+\'?[A-z]*", text_string)
	markov = dict()
	for i in range(0,30):
		print(good_words[i])


	for i in range(0, len(good_words) -1):
		











	# for word in good_words:
	# 	print(word)

	# for words in line:
	# 	word = line.split 
def assign_number():





main()