def count_words(text, words):
    text = text.lower()
    return len([x for x in words if x in text])
