def checkio(text):
    text = text.lower()
    text_list = list(''.join(e for e in text if e.isalpha()))
    text_list.sort(reverse=True)
    count = 0
    frequent = ""
    for letter in text_list:
        if text_list.count(letter) >= count:
            count = text_list.count(letter)
            frequent = letter
    return frequent
