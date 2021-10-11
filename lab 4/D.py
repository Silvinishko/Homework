n = int(input())
x = float(input())
summ = 0
pr = 1
for i in range(1, n+1):
	pr *= (x+i)
	summ += pr
print(summ)