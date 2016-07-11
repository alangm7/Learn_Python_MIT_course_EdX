"""Write a Python function that returns True if aString is a palindrome (reads the same forwards or reversed) and False otherwise. Do not use Python's built-in reverse function or aString[::-1] to reverse strings.

This function takes in a string and returns a boolean."""


def isPalidrome(word):
	result = {}
	x = len(word) - 1
	
	for i in range(len(word)):
		result[i] = word[(i - x) * (-1)]
		final = "".join(result.values())
	if final == word:
		print (True)
	else:
		print (False)
			
isPalidrome('ana')
