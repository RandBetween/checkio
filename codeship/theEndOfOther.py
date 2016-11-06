def checkio(words_set):
    words_list = list(words_set)
    words_list.sort(key = len)
    for i in range(len(words_list)-1):
        for j in range(i+1,len(words_list)):
            if words_list[i] == words_list[j][len(words_list[j]) - len(words_list[i]):]:
                return True
    return False
