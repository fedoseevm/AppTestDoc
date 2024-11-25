def compressTheSequence(sequence):
    if not sequence: return ""
    if len(sequence) == 1: return sequence

    result = ""
    letterCounter = 1
    for i in range(len(sequence) - 1):
        if (sequence[i] == sequence[i + 1]):
            letterCounter += 1
        else:
            if letterCounter > 1:
                result += str(letterCounter) + sequence[i]
            else:
                result += sequence[i]
            letterCounter = 1

    if letterCounter > 1:
        result += str(letterCounter)
    result += sequence[i + 1]

    return result
