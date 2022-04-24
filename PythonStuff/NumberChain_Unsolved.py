# Initial variable to track game play
user_play = "y"
startNumber = 0
# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    x = int(input("how many number do you want to loop through?"))
    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for numbers in range(startNumber, int(x) + startNumber):
        

        # Print each number in the range
       print(numbers)
    startNumber = startNumber + int(x)
    # Once complete...
    user_play = input("Continue: (y)es or (n)o? ")

    # bonus
    