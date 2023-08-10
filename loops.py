#loop a name
'''name='Sabrina Spellman'

for l in name :
    print(l)'''

#loop with a list

'''names =['Sabrina', 'Ambrose', 'Hilda', 'Zelda']

for name in names:
    print(name)'''


#set account balance
'''balance = 500
while balance > 0:
    balance=balance -50
    print(f'You just {balance}, your new balance is {balance}')

print(f'Your new balance is {balance}, which is no longer sufficient to withdraw 50$')'''

#infinite loop
'''while(True):
    print("let's go")
    loop_again = input('enter STOP to end the loop: ')
    if(loop_again == 'STOP'):
        break'''


#range
'''for x in range(3):
    print(x)'''


#list
'''example_list= ['Sabrina',16,['Prudence', 'Doncas', 'Agatha'], True, 21, False]
print(example_list)

for x in example_list:
    print(type(x))

for x in example_list:
    print(x)'''

#modify list
'''names=['Sabrina', 'Ambrose','Hilda','Zelda', 'Harvey']

names.append('Carla')
print(names)

names.remove('Carla')
print(names)


names.sort()
print(names)

names.sort(reverse=True)
print(names)'''


#tuples
customers=('Sabrina', 'Ambrose','Hilda','Zelda', 'Harvey')

for cust in customers:
    print(cust)