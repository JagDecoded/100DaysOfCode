def makeArrayConsecutive2(statues):
    return max(statues)-min(statues)-len(statues)+1
    #return sum(1 for i in range(min(statues),max(statues)) if i not in statues)
    
