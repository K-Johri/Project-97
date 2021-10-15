import random

print("Number guessing game")
number = random.randint(1,9)
chances = 0
print("Guess the number between 1 and 9")

while chances < 5:
    guess = int(input("Enter your guess"))

    if guess == number:
        print("You won")
        break

    elif guess < number:
        print("Your guess was too low. Enter a higher number than",guess)

    else :
     print("Your guess was too high. Enter a lower number than",guess)

chances += 1 
# Check whether the user guessed the correct number 

if not chances < 5: 
    print("YOU LOSE!!! The number is", number)