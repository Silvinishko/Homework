n = int(input())
otvet =  0
if n % 2 == 0:
	for i in range(2, n + 1, 2):
		otvet *= i
else:
	for j in range(1, n + 1, 2):
		otvet *= j
print(otvet)