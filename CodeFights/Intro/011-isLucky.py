#Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky
#if the sum of the first half of the digits is equal to the sum of the second half.
#Given a ticket number n, determine if it's lucky or not.

def isLucky(n):
    n= str(n)
    if sum(int(i) for i in n[:len(n)//2]) == sum(int(i) for i in n[len(n)//2:]):
        return True
    else:
        return False
