def isIPv4Address(inputString):
    ip= inputString.split('.')
    #return len(ip)==4 and all(i.isnumeric() and 0<= i <= 256 for i in ip)
    if len(ip)!=4:
        return False
    for i in ip:
        if not i.isnumeric() or not 0<= int(i) <= 256:
            return False
    return True
