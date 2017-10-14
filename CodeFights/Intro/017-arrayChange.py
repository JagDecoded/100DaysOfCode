def arrayChange(inputArray):
    count =0
    for i in range(1,len(inputArray)):
        a, b = inputArray[i-1] ,inputArray[i]
        if a>=b:
            count=count+(a-b+1)
            inputArray[i]=a+1
    return count
