land = [[0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0]]
def solution(land):
    long = len(land[0])
    high = len(land)
    sum = [[0] * long for i in range(len(land))]
    for i in range(0, high):
        for j in range(0, long):
            if land[i][j] == 0:
                sum[i][j] = 1
            else:
                sum[i][j] = 0
    
    for i in range(1, high):
        for j in range(1, long):
            if sum[i][j] == 1:
                sum[i][j] = min(sum[i-1][j-1], min(sum[i-1][j], sum[i][j-1])) + 1

    maxValue = 0
    x = 0
    y = 0
    for i in range(0, high):
        for j in range(0, long):
            if maxValue < sum[i][j]:
                maxValue = sum[i][j]
                x = i
                y = j
    print(maxValue, x, y)
    print(maxValue, 'X', maxValue)
    for i in range(x - (maxValue - 1), x + 1):
        for j in range(y - (maxValue - 1), y + 1):
            land[i][j] = '#'
    return land
solution(land)