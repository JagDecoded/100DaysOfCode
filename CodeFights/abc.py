def divisorsPairs(sequence):

    result = 0-len(sequence)

    for i in range(len(sequence)):
        for j in range(len(sequence)):
            if sequence[i] % sequence[j] == 0 or sequence[j] % sequence[i] == 0and i!=j:
                result += 1
                print(sequence[i],sequence[j])

    return result
sequence = [1, 3, 2]
print(divisorsPairs(sequence))
