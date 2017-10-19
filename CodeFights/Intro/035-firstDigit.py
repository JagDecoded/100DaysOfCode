def firstDigit(inputString):
    for i in inputString:
        if i.isdigit():
            return i
    # return [i for i in inputString if i.isdigit()][0]
