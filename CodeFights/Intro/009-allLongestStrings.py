#Given an array of strings, return another array containing all of its longest strings.

def allLongestStrings(array):
    long= max(len(i) for i in array)
    new=[i for i in array if len(i)==long]
    return new
