import sys
import time

def type_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  
    return ''




type_effect('Welcome To Amazon!')
Choice =  (' Food', 'Cloth', 'Electronics') 
type_effect = (Choice)

for kk in range(len(Choice)):
    print(str(kk+1) + '.' + Choice[kk], sep = '\t')
Section = input('In which section do you want to buy? \n')
if Section == 1:
    menu = ['Pizza', 'Milkshake','Burger', 'Ice-Cream', 'Taco']
    price = ['150', '120','100', '40', '60']

    for kk in range(len(Choice)):
        print(str(kk+1)+'. '+menu[kk], price[kk], sep='\t\t')

    shopping_cart = []
    shopping_quant = []

    shopping_complete = False

    while not shopping_complete:
     order = int(input(print('Type 1-5 to process the item, press 6 for checkout.')) )

     if order <= 5:
        type_effect ('Purchasing')
        quant = input(type_effect('How many units? \n'))

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
        unit_price=price[idx]
        tot_price = round(unit_price*shopping_quant[kk], 2)
        grand_tot += tot_price
    type_effect(shopping_cart[kk], shopping_quant[kk], unit_price, tot_price, sep='\t\t\t')

    type_effect()


    Currency =  (' Dollars($)', 'Yen(¥)', 'Inr(₹)') 
    type_effect = (Currency)

   

    for kk in range(len(Currency)):
        print(str(kk+1) + '.' + Currency[kk], sep = '\t')
        input('In which currency do you want to buy? \n')

        if input == 1:
           dollar = grand_tot / 100
           type_effect('Your total order is ($)', dollar)

        elif input == 2:
           yen = grand_tot / 10
           type_effect('Your total order is (¥)', yen)


        else:
           type_effect('Your total order is (INR)', grand_tot)



        

   


