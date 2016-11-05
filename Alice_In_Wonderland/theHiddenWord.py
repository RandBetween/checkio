def checkio(text, word):
    text = text.lower()
    text = text.replace(" ", "")
	y = text.splitlines()
	y_rows = len(y)
	horizontal_search = "".join(y)
	y2 = flip_text(y)
	y2_rows = len(y2)
	vertical_search = "".join(y2)
	try:
		position = horizontal_search.index(word)
		row_cutoffs = []
		z = 0
		for i in range(y_rows):
			row_cutoffs.append(len(y[i])+z)
			z += len(y[i])
		first_row = 0
		second_row = 0
		second_col = 0
		for k in range(len(row_cutoffs)):
			if position < row_cutoffs[k]:
				first_row = k
				break
		first_col = y[first_row].find(word)
		if first_col + len(word) <= len(y[first_row]):
			second_row = first_row
			second_col = first_col + len(word)
		else:
			second_row = first_row + 1
			second_col = len(word) - (len(y[first_row]) - first_col)
		return [first_row + 1, first_col + 1, second_row + 1, second_col]
	except ValueError:
		position = vertical_search.index(word)
		row_cutoffs = []
		z = 0
		for i in range(y2_rows):
			row_cutoffs.append(len(y2[i])+z)
			z += len(y2[i])
		first_row = 0
		second_row = 0
		second_col = 0
		for k in range(len(row_cutoffs)):
			if position < row_cutoffs[k]:
				first_row = k
				break
		first_col = y2[first_row].find(word)
		if first_col + len(word) <= len(y2[first_row]):
			second_row = first_row
			second_col = first_col + len(word)
		else:
			second_row = first_row + 1
			second_col = len(word) - (len(y2[first_row]) - first_col)
    	return [first_col + 1, first_row + 1, second_col, second_row + 1]

def flip_text(text):
	new_text = []
	cols = len(max(text))
	rows = len(text)
	for i in range(cols):
		temp_row = []
		for j in range(rows):
			try:
				temp_row.append(text[j][i])
			except IndexError:
				temp_row.append(" ")
		new_text.append("".join(temp_row))
	return new_text
