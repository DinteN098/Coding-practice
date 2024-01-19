test = [0,50, 11, 33, 21, 40, 50, 40, 40, 21]

def deDuplicate(lst):
    maxValue = 0

    #test case if list is empty
    if len(lst) == 0: 
        return "The list is empty."
    
    #test case if list has a string
    for i in range(len(lst)):
        if type(lst[i]) == type(""):
           return "There is a string in the list"

    #for loop to find greatest number
    for i in range(len(lst)):
        if lst[i] > maxValue:
            maxValue = lst[i]
    
    #list to keep track of what numbers are are repeated
    countList = [0 for i in range(0, maxValue+1)]
    #list from 0 to the greatest number in lst
    indexOfVal = [i for i in range(0, maxValue+1)]

    #checking what numbers from the lst are in the the indexOfVal
    for i in range(len(lst)):
        for j in range(len(indexOfVal)):
            if lst[i] == indexOfVal[j]:
                countList[j] += 1

    
    deduplicated_list = []

    #adding numbers that don't have a value of zero in countlist to the deduplicated list
    for i in range(len(countList)):
        if countList[i] != 0:
            deduplicated_list.append(indexOfVal[i])

    return deduplicated_list

print(deDuplicate(test))
