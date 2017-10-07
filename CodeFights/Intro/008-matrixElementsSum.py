def matrixElementsSum(matrix):
    #way 1
    '''
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                for k in range(i,len(matrix)):
                    matrix[k][j]=0
    return sum(m for n in matrix for m in n)
    '''
    #way 2
    matrix=zip(*matrix)
    total=0
    for i in matrix:
        for j in i:
            if j==0:
                break
            total=total+j
    return total
