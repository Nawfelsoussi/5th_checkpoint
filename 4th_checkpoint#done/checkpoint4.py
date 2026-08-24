
# class Bank1:
#     def __init__(self, name, age, id, key, balance, loan_amount):
#         self.name = name 
#         self.age = age
#         self.id = id
#         self.key = key
#         self.balance = balance
#         self.loan_amount = loan_amount
     
    
#     def deposit1(self, de):
#         self.balance += de  
#         print(f"Deposited {de}. New balance: {self.balance}")

    
#     def withdraw1(self, amount):
#         self.balance -= amount
#         self.loan_amount += amount  
#         print(f"Withdrew {amount}. New balance: {self.balance}. Loan is now: {self.loan_amount}")
         


# def person():
#     name = input("What's your name: ")
#     age = int(input("How old are you: "))
#     id_num = int(input("What's your id: "))
#     key = input("What's your password: ")
#     balance = int(input("What's your balance in DA: "))
#     loan_amount = int(input("What's your loan amount: ")) 
#     bank = Bank1(name, age, id_num, key, balance, loan_amount)
#     return bank



# print(" ---PERSON 1--- ")


# person1 = person()


# de = int(input("How much money do you want to deposit in DA: "))
# person1.deposit1(de)


# wi = int(input("How much money do you want to withdraw in DA: "))
# person1.withdraw1(wi)





# What You're Aiming For
# The objective is to create a Python class named "Account" with methods for depositing, withdrawing, and checking balances, encapsulated in a script called "bank_account.py" to simulate basic bank account operations.

 

# Create a class called "Account" that has the following attributes:

# account_number (string)
# account_balance (float)
# account_holder (string)
# The class should have the following methods:

# deposit(amount: float) - This method should add the amount passed as an argument to the account balance.
# withdraw(amount: float) - This method should subtract the amount passed as an argument from the account balance, but only if the account balance is greater than the amount being withdrawn.
# check_balance() - This method should return the current account balance.

# Instructions
 

# Define the Account class and its attributes as specified above.
# Define the deposit() method. It should take in one argument, the amount to be deposited, and add it to the account balance.
# Define the withdraw() method. It should take in one argument, the amount to be withdrawn, and subtract it from the account balance. The method should only execute the withdrawal if the account balance is greater than or equal to the amount to be withdrawn.
# Define the check_balance() method. It should return the current account balance.
# Create an instance of the Account class, and assign it to a variable called "my_account".
# Use the methods of the class to deposit and withdraw money from the account, and check the account balance.
# Test the program by creating multiple instances of the class and performing different transactions on them.

#--- What You're Aiming For----
# The objective is to create a Python class named "Account" with methods for depositing, withdrawing, and checking balances, 
# encapsulated in a script called "bank_account.py" to simulate basic bank account operations.

 

# Create a class called "Account" that has the following attributes:

# account_number (string)
# account_balance (float)
# account_holder (string)
# The class should have the following methods:

# deposit(amount: float) - This method should add the amount passed as an argument to the account balance.
# withdraw(amount: float) - This method should subtract the amount passed as an argument from the account balance, but only if the account balance is greater than the amount being withdrawn.
# check_balance() - This method should return the current account balance.

# Instructions
 

# Define the Account class and its attributes as specified above.
# Define the deposit() method. It should take in one argument, the amount to be deposited, and add it to the account balance.
# Define the withdraw() method. It should take in one argument, the amount to be withdrawn, and subtract it from the account balance. The method should only execute the withdrawal if the account balance is greater than or equal to the amount to be withdrawn.
# Define the check_balance() method. It should return the current account balance.
# Create an instance of the Account class, and assign it to a variable called "my_account".
# Use the methods of the class to deposit and withdraw money from the account, and check the account balance.
# Test the program by creating multiple instances of the class and performing different transactions on them.

class Account:
    def __init__(self, account_number: str, account_balance: float, account_holder: str):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_holder = account_holder

    def deposit(self, amount: float):
        self.account_balance += amount

    def withdraw(self, amount: float):
        if self.account_balance >= amount:
            self.account_balance -= amount
        else:
            print(f"Insufficient funds for {self.account_holder} , you can't withdraw money .")

    def check_balance(self):
        return self.account_balance


my_account = Account("1", 500.0, "Nawfel")
print("Nawfel's balance", my_account.check_balance())
my_account.deposit(50.0)
my_account.withdraw(20.0)
print("Nawfel's new balance", my_account.check_balance())



account2 = Account("2", 100.0, "Yacine")
print("\nYacine's balance:", account2.check_balance())
account2.withdraw(600.0)
print("Yacine's new balance:", account2.check_balance())