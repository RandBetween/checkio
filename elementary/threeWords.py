def checkio(words):
    split_list = words.split()
	integer_list = [1 if split_list[x].isalpha() else 0 for x in range(len(split_list))]
	if len(integer_list) >= 3:
		for i in range(0,len(integer_list)-2):
			if integer_list[i] + integer_list[i+1] + integer_list[i+2] == 3:
				return True
		return False
	return False
