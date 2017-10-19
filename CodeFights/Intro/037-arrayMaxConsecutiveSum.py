def arrayMaxConsecutiveSum(inputArray, k):
    maximum = sum (inputArray[:k])
    pre =maximum
    for i in range(1,len(inputArray)-k+1):
        pre =pre-inputArray[i-1]+inputArray[i+k-1]
        if pre > maximum:
            maximum = pre
    return maximum
