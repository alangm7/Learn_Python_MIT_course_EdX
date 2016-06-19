

"""Write a function called item_order that takes as input a string named order. The string contains only words for the items the customer can order separated by one space. """


from collections import Counter

def item_order(order, items=('salad', 'hamburger', 'water')):
    counter = Counter(order.split())
    return ' '.join(['{}: {}'.format(item, counter.get(item, 0))
    for item in items])
print (item_order('water water salad salad'))
