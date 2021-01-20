class Bank_Account():
    
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
        
    def deposit(self,add):
        self.balance+=add
        print('Your deposit is accepted')
        return self.balance 
        
    def withdraw(self,sub):
        self.balance-=sub
       
        if(self.balance<sub):
            print('Insufficient funds')
        else:
            print('withdrawn successful')
            return self.balance
