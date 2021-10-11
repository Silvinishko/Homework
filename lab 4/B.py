n = int(input())
x = int(input())
a = []
s = 0
for i in range(n):
	a.append(int(input()))
for j in range(n+1):
	s += a[j] * x**j
print(s)

