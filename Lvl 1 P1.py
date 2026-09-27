# Imports 
import time

# Title 

print ('PPPPP', 'Y   Y', 'TTTTT', 'H   H', 'OOOOO', 'N   N', sep = '  | ')
print ('P   P', ' Y Y ', '  T  ', 'H   H', 'O   O', 'NN  N', sep = '  | ')
print ('PPPPP', '  Y  ', '  T  ', 'HHHHH', 'O   O', 'N N N', sep = '  | ')
print ('P    ', '  Y  ', '  T  ', 'H   H', 'O   O', 'N  NN', sep = '  | ')
print ('P    ', '  Y  ', '  T  ', 'H   H', 'OOOOO', 'N   N', sep = '  | ')
print ('\v')

# Ask

player = input ('What is your name: ')

intrest = input ('\v What is your intrest: ')

school = input ('\v What is your schools name: ')

sport = input ('\vWhat is you favorite sport:  ')

# Animation Code

print ('\v')

print ('Greeting', player, ', are you ready to get this started, I guess you are!', '\v')

print ('Lets see your name in a fancy way:')

print ('\v')

for kk in range (len(player)):
    print(player[0:kk+1:1], end = '\n')
    time.sleep(0.1)

print ('\v')


print ('Lets see your intrest in a fancy way:')

print ('\v')

for kk in range (len(intrest)):
    print(intrest[0:kk+1:1], end = '\n')
    time.sleep(0.1)

print ('\v')


print ('Lets see your schools name in a fancy way:')

print ('\v')

for kk in range (len(school)):
    print(school[0:kk+1:1], end = '\n')
    time.sleep(0.1)

print ('\v')


print ('Lets see your sport in a fancy way:')

print ('\v')

for kk in range (len(sport)):
    print(sport[0:kk+1:1], end = '\n')
    time.sleep(0.1)

print ('\v')

# Real Code

print ('Lets create a line using the information above ⬆️', sep= '\v')

print ('Using your name:', player, 'is a very good person, he likes to see my project!!!', sep= '\v')

print ('Now with your intrest:', player, 'really likes', intrest, sep='\v' )

print ('Now with your school:', player, 'goes to', school, player, 'is very popular in the school', sep='\v')

print ('And now and finally with your sports:', player, 'is very-very goood at', sport,'\n', player, ' is soo good that he is a sport captain in his school', sep='\v')

print ('\v')

print ('Thank you for seeing this code!!!')


print ('EEEEE', 'N   N', 'DDDDD   ', sep = '  | ')
print ('E    ', 'NN  N', 'D    D  ', sep = '  | ')
print ('EEEEE', 'N N N', 'D     D ', sep = '  | ')
print ('E    ', 'N  NN', 'D    D  ', sep = '  | ')
print ('EEEEE', 'N   N', 'DDDDD   ', sep = '  | ')
