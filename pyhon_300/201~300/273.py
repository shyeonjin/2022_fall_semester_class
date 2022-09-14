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
counter1=Account("심현진",100)
counter2=Account("심진",1020)
counter1.get_account_num()