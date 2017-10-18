def chessBoardCellColor(cell1, cell2):
    #return sum(ord(i) for i in cell1)%2 == sum(ord(i) for i in cell2)%2
    return sum(ord(i) for i in cell1+cell2)%2 == 0
