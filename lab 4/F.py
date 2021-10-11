n = 5
l = 2*n + 1
nol = 0
for i in range(1, l+1, 2):
	nol = (l-i)//2
	print('*' * nol, '0' * i, '*' * nol)
for i in range(l-2, 0, -2):
	nol = (l-i)//2
	print('*' * nol, '0' * i, '*' * nol)
