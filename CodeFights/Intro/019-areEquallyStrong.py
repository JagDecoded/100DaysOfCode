def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    #innovative way:
    # return sorted(yourLeft,yourRight) == sorted(friendsLeft, friendsRight)
    if yourLeft == friendsLeft or yourLeft == friendsRight:
        if yourRight == friendsLeft or yourRight == friendsRight:
            return True
    return False
