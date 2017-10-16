def avoidObstacles(inputArray):
    jump = max(inputArray)+1
    for i in range(1,jump+1):
        if all(j%i!=0 for j in inputArray):
            return i
