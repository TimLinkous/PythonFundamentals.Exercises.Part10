
import pickle


class Person:
    def __init__(self, id: int, first_name: str, last_name: str):
        self.id = id 
        self.first_name = first_name
        self.last_name = last_name

class Account:
    def __init__(self, number: int, type_of_account: str, owner: Person, balance: float = 0.0):
        self.number = number
        self.type_of_account = type_of_account
        self.owner = owner
        self.balance = balance


class PersistenceUtils():
    @staticmethod
    def write_pickle(data, filename):
        with open(filename, 'wb') as file:
            pickle.dump(data, file)

    @staticmethod
    def load_pickle(filename):
        with open(filename, 'rb') as file:
            data = pickle.load(file)
        return data

    
class Bank:    
    def __init__(self):
        self.customers = {}  #create empty dictionaries to store customers and accounts
        self.accounts = {}

    def add_customer(self, person: Person): #defines the method - 'person' parameter will be intance of the person class
        if person.id in self.customers:  #need to check to see if customer already exists
            raise ValueError(f"Identification number {person.id} already exists in the system.")
            #^^ raise an exception if the person is already in the customer list
        self.customers[person.id] = person  #person added to the self.customers dictionary
                #id is the key, person is the value
    def add_account(self, account: Account):
        if account.owner.id not in self.customers:
            raise ValueError("The account owner must be registered as a customer first.")
        if account.number in self.accounts:
            raise ValueError("This account ID already exists.")
        self.accounts[account.number] = account

    def remove_account(self, account_number: int):
        if account_number not in self.accounts:
            raise ValueError("This account does not exist.")
        del self.accounts[account_number] 
        
    def deposit(self, account_number: int, deposit: float):
        if account_number not in self.accounts:
            raise ValueError("This account does not exist.")
        if deposit <= 0:
            raise ValueError("Deposit amount cannot be negative.")
        self.accounts[account_number].balance += deposit #grabs acct number from accounts dictionary
            #access balance attribute of 'Account' object. Increases balance for that account by 'deposit' amount
    
    def withdrawal(self, account_number: int, withdrawl_amount: float):
        if account_number not in self.accounts:
            raise ValueError("This account does not exist.")
        if withdrawl_amount <= 0:
            raise ValueError("You must enter a positive amount to withdraw.")
        if withdrawl_amount > self.accounts[account_number].balance:
            raise ValueError("You have insufficient funds in this account for that withdrawl request.")
        self.accounts[account_number].balance -= withdrawl_amount
                #decrease balance of the specified account number by the withdrawl amount

    def balance_inquiry(self, account_number: int):
        if account_number not in self.accounts:
            raise ValueError("This account does not exist.")
        balance = self.accounts[account_number].balance
        print(f"The current balance associated with Account # {account_number} is {balance}.")
        return balance 
    
    def save_data(self, filename = 'bank_data.pickle'):
        data = {
            'customers': self.customers,
            'accounts': self.accounts
        }
        PersistenceUtils.write_pickle(data, filename)

    def load_data(self, filename = 'bank_data.pickle'):
        data = PersistenceUtils.load_pickle(filename)
        self.customers = data['customers']
        self.accounts = data['accounts']



