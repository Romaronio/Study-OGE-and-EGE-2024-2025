def g(s, p, end):
	if s >= 88 and p == end:
		return True
	if s < 88 and p == end:
		return False
	if s >= 88 and p != end:
		return False
	if (p + 1) % 2 == end % 2:
		g(s + 2, p + 1, end) or g(s + 3, p + 1, end) or g(s * 2, p + 1, end)
	else:
		g(s + 2, p + 1, end) and g(s + 3, p + 1, end) and g(s * 2, p + 1, end)
for s in range(1, 88):
	if g(s, 0, 3):
		print(s)