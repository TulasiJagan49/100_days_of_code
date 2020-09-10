# This program gives the first and last occurence of an element in
# a sorted array.

def binary_search_fo(l, n):
    low = 0
    high = len(l) - 1
    result = -1
    while (low <= high):
        mid = low + ((high - low) // 2)
        if l[mid] == n:
            result = mid
            high = mid - 1
        elif l[mid] < n:
            low = mid + 1
        else:
            high = mid - 1
    return result

def binary_search_lo(l, n):
    low = 0
    high = len(l) - 1
    result = -1
    while (low <= high):

        mid = low + ((high - low) // 2)

        if l[mid] == n:
            result = mid
            low = mid + 1
        elif l[mid] < n:
            low = mid + 1
        else:
            high = mid - 1
    return result

def binary_search(arr, x):

    l = 0
    h = len(arr) - 1

    while (l <= h):
        mid = l + (h - l) // 2
        print(mid)
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            h = mid - 1
    
    return -1

t = int(input())  # Reading the no.of testcases

for _ in range(t):

    n = int(input()) # Element for which first and last index has to be found
                     # in a sorted array.

    l = list(map(int, input().rstrip().split(" ")))

    res = list()

    res.append(binary_search_fo(l, n))
    res.append(binary_search_lo(l, n))

    print(res)