'''
Write a function called dict_invert that takes in a dictionary
with immutable values and returns the inverse of the dictionary
'''

def dict_invert(d):

    inv = {}
    for k, v in d.iteritems():
        keys = inv.setdefault(v, [])
        keys.append(k)
    for key in inv.keys():
        inv[key].sort()
    return inv
