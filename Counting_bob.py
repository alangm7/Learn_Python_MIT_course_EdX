s = 'azcbobobegghakl'
bobs = ''
count = 0
for char in s:
    if char == 'b':
        bobs = 'b'
    if char == 'o':
        bobs = 'bo'
        if char == 'b':
            bobs = 'bob'
            if bobs == 'bob':
                count += 1
print ('Number of times bob occurs is: ' + str(count))
