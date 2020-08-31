import sys
t = int(input())

for _ in range(t):

	n = int(input())

	l = list(map(int, input().split(" ")))

	d = dict()

	for i in l:

		if i not in d:
			d[i] = 0

		d[i] += 1

	a = dict()

	for i in d:

		if d[i] not in a:

			a[d[i]] = 0

		a[d[i]] += 1

	lmax = sys.minsize 
	lmin = sys.maxsize

	for i in a:

		if lmax <= a[i]:

			lmax = a[i]

			if i < lmin:
				lmin = i

	print(lmin)