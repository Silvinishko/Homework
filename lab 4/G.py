n = int(input())
l = 2*n + 1
nol = 0
for i in range(1, l, 2):
	nol = (l - i) // 2
	print(' ' * (l // 2), '*' * i, ' ' * nol)
for i in range(1, l, 2):
	nol = (l - i)//2
	print(' ' * nol, '*' * i, ' ' * nol, end = '')
	print(' ' * (nol - 1), '*' * i, ' ' * nol)

