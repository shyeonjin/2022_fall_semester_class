class Car:
    def __init__(self,ti,price):
        self.ti=ti
        self.price=price
    def ideal(self):
        print("바퀴수 ", self.ti)
        print("가격 ", self.price)


class Sedan(Car):
    def __init__(self,ti,price):
        super().__init__(ti,price)
class SUV(Car):
     def __init__(self,ti,price,name):
        super().__init__(ti,price)
        self.name=name
c=SUV(4,1000,'시마노')
c.ideal()