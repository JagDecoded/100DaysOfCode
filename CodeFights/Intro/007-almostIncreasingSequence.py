#Given a sequence of integers as an array, determine whether it is possible to obtain a
#strictly increasing sequence by removing no more than one element from the array.

def almostIncreasingSequence(sequence):

    '''for i in range(len(array)-1):
        if array[i]>=array[i+1]:
            array.pop(i)
            break
    for i in range(len(array)-1):
        if array[i]>=array[i+1]:
            return False
    return True'''

    count_decreasing_sq = 0
    for i in range(len(sequence) - 1):
        if sequence[i+1] <= sequence[i]:
            count_decreasing_sq += 1
            if (i >= 1) and (sequence[i+1] <= sequence[i-1]):
                if (len(sequence) - 2 > i) and (sequence[i+2] <= sequence[i]):
                    count_decreasing_sq += 1
        if count_decreasing_sq > 1:
            return False
    return True
