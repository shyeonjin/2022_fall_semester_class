import random
class Account:
    count=0
    def __init__(self,name,num):
        self.plusmoney_c=0
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
            self.plusmoney_c += 1
            if self.plusmoney_c % 5 == 0: 
                self.num = (self.num * 1.01)
    def out(self,money):
        if self.num >money:
            self.num -=money

    def display_info(self):
        print("은행이름:",self.bankname)
        print("예금주:",self.name)
        print("계좌번호:",self.acnum)
        print("잔고:{}".format(self.num,','))

counter1=Account("심현진",100)
counter1.put(1)
counter1.put(2)
counter1.put(3)
counter1.put(4)
counter1.put(5)

print(counter1.num)