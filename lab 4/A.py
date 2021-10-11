n = int(input())
nechet_sum = 0
chet_pr = 1
otr_sum = 0
pol_pr = 1
for i in range(n):
	x = int(input())
	if x % 2 != 0:
		nechet_sum += x
	else:
		chet_pr = chet_pr * x
	if x >= 0:
		pol_pr = pol_pr * x
	else:
		otr_sum += x
print(nechet_sum, chet_pr, otr_sum, pol_pr)
