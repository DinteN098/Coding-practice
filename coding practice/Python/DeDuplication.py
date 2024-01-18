test = [50, 11, 33, 21, 40, 50, 40, 40, 21+1]

def deDuplication(lst):
    
    #test case if list is empty
    if len(lst) == 0: 
        return "List is empty"
    
    #test case if list has a string
    for i in range(len(lst)):
        if type(lst[i]) == type(""):
           return "There is a string in the list"

    #using a bubble sort algorithm to sort the list
    for i in range(1, len(lst)):
        for j in range(0,len(lst)-1):
            if lst[j] > lst[j+1]:                
                tempNum = lst[j+1]
                lst[j+1] = lst[j]
                lst[j] = tempNum

    # no duplicate numbers and sorted list
    newList = []

    # removing duplicates
    for i in lst:
        if i not in newList:
            newList.append(i)

    return newList


print(deDuplication(test))


