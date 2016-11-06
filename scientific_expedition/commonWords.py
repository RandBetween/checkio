def checkio(first, second):
    first = first.split(",")
	second = second.split(",")
	final_list = []
	for item in first:
		if item in second:
			final_list.append(item)
	final_list.sort()
	return ",".join(final_list)
