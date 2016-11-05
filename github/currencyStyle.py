def checkio(text):
    text_list = text.split(" ")
    new_str = []
    for word in text_list:
        word_str = []
        if len(word) != 0:
            if word[0] == "$":
                for i in range(len(word)-2):
                    if word[i] == "." or word[i] == ",":
                        try:
                            if word[i+1].isdigit() and word[i+2].isdigit() and word[i+3].isdigit(): word_str.append(",")
                            elif word[i+1].isdigit() and word[i+2].isdigit(): word_str.append(".")
                            else: word_str.append(word[i])
                        except:
                            word_str.append(".")
                    else: word_str.append(word[i])
                word_str.append(word[len(word)-2])
                word_str.append(word[len(word)-1])
            else:
                for letter in word:
                    word_str.append(letter)
        new_str.append("".join(word_str))
    return " ".join(new_str)
