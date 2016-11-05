def checkio(str_number, radix):
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
	decimal_value = 0
	for i in range(len(str_number)):
		if alphabet.find(str_number[i].lower()) >= radix:
			return -1
		else:
			decimal_value += alphabet.find(str_number[i].lower())*(radix**(len(str_number)-(i+1)))
	return decimal_value
