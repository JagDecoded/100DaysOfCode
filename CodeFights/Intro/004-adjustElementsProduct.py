#Given an array of integers,
#find the pair of adjacent elements that has the largest product and return that product.

def adjacentElementsProduct(array):
    return max(array[i]*array[i+1] for i in range(len(array)-1))
