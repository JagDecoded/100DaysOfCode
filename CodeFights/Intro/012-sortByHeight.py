def sortByHeight(a):

    '''order = sorted(i for i in a if i !=-1)
    for i, n in enumerate(a):
        if n==-1:
            order.insert(i,n)
    return order
    '''

    for i in range(len(a)):
        for j in range(len(a)):
            if a[j] != -1 and a[i]!=-1 and a[j]>a[i]:
                a[j], a[i] = a[i], a[j]
    return a
