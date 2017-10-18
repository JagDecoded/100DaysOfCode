def minesweeper(matrix):
    new=[]
    row=[]
    lenRow=len(matrix)
    lenCol=len(matrix[0])
    for i in matrix:
        i.insert(0,False)
        i.append(False)
    matrix.insert(0,[False for i in range(lenCol+2)])
    matrix.insert(lenRow+1,[False for i in range(lenCol+2)])
    for i in range(1,lenRow+1):
        for j in range(1,lenCol+1):
            total=sum(matrix[i-1][j-1],
               matrix[i-1][j],
               matrix[i-1][j+1],
               matrix[i][j-1],
               matrix[i][j+1],
               matrix[i+1][j-1],
               matrix[i+1][j],
               matrix[i+1][j+1])
            row.append(total)
        new.append(row)
        row=[]
    return new
