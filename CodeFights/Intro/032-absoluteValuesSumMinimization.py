#find the median
def absoluteValuesSumMinimization(a):
    # return a[len(a)//2 - (len(a)%2==0)]
    return a[len(a)//2] if len(a)%2==1 else a[(len(a)//2)-1]
