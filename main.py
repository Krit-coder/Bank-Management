from Bank import Bank

# use account no. as key and object(customer account) as value
customer_dict = {}
mobile_acc_link = {}            # use mobile no. as key and store account no. as value


def new_cust():
    name = input('Enter the name of customer: ')
    mobile_number = int(input('Enter the mobile number of customer: '))
    opening_balance = int(input('Enter the initial deposit amount: '))
    if opening_balance <= 0:
        print('Invalid Amount')
        return
    pin = int(input('Create PIN: '))
    customer = Bank(name=name, mobile_number=mobile_number,
                    opening_balance=opening_balance, pin=pin)
    customer_dict[customer.customer_account_number] = customer
    mobile_acc_link[customer.mobile_number] = customer.customer_account_number
    print('New User Created!')
    print(
        f'Welcome {customer.name} to World Bank. {customer.customer_account_number} is your account number')


def login():
    account_number = int(input('Enter your Account Number: '))
    account_pin = int(input('Enter your Account PIN: '))
    if account_number in customer_dict.keys() and account_pin == customer_dict[account_number].pin:
        print(f'\n{customer_dict[account_number].name} Logged in')
        customer_dict[account_number].basic_details()
    else:
        print('Account either not exist or the pin is wrong')
        return
    while True:
        user_input1 = input(
            "Press 1 for deposit:\nPress 2 for withdrawl:\nPress 3 for money transfer:\nPress 4 to log out\n")
        if user_input1 == '1':
            customer_dict[account_number].deposit()
        elif user_input1 == '2':
            customer_dict[account_number].withdrawl()
        elif user_input1 == '3':
            mobile = int(input('Enter the mobile number of recepient: '))
            if mobile in mobile_acc_link.keys():
                # use mobile no. to get acct. no.
                secondary = mobile_acc_link[mobile]
                customer_dict[account_number].payment(customer_dict[secondary])
            else:
                print(
                    'The mobile number you have enter does not have an account associated with it')
        elif user_input1 == '4':
            print('Logged Out')
            return
        else:
            print('Invalid input try again')
        print('\n#############################################################\n')
        customer_dict[account_number].basic_details()


while True:
    user_input1 = input(
        "Press 1 for creating a new customer:\nPress 2 for logging in as an existing customer:\nPress 3 for displaying number of customers:\nPress 4 for exit\n")

    if user_input1 == '1':
        print('Create user')
        new_cust()
    elif user_input1 == '2':
        login()
    elif user_input1 == '3':
        print('There currently', Bank.no_of_customer,
              'customers in World bank.')
    elif user_input1 == '4':
        print('Exited')
        break
    else:
        print('Invalid input try again')
    print('\n*************************************************************\n')
