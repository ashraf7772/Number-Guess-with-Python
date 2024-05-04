import random
#now we make a random number
top = input("Enter a number: ")


if top.isdigit(): #checking if entered value is a number
    top = int(top)
#now we check if top is less than 0
    if top <= 0:
        print("You need to use a number more than 0")
        quit()
    else:
        rand = random.randint(0, top)
        totalGuesses = 0
        while True:
            totalGuesses += 1
            guess = input("Guess what the number is ") #the users guess
            if guess.isdigit(): #checking if entered value is a number
                guess = int(guess)
            else:
                print("has to be a number ")
                continue

            if guess == rand:
                print("correct ")
                break
            elif guess > rand:
                    print("too high")
            else:
                    print("too low")


print("Your total guesses were", totalGuesses, "guesses")






