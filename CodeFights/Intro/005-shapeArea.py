def shapeArea(n):
    total=0
    for i in range(1,n+1):
        if i <3:
            total=total+i*i
        else:
            total=total+i*2+(i-2)*2
    return total
