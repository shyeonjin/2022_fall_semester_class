# **********************************
# 문제이해를 못함
import numpy as np

squr = 5
area = 3

land = [[1, 0, 0, 1, 0],
          [0, 1, 0, 0, 1],
          [0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 1, 0, 0]]

s = 0
for i in range(squr - area + 1):
    for j in range(area):
        if np.sum(land[i:area+i, j:area+j]) > s: 
            s = np.sum(land[i:area+i, j:area+j])
print(s)