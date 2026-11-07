import sys
import time


def type_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  
    return ''



P = print
type_effect('Welcome To Amazon!')
Choice =  (' Food', 'Cloth', 'Electronics') 


for kk in range(len(Choice)):
    P(str(kk+1) + '.' + Choice[kk], sep = '\t')
Section = input('In which section do you want to buy? \n')
if Section == '1':
    menu = ['Pizza', 'Milkshake','Burger', 'Ice-Cream', 'Taco    ']
    price =['150', '120','100','40','60']

    for kk in range(len(menu)):
        print(str(kk+1)+'. '+menu[kk], price[kk], sep='\t\t')

    shopping_cart = []
    shopping_quant = []

    shopping_complete = False
    print('-------------------------------------------- \n')

    while not shopping_complete:
     order = int(input('Type 1-5 to process the item, press 6 for checkout. \n'))

     if order <= 5:
        print ('Purchasing')
        quant = input('How many units? \n')

        if menu[order - 1] in shopping_cart:
           type_effect('Repeate Purchase')
           idx = shopping_cart.index(menu[order-1])
           shopping_quant[idx]+=quant


        else:
           shopping_cart.append(menu[order-1])
           shopping_quant.append(quant)
            
     elif order == 6:
       type_effect('Proceed to checkout..')
       shopping_complete = 1
     else: 
        type_effect("Sorry that was not a valid input.")


    print('\n')
    print('Your shopping cart')

    grand_tot = 0.0


    print('Item', 'Quant', 'Unit Price', 'Total', sep = '\t\t\t')
    for kk in range(len(shopping_cart)):
        idx = menu.index(shopping_cart[kk])
        unit_price= int(price[idx])
        shopping_quant[kk] = int(shopping_quant[kk])
        tot_price = round (unit_price*shopping_quant[kk], 2)
    
        grand_tot += tot_price
    print(shopping_cart[kk], shopping_quant[kk], unit_price, tot_price, sep='\t\t\t')

    type_effect('\n')

    Currency = ('Dollars($)', 'INR(₹)', 'Yen(¥)')

    for kk in range(len(Currency)):
     print(str(kk+1) + '. ' + Currency[kk])

    choice = int(input('In which currency do you want to buy?\n'))

    if choice == 1:
     dollar = grand_tot / 100
     print("Your total order is ($)", dollar)

    elif choice == 2:
     print("Your total order is (INR)", grand_tot)

    elif choice == 3:
        yen = grand_tot / 10
        print("Your total order is (¥)", yen)

    else:
        print("Invalid choice!")

    print('\n')

    d = input('How do you want to pay? (UPI or card) \n sorry cant do Cash because we do not have "cash on delivery."\n')
    if d == 'card':
        

        CC = ('Visa', 'Mastercard', 'Amex')

        for kk in range(len(CC)):
         print(str(kk+1) + '. ' + CC[kk])

        checkout = int(input('Please choose a card to prooceed checkout! '))

        if checkout == 1:
            type_effect('We have 10% discount in INR(₹) ')
            if choice == 2:
                Inr = grand_tot / 10
                print('Please Pay', Inr )
                print('Dingg come from the machine')
                type_effect('Thank you for using Amazon. ')
                type_effect('I wish seeing you again. ') 
            else:
                type_effect('Cant use this card')
                type_effect('Thank you for using Amazon. ')
                type_effect('I wish seeing you again. ') 

        elif checkout == 2:
            type_effect('We have 10% discount in Yen(¥) ')
            if choice == 3:
                YeN = yen / 10
                print('Please Pay', YeN )
                print('Dingg come from the machine')
                type_effect('Thank you for using Amazon. ')
                type_effect('I wish seeing you again. ') 
            else:
                type_effect('Cant use this card')
                type_effect('Thank you for using Amazon. ')
                type_effect('I wish seeing you again. ') 

        elif checkout == 3:
            type_effect('We have 10% discount in Dollar(¥) ')
            if choice == 1:
                llar = dollar / 10
                print('Please Pay', llar )
                print('Dingg come from the machine')
                type_effect('Thank you for using Amazon. ')
                type_effect('I wish seeing you again. ') 
            else:
                type_effect('Cant use this card')
                type_effect('Thank you for using Amazon. ')
                type_effect('I wish seeing you again. ') 

    else:
        print('Dingg come from the machine')
        type_effect('Thank you for using Amazon. ')
        type_effect('I wish seeing you again. ') 









   

    print('-------------------------------------------- \n')

elif  Section == '2':
    menu = ['T-shirt', 'Jeans ','Kurta', 'Track pant', 'Shirt']
    price =['300', '420','301','720','610']
   

    for kk in range(len(menu)):
        print(str(kk+1)+'. '+menu[kk], price[kk], sep='\t\t')

    shopping_cart = []
    shopping_quant = []

    shopping_complete = False
    print('-------------------------------------------- \n')

    while not shopping_complete:
     order = int(input('Type 1-5 to process the item, press 6 for checkout. \n'))

     if order <= 5:
        print ('Purchasing')
        quant = input('How many units? \n')

        if menu[order - 1] in shopping_cart:
           type_effect('Repeate Purchase')
           idx = shopping_cart.index(menu[order-1])
           shopping_quant[idx]+=quant


        else:
           shopping_cart.append(menu[order-1])
           shopping_quant.append(quant)
            
     elif order == 6:
       type_effect('Proceed to checkout..')
       shopping_complete = 1
     else: 
        type_effect("Sorry that was not a valid input.")


    print('\n')
    print('Your shopping cart')

    grand_tot = 0.0


    print('Item', 'Quant', 'Unit Price', 'Total', sep = '\t\t\t')
    for kk in range(len(shopping_cart)):
        idx = menu.index(shopping_cart[kk])
        unit_price= int(price[idx])
        shopping_quant[kk] = int(shopping_quant[kk])
        tot_price = round (unit_price*shopping_quant[kk], 2)
    
        grand_tot += tot_price
    print(shopping_cart[kk], shopping_quant[kk], unit_price, tot_price, sep='\t\t\t')

    type_effect('\n')

    Currency = ('Dollars($)', 'INR(₹)', 'Yen(¥)')

    for kk in range(len(Currency)):
     print(str(kk+1) + '. ' + Currency[kk])

    choice = int(input('In which currency do you want to buy?\n'))

    if choice == 1:
     dollar = grand_tot / 100
     print("Your total order is ($)", dollar)

    elif choice == 2:
     print("Your total order is (INR)", grand_tot)

    elif choice == 3:
        yen = grand_tot / 10
        print("Your total order is (¥)", yen)

    else:
        print("Invalid choice!")



    print('\n')

    d = input('How do you want to pay? (UPI or card) \n sorry cant do Cash because we do not have "cash on delivery."\n')
    if d == 'card':
        

        CC = ('Visa', 'Mastercard', 'Amex')

        for kk in range(len(CC)):
         print(str(kk+1) + '. ' + CC[kk])

        checkout = int(input('Please choose a card to prooceed checkout! '))

        if checkout == 1:
            type_effect('We have 10% discount in INR(₹) ')
            if choice == 2:
                Inr = grand_tot / 10
                print('Please Pay', Inr )
                print('Dingg come from the machine')
                type_effect('Thank you for using Amazon. ')
                type_effect('I wish seeing you again. ') 
            else:
                type_effect('Cant use this card')
                type_effect('Thank you for using Amazon. ')
                type_effect('I wish seeing you again. ') 

        elif checkout == 2:
            type_effect('We have 10% discount in Yen(¥) ')
            if choice == 3:
                YeN = yen / 10
                print('Please Pay', YeN )
                print('Dingg come from the machine')
                type_effect('Thank you for using Amazon. ')
                type_effect('I wish seeing you again. ') 
            else:
                type_effect('Cant use this card')
                type_effect('Thank you for using Amazon. ')
                type_effect('I wish seeing you again. ') 

        elif checkout == 3:
            type_effect('We have 10% discount in Dollar(¥) ')
            if choice == 1:
                llar = dollar / 10
                print('Please Pay', llar )
                print('Dingg come from the machine')
                type_effect('Thank you for using Amazon. ')
                type_effect('I wish seeing you again. ') 
            else:
                type_effect('Cant use this card')
                type_effect('Thank you for using Amazon. ')
                type_effect('I wish seeing you again. ') 

    else:
        print('Dingg come from the machine')
        type_effect('Thank you for using Amazon. ')
        type_effect('I wish seeing you again. ') 









   

    print('-------------------------------------------- \n')





   
elif Section == '3':
    if Section == '3':
        menu = ['Tv   ', 'Mobile ','Fridge', 'Ps5    ', 'X-box']
        price =['35000', '40020','30001','70020','61210']
   

    for kk in range(len(menu)):
        print(str(kk+1)+'. '+menu[kk], price[kk], sep='\t\t')

    shopping_cart = []
    shopping_quant = []

    shopping_complete = False
    print('-------------------------------------------- \n')

    while not shopping_complete:
     order = int(input('Type 1-5 to process the item, press 6 for checkout. \n'))

     if order <= 5:
        print ('Purchasing')
        quant = input('How many units? \n')

        if menu[order - 1] in shopping_cart:
           type_effect('Repeate Purchase')
           idx = shopping_cart.index(menu[order-1])
           shopping_quant[idx]+=quant


        else:
           shopping_cart.append(menu[order-1])
           shopping_quant.append(quant)
            
     elif order == 6:
       type_effect('Proceed to checkout..')
       shopping_complete = 1
     else: 
        type_effect("Sorry that was not a valid input.")


    print('\n')
    print('Your shopping cart')

    grand_tot = 0.0


    print('Item', 'Quant', 'Unit Price', 'Total', sep = '\t\t\t')
    for kk in range(len(shopping_cart)):
        idx = menu.index(shopping_cart[kk])
        unit_price= int(price[idx])
        shopping_quant[kk] = int(shopping_quant[kk])
        tot_price = round (unit_price*shopping_quant[kk], 2)
    
        grand_tot += tot_price
    print(shopping_cart[kk], shopping_quant[kk], unit_price, tot_price, sep='\t\t\t')

    type_effect('\n')

    Currency = ('Dollars($)', 'INR(₹)', 'Yen(¥)')

    for kk in range(len(Currency)):
     print(str(kk+1) + '. ' + Currency[kk])

    choice = int(input('In which currency do you want to buy?\n'))

    if choice == 1:
     dollar = grand_tot / 100
     print("Your total order is ($)", dollar)

    elif choice == 2:
     print("Your total order is (INR)", grand_tot)

    elif choice == 3:
        yen = grand_tot / 10
        print("Your total order is (¥)", yen)

    else:
        print("Invalid choice!")




    print('\n')

    d = input('How do you want to pay? (UPI or card) \n sorry cant do Cash because we do not have "cash on delivery."\n')
    if d == 'card':
        

        CC = ('Visa', 'Mastercard', 'Amex')

        for kk in range(len(CC)):
         print(str(kk+1) + '. ' + CC[kk])

        checkout = int(input('Please choose a card to prooceed checkout! '))

        if checkout == 1:
            type_effect('We have 10% discount in INR(₹) ')
            if choice == 2:
                Inr = grand_tot / 10
                print('Please Pay', Inr )
                print('Dingg come from the machine')
                type_effect('Thank you for using Amazon. ')
                type_effect('I wish seeing you again. ') 
            else:
                type_effect('Cant use this card')
                type_effect('Thank you for using Amazon. ')
                type_effect('I wish seeing you again. ') 

        elif checkout == 2:
            type_effect('We have 10% discount in Yen(¥) ')
            if choice == 3:
                YeN = yen / 10
                print('Please Pay', YeN )
                print('Dingg come from the machine')
                type_effect('Thank you for using Amazon. ')
                type_effect('I wish seeing you again. ') 
            else:
                type_effect('Cant use this card')
                type_effect('Thank you for using Amazon. ')
                type_effect('I wish seeing you again. ') 

        elif checkout == 3:
            type_effect('We have 10% discount in Dollar(¥) ')
            if choice == 1:
                llar = dollar / 10
                print('Please Pay', llar )
                print('Dingg come from the machine')
                type_effect('Thank you for using Amazon. ')
                type_effect('I wish seeing you again. ') 
            else:
                type_effect('Cant use this card')
                type_effect('Thank you for using Amazon. ')
                type_effect('I wish seeing you again. ') 

    else:
        print('Dingg come from the machine')
        type_effect('Thank you for using Amazon. ')
        type_effect('I wish seeing you again. ') 









   

    print('-------------------------------------------- \n')

  
 