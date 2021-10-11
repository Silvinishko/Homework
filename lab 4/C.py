import math
otvet = 0
x = float(input())
n = int(input())
for i in range(n):
	otvet = math.cos(x + otvet)
print(otvet)