import sys
import time

def type_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  
    return ''



import datetime as dt


chances = int(50)
type_effect('Are you here for the Job Interview?\v')
type_effect(' If yes then, first answer the questions to join the list!\v')
type_effect(f'Chances: {chances}%\v')
# 'f' is used to remove the delay
type_effect( 'Your chances are low because you did not look confident when you entered.\v')
answer = input(type_effect('What is [(80 x 4) ÷ 8] ? \v '))

if answer.lower() == '40':
    type_effect('You are smart, This was just a warm up. Heheheheh!')
    chances = chances + 10
    print ('Chances:', chances, ' %\v')
else:
    type_effect('The chances to get this job, just got low!')
    chances = chances - 25
    print ('Chances:', chances, ' %\v')

answer = input(type_effect('Give me a 8 letter word with atleast 3 vowels.\v'))

if len(answer) == 8:
    count_a = answer.count('a')
    count_e = answer.count('e')
    count_i = answer.count('i')
    count_o = answer.count('o')
    count_u = answer.count('u')
    count_vowels = count_a + count_e + count_i + count_o + count_u

    if count_vowels > 3:
        type_effect('Trying more vowels..... but No!')
        chances = chances - 25
        print ('Chances:', chances, ' %\v')

    elif count_vowels < 3:
        type_effect ('Trying to act smart...... but No!')
        chances = chances - 25
        print ('Chances:', chances, ' %\v')

    else:
        type_effect('You are good. Hehehehe, but this was the 2nd warm upp')
        chances = chances +10
        print ('Chances:', chances, ' %\v')

else:
    type_effect('Stop.... WASTING....MY TIME!!!!!!!  but this was the 2nd warm upp. hehhehehehhehhehhehhehhhheh')
    chances = chances - 25
    print ('Chances:', chances, ' %\v')



sentence = input("ok, tell me a sentence ending in 'dispite of that, im still smart' (no question please)\n")

if sentence.endswith('dispite of that, im still smart'):
    type_effect("Haven't you learnt about punctuations?")
elif sentence.endswith('dispite of that, im still smart.'):
    len_first = sentence.find(' ')
    if len_first < 5:
        type_effect("The first word in the sentence is too short.")
        chances = chances + 10
        print ('Chances:', chances, ' %\v')
else:
    type_effect("The chances to get this job, just got low!")
    chances = chances - 25
    print ('Chances:', chances, ' %\v')

print('\v')   

if chances > 0:
    
    type_effect('You have joined the list. While you were waiting in the list, you felt super thirsty, so you asked a person to bring you some water. While drinking water You squished the plastic bottle too hard and all the water fell on your suit. So you ran back home and changed your suit. But when you returned the interview timing were over. So, you asked the professors assistant, "When is the next appointment?",The assistant says: \v ')
    type_effect ('Ok, pick your preferred appointment time for tomorrow. (A/B/C/D)')
    print('A. 8 mins past midnight', 'B. 16 mins before sunrise', sep= '\t') 
    print('C. 24 mins before noon', 'D. 48 mins after sunset', sep= '\t')
    appointment = input(type_effect('Select your slot (A/B/C/D)\v'))
    
    if appointment == 'A':
        type_effect("Caution, Prof. may be sleepy and might not hear your intro.")
    elif appointment == 'B':
        type_effect("Warning, Prof. may be doing his morning exercise.")
    elif appointment == 'C':
        type_effect("Beware, Prof. may be eating a salad (no one disturbs prof , when he is eating his salad.).")
    else:
        type_effect("Caution, Prof. may be sleepy and might not hear your intro.")
    
    type_effect('You arrive tomorrow, but u see 20 people before you, so you wait by reading a book, they your chance comes, there was a girl who told you "The Previous person disapointed the Prof, So he is Grumpy, be careful!". \v')
    type_effect('You enter and see a 40-50 year man, he tells you to sit down, you sit.')
    type_effect('He asks you what type of Questions do you want? [A,B,C] ')
    print('A = Math','B = GK', 'C = Sports, but there will be a timer this time.', sep= '\t')
    Questions = input(type_effect('Select your slot (A/B/C)\v'))
    ct1 = dt.datetime.now()

    if Questions == 'A':
        type_effect('Make sure to bring a pen and paper\v')
        type_effect('Solve these 5 questions within 500 seconds. \v')
        Aq1 = int(input(type_effect('Solve for x: 4x - 7 = 2x + 15')))
        if Aq1 == 11:
            type_effect('Good but it is going to get harder! hehehehehehe\v')
        else:
            type_effect('Chee, This was the easiest question.\v')

        Aq2 = int(input(type_effect('A shop sells notebooks in packs of 6. If Rohan buys 4 packs and gives away 9 notebooks, how many does he have left?\v')))
        if Aq2 == 15:
            type_effect('Good but it is going to get harder! hehehehehehe\v')
        else: 
            type_effect('Bruh!\v')

        Aq3 = int(input(type_effect('20(%) of 150?\v')))
        if Aq3 == 30:
            type_effect('Good but it is going to get harder! hehehehehehe\v')
        else:
            type_effect('Bruh!\v')

        Aq4 = str(input(type_effect('Rectangle 9 cm x 5 cm, Find area.\v')))
        if Aq4 == '45 cm':
            type_effect('Good but it is going to get harder! hehehehehehe\v')
        else: 
            type_effect('Bruh!\v')
        Aq5 = int(input(type_effect('Find for x: 2(x + 3) = 16\v')))
        if Aq5 == 5:
             type_effect('Good but it is going to get harder! hehehehehehe\v')
        else: 
            type_effect('Bruh!\v')
        
        ct2 = dt.datetime.now()    
        diff = ct1 - ct2
        if diff.seconds < 500:
         type_effect('Dammmm...., Im impressed, You are accepted to become a janitor!, salary = 5$ per hour, with every 2nd Saturday a off. ' )
         type_effect('You took', diff.seconds, 'seconds')

        else:
            type_effect('You are not accepted!, Thx for wasting my time 😊')
            print('You took', diff.seconds, 'seconds')

    elif Questions == 'C':
        type_effect('Solve these 5 questions within 500 seconds. \v')

        Cq1 = input(type_effect('Which country invented cricket?\v'))
        if Cq1 == 'England':
              type_effect('Good but it is going to get harder! hehehehehehe\v')
        else:
            type_effect('Chee, This was the easiest question.\v')
        
        Cq2 = int(input(type_effect('How many rings are there in the Olympic symbol?\v')))
        if Cq2 == 5:
            type_effect('Good but it is going to get harder! hehehehehehe\v')
        else: 
            type_effect('Bruh!\v')
        
        Cq3 = input(type_effect('Which sport uses the term "love" for zero?\v'))
        if Cq3 ==  'Tennis':
            type_effect('Good but it is going to get harder! hehehehehehe\v')
        else:
            type_effect('Bruh!\v')
        
        Cq4 = input(type_effect('Which country has won the most Olympic gold medals overall?\v'))
        if Cq4 == 'United States':
            type_effect('Good but it is going to get harder! hehehehehehe\v')
        else: 
            type_effect('Bruh!\v')
        Cq5 = int(input(type_effect('In which year did Neymar Jr retire from international football?\v')))
        if Cq5 == 2026:
            type_effect('Good but it is going to get harder! hehehehehehe\v')
        else: 
            type_effect('Bruh!\v')
                
        ct2 = dt.datetime.now()    
        diff = ct1 - ct2
        if diff.seconds < 500:
            type_effect('Dammmm...., Im impressed, You are accepted to become a janitor!, salary = 5$ per hour, with every 2nd Saturday a off. ' )
            type_effect('You took', diff.seconds, 'seconds')
        else:
            type_effect('You are not accepted!, Thx for wasting my time 😊')
            print('You took', diff.seconds, 'seconds')


    else:
         type_effect('Solve these 5 questions within 500 seconds. \v')
        
         Bq1 = input(type_effect('Which is the smallest country in the world by area?\v'))
         if Bq1 == 'Vatican City':
            type_effect('Good but it is going to get harder! hehehehehehe\v')
         else:
            type_effect('Chee, This was the easiest question.\v')
                
         Bq2 = input(type_effect('What is the chemical symbol for gold?\v'))
         if Bq2 == 'Au':
            type_effect('Good but it is going to get harder! hehehehehehe\v')
         else: 
            type_effect('Bruh!\v')
                
         Bq3 = input(type_effect('What is the currency of Russia?\v'))
         if Bq3 == 'Ruble':
            type_effect('Good but it is going to get harder! hehehehehehe\v')
         else:
            type_effect('Bruh!\v')
                
         Bq4 = input(type_effect('What is the capital of Australia?\v'))
         if Bq4 == 'Canberra':
            type_effect('Good but it is going to get harder! hehehehehehe\v')
         else: 
            type_effect('Bruh!\v')
         Bq5 = int(input(type_effect('In which year did the titanic sink?\v')))
         if Bq5 == 1912:
            type_effect('Good but it is going to get harder! hehehehehehe\v')
         else: 
            type_effect('Bruh!\v')
                        
         ct2 = dt.datetime.now()    
         diff = ct1 - ct2
         if diff.seconds < 500:
            type_effect('Dammmm...., Im impressed, You are accepted to become a janitor!, salary = 5$ per hour, with every 2nd Saturday a off. ' )
            type_effect('You took', diff.seconds, 'seconds')
                
         else:
            type_effect('You are not accepted!, Thx for wasting my time 😊')
            print('You took', diff.seconds, 'seconds')

else: 
   type_effect('You failed because you failed the prof. assistant questions.')


print('\v')

print ('EEEEE', 'N   N', 'DDDDD   ', sep = '  | ')
print ('E    ', 'NN  N', 'D    D  ', sep = '  | ')
print ('EEEEE', 'N N N', 'D     D ', sep = '  | ')
print ('E    ', 'N  NN', 'D    D  ', sep = '  | ')
print ('EEEEE', 'N   N', 'DDDDD   ', sep = '  | ')

print('\v')

type_effect('x----------x----------x----------x----------x----------x----------x')