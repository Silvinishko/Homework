from math import factorial

n = int(input())
summ = 0
for i in range(1, n+1):
	summ += factorial(i-1)**2/factorial(2*i)
print(summ)