#Given the string, check if it is a palindrome.

def checkPalindrome(inputString):
    return True if inputString==inputString[::-1] else False
