def addBorder(picture):
    border =['*'*(len(picture[0])+2),'*'*(len(picture[0])+2)]
    for i in picture[::-1]:
        border.insert(1,'*'+i+'*')
    return border
