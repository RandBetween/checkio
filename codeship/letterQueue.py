def letter_queue(commands):
    queue = ""
    for command in commands:
        if command.startswith("PUSH"):
            queue += command[-1]
        else:
            try:
                queue = queue[1:]
            except IndexError:
                continue
    return queue
