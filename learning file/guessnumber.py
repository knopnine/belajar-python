# guess tthe number game
import random
print('Hello, what is your name?')
name=input("enter your name here :")

print('\nWell ' + name +',i am thinking a number beween 1 and 20, \nTake a guess. \n')
secretNumber = random.randint(1,20)

print('DEBUG : the secret number is ' + str(secretNumber))

for guessTaken in range(1,7):
    print('Guess the number')
    guess=int(input())

    if guess<secretNumber:
        print('that is too low, guess the number again')
    elif guess>secretNumber:
        print('that is too high, guess the number again')
    else:
        break #condition when guess number is correct

if guess == secretNumber:
    print('good job, you are correct.')
else:
    print('my secret number is ' + str(secretNumber) +', \n good luck guessing again later.')