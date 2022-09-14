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


counter1=Account("심현진",100)
print(Account.count)

counter2=Account("심진",1020)
print(Account.count)