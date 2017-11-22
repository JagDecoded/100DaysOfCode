def digitDegree(n):
    count=0
    while n>9:
        count+=1
        n = sum(int(i) for i in str(n))
    return count
