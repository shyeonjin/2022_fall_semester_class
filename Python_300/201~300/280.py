import random
class Account:
    count=0
    def __init__(self,name,num):
        self.put_log=[]
        self.out_log=[]


        
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
            self.put_log.append(money)
            self.num+=money
            self.plusmoney_c += 1
            if self.plusmoney_c % 5 == 0: 
                self.num = (self.num * 1.01)
    def out(self,money):
        if self.num >money:
            self.out_log.append(money)
            self.num -=money

    def display_info(self):
        print("은행이름:",self.bankname)
        print("예금주:",self.name)
        print("계좌번호:",self.acnum)
        print("잔고:{}".format(self.num,','))


    def deposit_history(self):
        for money in self.put_log:
            print(money)
    def withdraw_history(self):
        for money in self.out_log:
            print(money)


counter=Account("그루트",10000)
counter.put(1111)
counter.put(11161)
counter.put(11151)
counter.put(11131)
counter.put(11121)
counter.put(11111)
counter.put(1111)
counter.deposit_history()


print()
counter.out(11131)
counter.out(11121)
counter.out(11111)
counter.out(1111)
counter.withdraw_history()