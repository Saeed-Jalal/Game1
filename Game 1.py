import random
print("Holla, What is your name. ")
#input is required
name = input()
print("Well, Do you want to check your IQ level? " + name + ", I am thinking of a number between 6 and 56.")


secretNumber = random.randint(5, 20 )
for guessesTaken in range(1,5):
    print("Start by Taking a guess in Interger.")
#int(input) is required
    guess = int(input())
    if guess < secretNumber:
        print("Your guessing too low. ")
    elif guess > secretNumber:
        print("OMG...Your are guessing too high. ")
    else:
        break # This condition is for the correct guess!
if guess == secretNumber:
    print("Wooowwww " + name + " you guessed secret number in " + str(guessesTaken) + " Gusses! ")
#str() required
else:
    print("Noooppppe. The secret number i was thinking of was " + str(secretNumber))


