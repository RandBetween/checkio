def left_join(phrases):
    str_p = ",".join(phrases)
    return str_p.replace("right", "left")
