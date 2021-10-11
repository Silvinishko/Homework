for i in range(1, 5001):
	d = 2
	summ  = 1
	while d*d < i:
		if i % d == 0:
			summ += d + i//d
		d += 1
	if d**2 == i:
		summ += d
	if summ == i:
		print(sum)