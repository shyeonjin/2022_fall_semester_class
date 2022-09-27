import math
def diff_sin(x):
    return math.cos(x)

def pi_chag(x):
    k=int(x[x.find("/")+1:])
    total=math.pi/k
    #print(put,type(put))
    return total

put=input("문자를 입력하세요")
if 'pi' in put:
    put=pi_chag(put)
put=float(put)
print(diff_sin(put))