from math import floor, log2 

testList = [0,1,2,3,4]
find = 0

def binarySearch(lst, n):

    #test cases for empty lists and lists with strings
    if len(lst) == 0:
        return "List is empty."

    if type(n) == type(""):
        return "I only accept integers."

    checks_should_take = floor(log2(len(lst)))+1

    checks = 0
    
    for i in range(0,checks_should_take):
        if len(lst) == 0:
            break

        middleIndex = floor(len(lst) / 2)
        checks += 1

        #applying binary search to slice the list until we find 'n'
        if lst[middleIndex] == n:          
            return (f"Number found after {checks} checks")
        elif lst[middleIndex] < n:
            lst = lst[middleIndex+1:]
        elif lst[middleIndex] > n:
            lst = lst[:middleIndex]

    #if the for loop ends and runs the last line in the function then it means that it didn't find the number
    return "“Fail to find the input number…"

print(binarySearch(testList, find))