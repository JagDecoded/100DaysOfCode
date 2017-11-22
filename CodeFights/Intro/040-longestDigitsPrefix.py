def longestDigitsPrefix(inputString):
    digit=[]
    for i in inputString:
        if i.isdigit():
            digit.append(i)
        else:
            break
    return ''.join(digit)
