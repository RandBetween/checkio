def checkio(message):
    new_message = [chr(int(bin(x)[2:len(bin(x))-1], 2)) for x in message if reduce(lambda i,j: i+j, [int(z) for z in bin(x)[2:len(bin(x))-1]]) % 2 == int(bin(x)[len(bin(x))-1:])]
    return "".join(new_message)
