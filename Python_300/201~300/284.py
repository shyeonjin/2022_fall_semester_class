class Car:
    def __init__(self,ti,price):
        self.ti=ti
        self.price=price

class Sedan(Car):
    def __init__(self,ti,price,name):
        self.ti=ti
        self.price=price
        self.name=name

c=Sedan(2,100,"시마노")
print(c.name)