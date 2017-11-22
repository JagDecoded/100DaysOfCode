def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1+weight2 <= maxW:
        return value1+value2
    elif weight1 <= maxW and (value1 >value2 or weight2>maxW):
        return value1
    elif weight2 <= maxW and (value2 >value1 or weight1>maxW):
        return value2
    elif value1 == value2:
        return value1
    else:
        return 0
