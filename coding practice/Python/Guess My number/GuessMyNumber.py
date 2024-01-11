import math #using the log function from the math python library

#how many numbers will the machine have to guess
n = int(input("Enter n: ")) 

#option that will decide when the game is done or how to slice the array
options = ["c", "h", "l"]

#while loop to make sure user inputs correct number
while n <= 0:
    n = int(input("Enter a positive integer for n: "))
    
    #breaks loop once the user inputs positive integer
    if n > 0:
        break

    #if positive integer is given then keep asking
    else: continue

#using formula to determine how many guesses it should take the machine to guess correct number (not necessary)
possibleGuesses = math.floor(math.log2(n)) + 1

numberList = [i for i in range(0, n)]

print("Welcome to Guess My Number!")
print(f"Please think of a number between 0 and {n-1}.")

#run for loop for the amount of times in the possible guesses
for i in range(0, possibleGuesses):

    #find middle index on the list
    middleIndex = math.floor(len(numberList) / 2)

    middleOfList = numberList[middleIndex]

    guess = middleOfList
    print(f"Is your number: {guess}?")
    print("Please enter C for correct, H for too high, or L for too low.")

    answer = input("Enter your response (H/L/C): ").lower()

    #run while loop until user inputs one of the options available
    while answer not in options:
        answer = input("Enter your response (H/L/C): ").lower()

    #if answer is correct then print win message
    if answer == options[0]:
        print("Thank you for playing Guess My Number!")
        break

    #else if answer too high then slice list to left of guess
    elif answer == options[1]:
        numberList = numberList[:middleIndex]
    #else if answer too low then slice list to right of guess
    elif answer == options[2]:
        numberList = numberList[middleIndex+1:]
