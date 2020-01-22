import sys
flag = False
for line in sys.stdin:
	a = []
	for i in line:
		# print(i)
		if i == "\"":
			if not flag:
				a.append("``")
				flag = True
			else:
				a.append("''")
				flag = False
		else:
			a.append(i)
	print(''.join(a))