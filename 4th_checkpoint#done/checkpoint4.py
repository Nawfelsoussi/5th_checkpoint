
class Bank1:
    def __init__(self, name, age, id, key, balance, loan_amount):
        self.name = name 
        self.age = age
        self.id = id
        self.key = key
        self.balance = balance
        self.loan_amount = loan_amount
     
    
    def deposit1(self, de):
        self.balance += de  
        print(f"Deposited {de}. New balance: {self.balance}")

    
    def withdraw1(self, amount):
        self.balance -= amount
        self.loan_amount += amount  
        print(f"Withdrew {amount}. New balance: {self.balance}. Loan is now: {self.loan_amount}")
         


def person():
    name = input("What's your name: ")
    age = int(input("How old are you: "))
    id_num = int(input("What's your id: "))
    key = input("What's your password: ")
    balance = int(input("What's your balance in DA: "))
    loan_amount = int(input("What's your loan amount: ")) 
    bank = Bank1(name, age, id_num, key, balance, loan_amount)
    return bank



print(" ---PERSON 1--- ")


person1 = person()


de = int(input("How much money do you want to deposit in DA: "))
person1.deposit1(de)


wi = int(input("How much money do you want to withdraw in DA: "))
person1.withdraw1(wi)