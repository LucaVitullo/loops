# loop a name
"""name='Sabrina Spellman'

for l in name :
    print(l)"""

# loop with a list

"""names =['Sabrina', 'Ambrose', 'Hilda', 'Zelda']

for name in names:
    print(name)"""


# set account balance
"""balance = 500
while balance > 0:
    balance=balance -50
    print(f'You just {balance}, your new balance is {balance}')

print(f'Your new balance is {balance}, which is no longer sufficient to withdraw 50$')"""

# infinite loop
"""while(True):
    print("let's go")
    loop_again = input('enter STOP to end the loop: ')
    if(loop_again == 'STOP'):
        break"""


# range
"""for x in range(3):
    print(x)"""


# list
"""example_list= ['Sabrina',16,['Prudence', 'Doncas', 'Agatha'], True, 21, False]
print(example_list)

for x in example_list:
    print(type(x))

for x in example_list:
    print(x)"""

# modify list
"""names=['Sabrina', 'Ambrose','Hilda','Zelda', 'Harvey']

names.append('Carla')
print(names)

names.remove('Carla')
print(names)


names.sort()
print(names)

names.sort(reverse=True)
print(names)"""


# tuples
"""customers=('Sabrina', 'Ambrose','Hilda','Zelda', 'Harvey')

for cust in customers:
    print(cust)"""


#######DICTIONARIES

"""customer ={
    'first_name':'Dartalion',
    'last_name': 'Swift',
    'age': 16
}

print(customer['first_name'])

#create a new dictionary

customer['birth_date']='10/31/2000'
customer['superpower']='Levitation'
customer['superpowers']= ['Levitation','power']

print(customer)


#pretty print ( this will put the dictionary in Alphabetich order)
from pprint import pprint

pprint(customer)


#( this will put the dictionary in the original order)
pprint(customer, sort_dicts=False)


#delete

del customer['birth_date']

print(customer)

#condition for dictionary
if ('superpowers' in customer):
    print(f'this customer has superpowers{customer["superpowers"]}' )
else:
    print('no superpowers')
    
#loop for dictionary key
for k in customer["superpowers"]:
    print(k)



#dictionaries

sabrina_dict ={'last_name' : 'Spellman',
               'first_name' : 'Sabrina',
               'birth_date' : '10/31/2000'}

nick_dict ={'last_name' : 'scratch',
               'first_name' : 'Nicholas'}

harvey_dict ={'last_name' : 'Kinkle',
               'first_name' : 'Harvey'}

characters = [sabrina_dict, nick_dict, harvey_dict]

pprint(characters, sort_dicts=False)

for c in characters:
    last_name = c['last_name']
    first_name = c['first_name']
    print(f'{first_name} {last_name}')




#dictionary of list

first_names={'first_name': ['Sabrina', 'Nicholas', 'harvey']}
last_names = {'last_name': ['Spellman', 'Scratch', 'kinkle']}

print(first_names)
print(last_names)

print (last_names['last_name'])

characters = ['Sabrina', 'Ambrosa','Hilda','Zelda','Harvey']
ages = [16,75,270,290,17]

characters_ages = { k:v for (k,v)  in zip (characters,ages)}
print(characters_ages)"""


######FUNCTIONS#####


"""account_balance = 500

def get_balance () :
    print(f'your balance is $ {account_balance}')

get_balance()



def get_balance (account_number) :
    print(f'Account {account_number} | Balance: $500')

get_balance(728736837)

account_balance = 500

def withdraw_funds ( account_number, withdrawal_amount):

    approve_transaction = 'Your transaction is denied'

    if (withdrawal_amount) <= account_balance:
        approve_transaction = 'Your transaction is approved'

    return approve_transaction
    
withdraw_funds('487387484', 600)



account_balance= 500

def deposit_funds ( deposit_amount):

    new_balance = deposit_amount+ account_balance
    return (new_balance)

deposit_funds(700)

#write a function
#accept a deposit amount and an account number
#add the deposit amount to the existing balance
#send back the new balance and the account number
account_balance = 500
def make_deposit(deposit_amount, account_number):
    new_balance = account_balance + deposit_amount
    return f'balance is {new_balance} for account { account_number}'

make_deposit(1000, '3584784')

account_balance= '500'
promo_interest_rate = 0.5

def add_interest (bal,rate):

    bal = float(bal)

    new_bal = bal + (bal * rate)
    return new_bal

print(add_interest(account_balance,promo_interest_rate))


#lambda function

add_interest = lambda bal, rate : float(bal) + (bal*rate)
new_balance = add_interest(float(account_balance), promo_interest_rate)

##define a lambda function
#set it up to accept a deposit amount
#sent back the new balance

make_deposit = lambda deposit_amount : float(account_balance) + deposit_amount

make_deposit(50)"""

#####PANDAS####

import pandas as pd
import pprint

"""

# Create a Pandas DataFrame
df = pd.DataFrame(
    {
        "Name": ["John Doe", "Jane Doe", "Peter Smith"],
        "Age": [30, 25, 20],
        "Occupation": ["Software Engineer", "Doctor", "Student"],
    }
)

# Print the DataFrame
print(df.describe())

# Print the DataFrame in name order
print(df.sort_values(by="Name"))
print(df.head)

# dataframe from a list of dictionaries
acconts = [
    {"acct_no": "779311", "full_name": "Sabrina Spellman", "acct_bal": 19000},
    {
        "acct_no": "779311",
        "full_name": "Ambrose Spellman",
        "acct_bal": 14000,
        "Superpower": "Telepathy",
    },
    {"acct_no": "779311", "full_name": "Zelda Spellman", "acct_bal": 29000},
]

acct_df = pd.DataFrame(acconts)
print(acct_df)

# create a new dataframe that returns only the account number and the account balance
acct_num_names = acct_df[["full_name", "acct_bal"]]
print(acct_num_names.head)


# CONVERT THE BALANCES TO A SERIES AND USE PANDAS  FUNCTION TO GENERATE THE SUM OF BALANCES
balances = acct_num_names["acct_bal"]

print(balances.sum())


# CONVERT THE BALANCES TO A LIST AND WRITE A TRADITIONAL  FUNCTION TO   SUM UP THE ACCOUNT  BALANCES
bal_list = list(balances)
print(bal_list)

bal_sum = 0

for b in bal_list:
    print(f"The total balance is {bal_sum}")
    print(f"The client's balance is {b}")
    bal_sum = bal_sum + b
    print(f"The total balance is {bal_sum}")
    print("----")


# use a f-string to print "The sum of all accounts balance is (sum)"

print(f"the sum of all account balance is {bal_sum}")"""

#######DICTIONARY OF LIST######


acct_dict = {
    "acct_no": ["7779311", "7789422", "7829366", "7839477"],
    "first_name": ["Sabrina", "Ambrose", " Hilda", "Zelda"],
    "last_name": ["Spellman", "Spellman", "Spellman", "Spellman"],
    "acct_bal": [19000, 21000, 25000, 32000],
}

acct_df = pd.DataFrame(acct_dict)
# iloc to find records
print(acct_df.iloc[0])
print(acct_df.iloc[1, 1])
# row 2 all columns
print(acct_df.iloc[1, :])

print(acct_df.iloc[:, 1])


# all rows from colomn 1 and 2(up to, but not including 3)

print(acct_df.iloc[:, 1:3])


# rows from 2 to 4

print(acct_df.iloc[1:4, 1:3])


# find record with last name

print(acct_df.loc[acct_df["last_name"] == "Spellman"])


# find value by numeric condition
print(acct_df.loc[acct_df["acct_bal"] >= 25000])


# find value by string wildcard

print(acct_df.loc[acct_df["first_name"].str.contains("Amb")])
