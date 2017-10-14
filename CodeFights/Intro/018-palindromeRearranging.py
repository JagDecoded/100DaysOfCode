def palindromeRearranging(inputString):
    return sum(1 for i in set(inputString) if inputString.count(i)%2==1)<2
