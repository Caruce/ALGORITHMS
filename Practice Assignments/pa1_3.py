
def trans(x):
	if x == 1 or x == 0:
		return x
	else: 
		print(x%2)
		return trans (x//2)

print(trans(5))