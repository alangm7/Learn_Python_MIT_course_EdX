#Problem set week 2, counting vowels in string

s = 'aeiou'
numVowels = 0

for char in s:
	if char == 'a' or char == 'e' or char == 'i' \
		or char == 'o' or char == 'u':
		numVowels += 1

print ('Number of vowels is: ' + str(numVowels))
