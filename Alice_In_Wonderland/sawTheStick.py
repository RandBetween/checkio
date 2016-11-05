def checkio(number):
    array = generate_triangular(number)
	array = array[::-1]
	solutions = []
	for i in range(len(array)):
		solutions.append(check_list(array[i:], number))
	solutions2 = [x for x in solutions if x is not None]
	solutions2.sort(key=len, reverse=True)
	if len(solutions2) > 0:
		return solutions2[0][::-1]
	else:
		return []


def generate_triangular(limit):
	list = []
	current_num = 0
	increment = 1
	while current_num <= limit:
		list.append(current_num)
		current_num += increment
		increment += 1
	return list

def check_list(list, target):
	sum = 0
	for j in range(len(list)):
		sum += list[j]
		if sum == target:
			return list[:j+1]
