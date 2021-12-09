class Atm:
    def _init_(self,cardnumber,pin):
        self.cardnumber =  cardnumber
        self.pin = pin
    
    def balanceinuiry(self):
        print("Your balance is :$100")    
        
    def cashwidthdrawal(self,amount):
        new_amount = 100 - amount
        print("You ithdrawed:"+str(amount)+"your remaining balance is :"+str(new_amount))
        
def main():
    name = input ("Hello what is your name?")       
    print("Hello, " + name)
    cardnumber = input ("Insert your card number: ")
    pin = input ("Enter your pin: ")
    new_user = Atm(cardnumber,pin)     
    
    print("choose your activity")
    print("1. Baklance Inquiry")
    print("2. cash withdrawal")
    activity = int(input("Enter activity choice: "))
    
    if (activity == 1):
        new_user .balanceinuiry()
    elif( activity==2) :
        amount = int(input("enter the amount: "))
        new_user.cashwidthdrawal(amount)   
    else:
        print("Enter a valid number")
        
if __name__ == "_main_":
    main()            