def boxBlur(image):
    lenRow = len(image[0])
    lenCol = len(image)
    new=[]
    row=[]
    for j in range(3,lenCol+1):
        for i in range(3,lenRow+1):
            temp=[k[i-3:i] for k in image[j-3:j]]
            row.append(sum(sum(i) for i in temp)//9)
        new.append(row)
        row=[]
    return new

#commented Eddition. 
def boxBlur(image):
    lenRow = len(image[0]) #row count
    lenCol = len(image) #column count
    new=[] #to keep the final list after doing the work
    row=[] #to keep row value temp - append to new and reset
    # first loop will go from row 3 to till last
    # second loop will go from column 3 to till last
    for j in range(3,lenCol+1):
        for i in range(3,lenRow+1):
            #store temp. selected arry out of image for the math
            temp=[k[i-3:i] for k in image[j-3:j]]
            #total sum- then avg then append
            row.append(sum(sum(i) for i in temp)//9)
        #append row because as loop start again it will be another list in our final list
        new.append(row)
        row=[]
    return new
