class account():
    def __init__(self,owner,balance):
        self.owner = owner 
        self.balance = balance 
    def deposit(self,newcome):
        self.balance += newcome 
    def withdraw(self,n):
        def __init__(self,n):
            self.n = n 
        if self.balance >= n:
            self.balance -= n
        else : 
            self.balance = 0 
    def show(self):
        print(self.balance)
a = account("random" , 2000)
a.deposit(1000)
a.withdraw(500)
a.show()

