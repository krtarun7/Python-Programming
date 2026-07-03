class ATM:      
    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()   
             
    def menu(self):
        user_input=input("""Hi how can i help you !
          1.create pin 
          2.change pin 
          3.check balance
          4.withdrawl balance
          """)   
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.change_pin()
        elif user_input=="3":
            self.check_balance()
        elif user_input=="4":
            self.withdraw_balance()
        else:
            exit()
    def create_pin(self):
        self.pin=input("Enter your pin: ")
        user_balance = int(input('enter balance: '))
        self.balance = user_balance
        print("pin created successfully")        
        self.menu()
        
    def change_pin(self):
        old_pin=input("Enter your old pin: ")
        if old_pin==self.pin:
            self.pin=input("Enter your new pin: ")
            print("pin changed successfully")
        else:
            print("incorrect pin")
        self.menu()
        
    def check_balance(self):
        pin=input("Enter your pin:  ")
        if pin==self.pin:
            print(f"Your balance is {self.balance}")
        else:
            print("incorrect pin")
        self.menu()
        
    def withdraw_balance(self):
        pin=input("Enter your pin:  ")
        if pin==self.pin:
            amount=int(input("Enter the amount to withdraw : "))
            if amount<=self.balance:
                self.balance-=amount
                print(f"withdrawl successful, your new balance is {self.balance}")
            else:
                print("insufficient balance")
        else:
            print("incorrect pin")
        self.menu()
Obj=ATM()