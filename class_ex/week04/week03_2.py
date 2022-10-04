import numpy as np

with open('list.txt','r',encoding='UTF-8') as o:
    total=np.array(list(map(int,o.readlines())))
    print("min: {} max: {}".format(total.min(),total.max()))
