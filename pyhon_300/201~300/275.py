import random
class Account:
    count=0
    def __init__(self,name,num):
        self.name=name
        self.num=num
        self.bankname="SC은행"
        self.acnum=((str(random.randint(0, 999)).zfill(3))+"-"+
        str(random.randint(0, 99)).zfill(2)+"-"+str(random.randint(0, 999999)).zfill(6))
        Account.count+=1
    @classmethod
    def get_account_num(a):
        print(a.count)
    
    def put(self,money):
        if money>0:
            self.num+=money

    def out(self,money):
        if self.num >money:
            self.num -=money


counter1=Account("심현진",100)
counter1.put(111111111111)
counter1.out(10000)
print(counter1.num)
