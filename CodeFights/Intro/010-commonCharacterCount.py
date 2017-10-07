#Given two strings, find the number of common characters between them.

def commonCharacterCount(a, b):
    # return sum(min(a.count(i),b.count(i)) for i in set(a))
    total=0
    for i in a:
        if i not in done:
            total=total+min(a.count(i),b.count(i))
            done.append(i)
    return total
