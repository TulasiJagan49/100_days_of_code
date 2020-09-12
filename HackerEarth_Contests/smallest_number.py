def count_factors(x):
    i = 1

    count = 0

    while i * i <= x:

        if x % i == 0:
            count += 1
            if x // i != i:
                count += 1
        i += 1
    
    return count % 2
t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    p = count_factors(n)
    n += 1
    while True:
        if p != count_factors(n):
            print(n)
            break
        n += 1
    


