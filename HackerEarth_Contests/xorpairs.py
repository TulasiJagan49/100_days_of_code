t = int(input().rstrip())

for _ in range(t):

    arr = list(map(int, input().rstrip().split(" ")))

    k = int(input()) + 1

    d = {i:0 for i in range(k)}

    s = set()

    for i in arr:

        for j in range(k):

            if (j ^ i) in s:
                d[j] += 1

        s.add(i)
            
    print(' '.join(str(d[i]) for i in d))
