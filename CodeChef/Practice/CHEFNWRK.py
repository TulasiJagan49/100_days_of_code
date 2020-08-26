def round_trips(n, k, l):

    for j in l:
        if j > k:
            return -1
    i = 0
    while i < n:
            trips += 1
            current_weight = 0
            while i < n and current_weight + l[i] <= k:
                current_weight += l[i]
                i += 1

    return trips

t = int(input())

for _ in range(t):
    
    n, k = map(int, input().split(" "))
    l = list()
    
    if n == 1:
        l.append(int(input()))
    else:
        for i in map(int, input().split(" ")):
            l.append(i)
    
    print(round_trips(n, k, l))
    