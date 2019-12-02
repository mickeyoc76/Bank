import sqlite3

class Account():
    
    def __init__(self, name=None):
        self.name = name
    
    def get_user(self):
         return self.name
    
    def __str__(self):
        return self.name
    
class Checking_Account(Account):
    
    def __init__(self,name,balance=100):
        super().__init__(name)
        self.balance = balance
    
    def get_deposit(self):
        self.deposit  = int(input("Well %s how much would you like to deposit? "%(self.name)))
        self.balance = self.balance + self.deposit
        return "%s Your checking account balance is %s" %(self.name, self.balance)
  
    def get_withdrawal(self):
        self.withdraw  = int(input("Well %s Enter withdrawal amount? "%(self.name)))
        self.balance = self.balance - self.withdraw
        return " %s Your checking account balance is %s" %(self.name, self.balance)
    
    def get_balance(self):
        return self.balance

class Business_Account(Checking_Account):
    
    def __init__(self,name,balance=100):
        super().__init__(name)
        self.balance = balance
    
    def get_deposit(self):
        self.deposit  = int(input("Well %s how much would you like to deposit? "%(self.name)))
        self.balance = self.balance + self.deposit
        return "%s Your business account balance is %s" %(self.name, self.balance)
  
    def get_withdrawal(self):
        self.withdraw  = int(input("Well %s Enter withdrawal amount? "%(self.name)))
        self.balance = self.balance - self.withdraw
        return " %s Your business account balance is %s" %(self.name, self.balance)
    
    def get_balance(self):
        return "%s Your business account balance is %s" %(self.name, self.balance)

class Savings_Account(Checking_Account):
    
    def __init__(self,name,balance=100):
        super().__init__(name)
        self.balance = balance
    
    def get_deposit(self):
        self.deposit  = int(input("Well %s how much would you like to deposit? "%(self.name)))
        self.balance = self.balance + self.deposit
        return "%s Your savings balance is %s" %(self.name, self.balance)
  
    def get_withdrawal(self):
        self.withdraw  = int(input("Well %s Enter withdrawal amount? "%(self.name)))
        self.balance = self.balance - self.withdraw
        return " %s Your savings account balance is %s" %(self.name, self.balance)
    
    def get_balance(self):
        return "%s Your savings account balance is %s" %(self.name, self.balance)

running_total = []

def checking_deposit(account_name):
    user = Account(account_name)
    bal = Checking_Account(user)
    bal.get_deposit()
    running_total.append(bal.get_balance())
    print(running_total[0])

def checking_withdraw(account_name):
    user = Account(account_name)
    bal = Checking_Account(user)
    bal.get_withdrawal()
    print(bal.get_balance())   

def business_deposit(account_name):
    user = Account(account_name)
    bal = Business_Account(user)
    bal.get_deposit()
    print(bal.get_balance())   

def business_withdraw(account_name):
    user = Account(account_name)
    bal = Business_Account(user)
    bal.get_withdrawal()
    print(bal.get_balance())    

def savings_deposit(account_name):
    user = Account(account_name)
    bal = Savings_Account(user)
    bal.get_deposit()
    print(bal.get_balance())   

def savings_withdraw(account_name):
    user = Account(account_name)
    bal = Savings_Account(user)
    bal.get_withdrawal()
    print(bal.get_balance())    


def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('accounts.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from customers"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        records = list(records)
        for row in records:
            if account_name in row[1] and account_type in row[4]:
                curr_bal = row[2]
                return curr_bal
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            #print("The SQLite connection is closed")


def updateSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('accounts.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sql = "UPDATE customers SET balance = %d WHERE name = %s " %(balance, sql_account_name)
        cursor.execute(sql)
        sqliteConnection.commit()
        print("Record Updated successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")


account_name = input("Enter username: ") 
account_type = input("Which account do you want to use? ").lower()
action = input("Would you like to withdraw or deposit? ").lower()

if action == "withdraw" and account_type == "checking":
    checking_withdraw(account_name)
elif action == "deposit" and account_type == "checking":
    checking_deposit(account_name)
elif action == "withdraw" and account_type == "business":
    business_withdraw(account_name)
elif action == "deposit" and account_type == "business":
    business_deposit(account_name)
elif action == "withdraw" and account_type == "savings":
    savings_withdraw(account_name)
elif action == "deposit" and account_type == "savings":
    savings_deposit(account_name)