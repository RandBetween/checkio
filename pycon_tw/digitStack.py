def digit_stack(commands):
    stack = []
    sum = 0
    for command in commands:
        phrase = command.split()
        if phrase[0] == "PUSH":
            stack.append(int(phrase[1]))
        elif phrase[0] == "POP":
            try:
                sum += stack.pop()
            except IndexError:
                continue
        elif phrase[0] == "PEEK":
            try:
                sum += stack[-1]
            except IndexError:
                continue
    return sum
