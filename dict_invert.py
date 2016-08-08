'''
Write a function called dict_invert that takes in a dictionary
with immutable values and returns the inverse of the dictionary
'''

def dict_invert(d):

    inv = {}
    for x, y in d.iteritems():
        keys = inv.setdefault(y, [])
        keys.append(x)
    for key in inv.keys():
        inv[key].sort()
    return inv
