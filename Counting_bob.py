s = 'bobobaeiou'
numBobs = 0

for char in s:
	if char == 'b' and char == 'o' and char == 'b':
		numBobs += 1

print ('Number of times bob occurs is: ' + str(numBobs))
