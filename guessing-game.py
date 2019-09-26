import random

targetNum = random.randint(1,100)
print("pick a number between 1 and 100. Try to guess the number")
guesses = []

while True:
    guess = int(input("Enter a number between 1 and 100: \n"))

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100: \n")
        continue

    elif guess == targetNum:
        print("Wow! So good! You guessed it!")
        break    
    else:
        guesses.append(guess)
    
    if guess > targetNum:
        print("too high")
    elif guess < targetNum:
        print("too low")
