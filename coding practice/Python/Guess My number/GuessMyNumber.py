import math

n = int(input("Enter n: ")) #how many numbers will the machine have to guess
formula = math.floor(math.log2(n)) + 1 #how many attempts will take to guess the number
numList = [i for i in range(0,n)] #where all the numbers will be stored
possibleGuesses = formula

print("Welcome to Guess My Number!") 
print(f"Please think of a number between 0 and {n-1}.")

for i in range(0, possibleGuesses):
    #the best way to win the game is to always guess on the middle
    middleIndex = math.floor(len(numList) / 2)
    middleOfList = numList[middleIndex]
    guess = middleOfList
    print(f"Is your number: {guess}")
    print("Please enter C for correct, H for too high, or L for too low.")
    answer = input("Enter your response (H/L/C): ").lower()
    #if c then the code guessed correctly
    if answer == "c":
        print("Thank you for playing Guess My Number!")
        break
    #else if the number is less than my guess then slice the list to the left
    elif answer == "l":
        numList = numList[:middleIndex]
    elif answer == "h":
    #else if the number is more than my guess then slice the list to the right
        numList = numList[middleIndex + 1:]
    else:
        print("Not an option")
        break