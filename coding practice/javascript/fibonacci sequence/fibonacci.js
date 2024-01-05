function fibonacci(n){
    //list where fibonacci number will be
    var list = [];

    // if the amount of fibonacci numbers are equal to 1 then add 0 to the list
    if (n === 1){
        list.push(0)
        return list
    }

    //else if the amount of fibonacci numbers are equal to 2 then add 0 and 1 to the list
    else if (n === 2) {
        list.push(0)
        list.push(1)
        return list
    }

    /*else if the amount of fibonacci numbers are more than two then add 0 and 1 to the 
    list and run a for loop for every number of fibonacci numbers asked*/
    else {
        list.push(0)
        list.push(1)

        /*we use this for loop to apply a sliding window that sums the last number in the list
        with the one before it and add that sum to the end of the list and repeat until 
        the amount of numbers in a list is the same as the one asked from user*/
        for(var i = 0; i < n; i++){
            var a = i
            var b = i + 1
            list.push(list[a] + list[b])
            if (list.length === n){
                return list
            }
                
        }
    }


}

console.log(fibonacci(20))