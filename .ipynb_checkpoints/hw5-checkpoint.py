import numpy as np

#1 The Odd Ones Out ????!?!!?!
def onlyOdd(arr):
    odds = np.array()
    for cluster in arr:
        test = np.array()
        for num in cluster:
            if num % 2 != 0:
                test.append(num)
            continue
        if len(test) == 3:
            odds.append(test)
        continue
    print(odds)

# Let's Play Checkers!
def checkerboard():
    arr = np.zeros((8, 8))
    print(arr)
checkerboard()