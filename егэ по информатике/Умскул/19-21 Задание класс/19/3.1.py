def g(x, s, p, end):
	if (x + s) >= 156 and p == end:
		return True
	if (x + s) < 156 and p == end:
		return False
	if (x + s) >= 156 and p != end:
		return False
	return (g(x, s + 2, p + 1, end) or g(x, s * 5, p + 1, end) or g(x + 2, s, p + 1, end) or g(x * 5, s, p + 1, end))
x = 5 
for s in range(1, 151):
	if g(x, s, 0, 1):
		print(s)
		break


