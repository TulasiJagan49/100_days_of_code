# print(sys.getrecursionlimit())
import sys
cycle_dict = {}

def cycle(k):

    if k in cycle_dict:
        # print("In if condition")
        return cycle_dict[k]
    elif k == 1:
        # print("In elif one condition")
        return 1
    elif k%2 == 1:
        # print("In elif odd condition")
        return 1 + cycle(3 * k + 1)
    else:
        # print("In else condition")
        return 1 + cycle(k >> 1)
for line in sys.stdin:
    i, j = map(int, line.strip().split())
    swap = 0
    if (i > j):
        swap = 1
        i, j = j, i

    max_cycle = 0

    for k in range(i, j + 1):
        m = cycle(k)
        # print(m)   
        cycle_dict[k] = m
        # print(cycle_dict)
        if (max_cycle < m):
            max_cycle = m
    if swap:
        print(j, i, max_cycle)
    else: 
        print(i, j, max_cycle)