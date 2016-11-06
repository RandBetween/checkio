def check_pangram(text):
    text = text.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter not in text:
            return False
    return True
