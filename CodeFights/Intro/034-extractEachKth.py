def extractEachKth(inputArray, k):
    # inputArray.insert(0,0)
    # return [ value for index,value in enumerate(inputArray) if index%k != 0]
    del inputArray[k-1::k]
    return inputArray
