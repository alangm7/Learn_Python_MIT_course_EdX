'''Write a function called getSublists,
which takes as parameters a list of integers named L and an integer named n
'''

def getSublists(L, n):
    sub = []
    for i in range(len(L) - n + 1):
        sub.append(L[i:i+n])
        # print L[i:i+n]
    return sub
