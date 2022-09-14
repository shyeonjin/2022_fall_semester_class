class Car:
    def __init__(self,ti,price):
        self.ti=ti
        self.price=price

class Sedan(Car):
    def __init__(self,ti,price):
        self.ti=ti
        self.price=price
    def ideal(self):
        print("바퀴수 ", self.ti)
        print("가격 ", self.price)

c=Sedan(4,1000)
c.ideal()