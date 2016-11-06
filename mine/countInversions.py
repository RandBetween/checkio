def count_inversion(sequence):
    sequence = list(sequence)
    i, count = 0, 0
    while i < (len(sequence) - 1):
        if sequence[i] > sequence[i+1]:
            sequence[i], sequence[i+1] = sequence[i+1], sequence[i]
            count += 1
            i = 0
        else:
            i += 1
    return count
