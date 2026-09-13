# Import
import random


import sys
import time

def type_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  

# Title

print ('M   M','IIIII','SSSSS','SSSSS','IIIII','N   N','GGGGG', sep = ' | ')
print ('MM MM','  I  ','S    ','S    ','  I  ','NN  N','G    ', sep = ' | ')
print ('M M M','  I  ','SSSSS','SSSSS','  I  ','N N N','G  GG', sep = ' | ')
print ('M   M','  I  ','    S','    S','  I  ','N  NN','G   G', sep = ' | ')
print ('M   M','IIIII','SSSSS','SSSSS','IIIII','N   N','GGGGG', sep = ' | ')

print ('\v')

# Code 

# 2 number

player = input('Greetings player, can you tell me your name: ')


num1 = int(input(player + ' Please tell me a number:\v'))
num2 = int(input(player + ' Please tell me another number:\v'))

op = random.randint(0, 3)

op_list = ['+', '-', '*', '/']

if op == 0:
  rhs = num1 + num2

if op == 1:
  rhs = num1 - num2

if op == 2:
  rhs = num1 * num2

if op == 3:
   rhs = num1 / num2 


type_effect('Can you tell me the missing operator''\v')

type_effect ('Choose between: + , - , * , / \v')

qn = str(num1) + ' __ ' + str(num2) + ' = ' + str(rhs) + '\n'

answer = input(qn)


if answer == op_list[op]:
  
  type_effect(player + ' Well Done')
else: 
  type_effect(player + ' You made a mistake...')

  print ('\v')

type_effect ('The correct answer is: ' + op_list[op])
type_effect (str(num1) + ' ' + op_list[op] + ' ' + str(num2) + ' = ' + str(rhs) + '\n')
 # 3 Number Code

num3 = random.randint(1, 100)

op1 = random.randint(0, 1)

op2 = random.randint(0, 1)


if op1 == 0:
  rhs = num1 + num2

if op1 == 1:
  rhs = num1 - num2

if op2 == 0:
  rhs = rhs + num3

if op2 == 1:
  rhs = rhs - num3


type_effect ('Can you tell me the missing operator\n')

qn = str(num1) + ' __ ' + str(num2) + ' __ ' + str(num3) + ' = ' + str(rhs) + '\n'

answer = input(qn)


if answer[0] == op_list[op1] and answer[1] == op_list[op1]:
  
  type_effect (player + ' Well Done')

else: 
  
 type_effect (player + ' You made a mistake...')

print ('\v')

type_effect ('The correct answer is: ' + op_list[op1 + op2])
type_effect (str(num1) + ' ' + op_list[op1] + ' ' +  str(num2) + ' ' +  op_list[op2] + ' ' + str(num3) + ' = ' + str(rhs) + '\n')

# 4 Number Code

num4 = random.randint(1, 100)

op1 = random.randint(0, 1)

op2 = random.randint(0, 1)

op3 = random.randint(0, 1)


if op1 == 0:
  rhs = num1 + num2

if op1 == 1:
  rhs = num1 - num2

if op2 == 0:
  abc = rhs + num3

if op2 == 1:
  abc = rhs - num3

if op3 == 1:
  bcd = abc * num4

if op3 == 0:
  bcd = abc / num4

type_effect('Can you tell me the missing operator\n')
 

qn = str(num1) + ' __ ' + str(num2) + ' __ ' + str(num3) + ' __ ' + str(num4) + ' = ' + str(bcd) + '\n'

answer = input(qn)

if answer[0] == op_list[op1] and answer[1] == op_list[op2]:

  type_effect (player + ' You are Goated')
else: 
 type_effect (player + ' You made a mistake...')

print ("\v")

type_effect ('The correct answer is: ' + op_list[op1 + op2 + op3])
type_effect (str(num1) + ' ' + op_list[op1] + ' ' + str(num2) + ' ' + op_list[op2] + ' ' + str(num3) + ' ' + op_list[op3] + ' ' + str(num4) + ' = ' + str(bcd) + '\n')


type_effect (player + ' thank you for playing!!! ')

print ("\v")

print ('EEEEE', 'N   N', 'DDDDD   ', sep = '  | ')
print ('E    ', 'NN  N', 'D    D  ', sep = '  | ')
print ('EEEEE', 'N N N', 'D     D ', sep = '  | ')
print ('E    ', 'N  NN', 'D    D  ', sep = '  | ')
print ('EEEEE', 'N   N', 'DDDDD   ', sep = '  | ')