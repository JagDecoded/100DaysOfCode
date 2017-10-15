def arrayMaximalAdjacentDifference(inputArray):
    #return max(abs(inputArray[i]-inputArray[i-1])for i in range(1,len(inputArray)))
    #but here is the efficient way, we dont need to count the len everytime.
    a=len(inputArray)
    return max(abs(inputArray[i]-inputArray[i-1])for i in range(1,a))
