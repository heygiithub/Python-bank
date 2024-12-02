class BankAccount:
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
        
    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount
            print(f"{amount} deposited, current balance is {self.balance}")
        else:
            print("not allowed")
            
    def withdraw(self,amount):
        if 0<amount<= self.balance:
            self.balance-=amount
            print(f"{amount} withraw current balance: {self.balance}")
        else:
            print("insufficient balance")
        
    def check_balance(self):
        print(f"current balance: {self.balance}ruppes ")
    
def main():
    account = {}
    while True:
        print("\nWELCOME TO THE BANK OF PYTHON!!!!")
        print("1.CREATE ACCOUNT")
        print("2.LOG IN")
        print("3.Quit")
        
        choice = input("enter your choice: ")
        
        if choice == "1":
            name = input("enter your name: ")
            if name in account:
                print("account already exits!!!")
            else:
                account[name] = BankAccount(name)
                print("Account Created Successfully!!")
                
        elif choice == "2":
            name = input("enter your name: ")
            if name in account:
                acc = account[name]
                print(f"welcome back, {name}")
                
                while True:
                    print("\n1.check balance")
                    print("2.deposit")
                    print("3.withdraw")
                    print("4.log out")
                    
                    option = input("enter your option: ")
                    if option == "1":
                        acc.check_balance()
                    elif option=="2":
                        amount = float(input("enter the amount to deposit: "))
                        acc.deposit(amount)
                    elif option == "3":
                        amount = float(input("enter the amount to withdraw: "))
                        acc.withdraw(amount)
                    elif option == "4":
                        print("logged out Successfully")
                        break
                    else:
                        print("invalid options!!")
            else:
                print("Account not found ..Please Create Account First..")
        
        elif choice == "3":
            print("Thank you for using python bank")
            break
        
        else:
            print("invalid choice ")
if __name__ == "__main__":
    main()
        
            

            
                        
                        
                        
                    
                    
                    
            