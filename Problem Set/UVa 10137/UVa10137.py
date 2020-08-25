while True:
	n = int(input())
	if not n:
		break
	l = list()
	lsum = 0
	for _ in range(n):
		m = float(input())
		l.append(m)
		lsum += m
	lsum = round((lsum) / n, 2)
	gsum = 0
	rsum = 0
	for ex in l:
		if ex < lsum:
			gsum += lsum - ex
		else:
			rsum += ex - lsum
	print("${price:.2f}".format(price = min(rsum, gsum)))