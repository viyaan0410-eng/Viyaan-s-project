import random 

n = random.randint (1,100)
import sys
import time

def type_effect(text, delay=0.05):
    for char in text:
         sys.stdout.write(char)
         sys.stdout.flush()
         time.sleep(delay)
         print()  



type_effect ('I picked a number between 1 to 100, can you guess: ')

attempts = 0

done = False

while not done:
    guess = int( input 'Guess the number: \v')
    attempts = attempts + 1

    if guess > n:
         type_effect ('My number is smaller then that number! \n')

    if guess < n:
         type_effect ('My number is larger than that number! \n')

    if guess == n:
         type_effect ('You are soo correct!! ')
         type_effect (Attempts number:, attempts )
         done = True


print ('\v')


type_effect ('Now your chance, pic a number between 1 to 100')

print ('\v')

done = False

attempts = 0

type_effect ('Click enter when you have choosen a number:')
input ()

guess = 1 
prev_answer = ''
guess_step = 10

while not done:
    # guess = round((low + high)/2)
    answer = input(type_effect('Is it '+ str(guess) + '? (y = Yes, s = smaller than that, l = larger than that) \n'))
    attempts = attempts + 1 

    if attempts > 1: 
      if answer != prev_answer:
        # guess_step = round(guess_step/2)
        guess_step = guess_step - 1
      
    prev_answer = answer
  
    if answer.lower() == 's':
        guess = guess - guess_step
    
    if answer.lower() == 'l':
        guess = guess + guess_step
    
    if answer.lower() == 'y':
      type_effect('You got it !!!')

      type_effect('I took ', attempts, 'attempts to guess it.')
      done = True



done = False
low = 0
high = 100
guess_step = 0
attempts = 0

while not done:
    guess = round((low + high)/2)
    answer = input('Is it '+ str(guess) + '? (y = Yes, s = smaller than that, l = larger than that) \n')
    attempts = attempts + 1 

    if answer.lower() == 's':
        high = guess
    
    if answer.lower() == 'l':
        low = guess
   