def verify_anagrams(first_word, second_word):
    first_word = format_word(first_word)
	second_word = format_word(second_word)
	for letter in first_word:
		try:
			second_word.remove(letter)
		except ValueError:
			return False
	if len(second_word) == 0:
		return True
	return False

def format_word(word):
	word = word.lower()
	word = word.replace(" ","")
	return list(word)
