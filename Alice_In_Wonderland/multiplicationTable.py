from operator import xor

def checkio(first, second):
    x1 = format(first, 'b')
	y1 = format(second, 'b')

	sum = 0

	sum += and_table(first, second, x1, y1)
	sum += or_table(first, second, x1, y1)
	sum += xor_table(first, second, x1, y1)

	return sum

def and_table(first, second, x1, y1):
	dec = []
	for i in range(len(x1)):
		temp_list = []
		for j in range(len(y1)):
			temp_list.append(str(int(x1[i]) and int(y1[j])))
		bit = "".join(temp_list)
		dec.append(int(bit, 2))
	return sum(dec)

def or_table(first, second, x1, y1):
	dec = []
	for i in range(len(x1)):
		temp_list = []
		for j in range(len(y1)):
			temp_list.append(str(int(x1[i]) or int(y1[j])))
		bit = "".join(temp_list)
		dec.append(int(bit, 2))
	return sum(dec)

def xor_table(first, second, x1, y1):
	dec = []
	for i in range(len(x1)):
		temp_list = []
		for j in range(len(y1)):
			temp_list.append(xor(bool(int(x1[i])), bool(int(y1[j]))))
		temp_list2 = [str(int(val)) for val in temp_list]
		bit = "".join(temp_list2)
		dec.append(int(bit, 2))
	return sum(dec)
