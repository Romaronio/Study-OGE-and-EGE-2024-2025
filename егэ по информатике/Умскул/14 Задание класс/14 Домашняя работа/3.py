s = 1024 ** 789 + 256 ** 678 - 64 ** 567
k = 0
while s > 0:
	if s % 5 == 4:
		k += 1
	s //= 5
print(k)