def g(s, p, end):
	if s >= 56 and p == end:
		return True
	if s < 56 and p == end:
		return False
	if s >= 56 and p != end:
		return False
	if (p + 1) % 2 == (end % 2):
		return g(s + 1, p + 1, end) or g(s * 3, p + 1, end)
	else:
		return g(s + 1, p + 1, end) or g(s * 3, p + 1, end)
for s in range(1, 57):
	if g(s, 0, 2):
		print(s)