# This file contains code for managing your account
#accounts = {}
accounts_dict = {'name': 'lolo', 'password': "time"}  # dictionary where key is the  password and value is User
#print("accounts['Name']: ", accounts['Name'])
#print("accounts['password']: ", accounts['password'])
# Write a function adds user details to accounts
name = input("Enter new user :")
password = input("Enter new user password: ")

def add_account(name, password):
  

    accounts_dict[password] = name

    return accounts_dict

print("Your account has been created!")
   


def login(name, password):
    if accounts_dict[password] == name:
        
        return True
    else:
        return False
    
