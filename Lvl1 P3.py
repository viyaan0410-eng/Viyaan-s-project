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




print ('GGGGG','U   U','EEEEE','SSSSS','SSSSS', sep = ' | ')
print ('G    ','U   U','E    ','S    ','S    ', sep = ' | ')
print ('G  GG','U   U','EEEEE','SSSSS','SSSSS', sep = ' | ')
print ('G   G','U   U','E    ','    S','    S', sep = ' | ')
print ('GGGGG','UUUUU','EEEEE','SSSSS','SSSSS', sep = ' | ')

print('\v')

type_effect('x----------x----------x----------x----------x----------x----------x')

print('\v')

# User Guess

done = False

attempts = 0

type_effect ('I picked a number between 1 to 100, can you guess? ')

while not done:
    guess = int (input ('Guess the Number: '+'\n'))
    attempts = attempts + 1

    if guess > n:
         type_effect ('My number is smaller then that number! \n')

    if guess < n:
         type_effect ('My number is larger than that number! \n')

    if guess == n:
         type_effect ('You are soo correct!! ')
         print ('attempts number:', attempts )
         done = True


print ('\v')

type_effect('x----------x----------x----------x----------x----------x----------x')

print('\v')

# Computer

done = False

type_effect ('Now your chance, pick a number between 1 to 100')
type_effect ('Click enter when you are ready.')

input ()
guess = 0
attempts = 0
guess_step = 10; 
prev_answer = ''

while not done:
    
    answer =  input (type_effect ('Is it '+ str(guess) + '? (y = Yes, s = smaller than that, l = larger than that) \v'))
    attempts = attempts + 1 

    if attempts > 1: 
      if answer != prev_answer:
       
        guess_step = guess_step - 1
      
    prev_answer = answer
  
    if answer.lower() == 's':
        guess = guess - guess_step
    
    if answer.lower() == 'l':
        guess = guess + guess_step
    
    if answer.lower() == 'y':
      type_effect ('Bingo, I got it.')
      print ('The number of attempts I took:', attempts )
      done = True

print ('\v')

type_effect('x----------x----------x----------x----------x----------x----------x')

print('\v')


# Binary 

type_effect ('Lets play a faster version!')
type_effect ('Click enter when you are ready.')

input ()

guess = 0
done = False
low = 0
high = 100
guess_step = 0
attempts = 0

while not done:
    guess = round((low + high)/2)
    answer = input (type_effect ('Is it '+ str(guess) + '? (y = Yes, s = smaller than that, l = larger than that) \v'))
    attempts = attempts + 1 

    if answer.lower() == 's':
        high = guess
    
    if answer.lower() == 'l':
        low = guess
    
    if answer.lower() == 'y':
      type_effect('Bingo, I got it.')
      print('I took ', attempts, 'attempts to guess it.')
      done = True
    
print('\v')

type_effect('x----------x----------x----------x----------x----------x----------x')

print('\v')

# HangMan Version

type_effect('Now lets play the hangman version!')

print ('\v')

words = ("apple", "orange", "banana", "coconut", "pineapple",
    "ant", "baboon", "badger", "bat", "bear", "beaver", "camel",
    "cat", "clam", "cobra", "cougar", "coyote", "crow", "deer",
    "dog", "donkey", "duck", "eagle", "ferret", "fox", "frog",
    "goat", "goose", "hawk", "lion", "lizard", "llama", "mole",
    "monkey", "moose", "mouse", "mule", "newt", "otter", "owl",
    "panda", "parrot", "pigeon", "python", "rabbit", "ram", "rat",
    "raven", "rhino", "salmon", "seal", "shark", "sheep", "skunk",
    "sloth", "snake", "spider", "stork", "swan", "tiger", "toad",
    "trout", "turkey", "turtle", "weasel", "whale", "wolf", "wombat", "zebra")

answer = random.choice(words)

hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")}

def display_man(wrong_guesses):
    type_effect("**********")
    for line in hangman_art[wrong_guesses]:
        type_effect(line)
    type_effect("**********")

def display_hint(hint):
    type_effect(" ".join(hint))

def display_answer(answer):
    type_effect(" ".join(answer))

def main():
    
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            type_effect("Invalid input")
            continue

        if guess in guessed_letters:
            type_effect(f"'{guess}' is already guessed")
            continue

        guessed_letters.add(guess)


        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            type_effect("YOU WIN!")
            is_running = False
        
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            type_effect("YOU LOSE!")
            is_running = False

type_effect('Instruction:')
type_effect(' 1. The word is ' + str(len(answer)) + ' letters long.')
type_effect(' 2. You have 6 chances.')
type_effect('The word can be a animal, fruit.')
print ('\v')

if __name__ == '__main__':
    main()


print('\v')

print ('EEEEE', 'N   N', 'DDDDD   ', sep = '  | ')
print ('E    ', 'NN  N', 'D    D  ', sep = '  | ')
print ('EEEEE', 'N N N', 'D     D ', sep = '  | ')
print ('E    ', 'N  NN', 'D    D  ', sep = '  | ')
print ('EEEEE', 'N   N', 'DDDDD   ', sep = '  | ')

print('\v')

type_effect('x----------x----------x----------x----------x----------x----------x')