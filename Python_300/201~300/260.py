'''
아래와 같은 에러가 발생한 원인에 대해 설명하세요.

class OMG : 
    def print() :
        print("Oh my god")

>>> >>> myStock = OMG()
>>> myStock.print()
TypeError Traceback (most recent call last)
<ipython-input-233-c85c04535b22> in <module>()
----> myStock.print()

TypeError: print() takes 0 positional arguments but 1 was given
'''
# >>> >>>사용하였기에 에러
class OMG : 
    def print() :
        print("Oh my god")

myStock = OMG()
myStock.print()