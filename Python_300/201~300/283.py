class Car:
    def __init__(self,ti,price):
        self.ti=ti
        self.price=price

class Sedan(Car):
    pass
c=Sedan(2,1000)
print(c.ti,c.price)
