"""A catering company has hired you to help with organizing and preparing customer's orders. You are given a list of each customer's desired items, and must write a program that will count the number of each items needed for the chefs to prepare. The items that a customer can order are: salad, hamburger, and water."""

Write a function called item_order that takes as input a string named order. The string contains only words for the items the customer can order separated by one space. The function returns a string that counts the number of each item and consolidates them in the following order: salad:[# salad] hamburger:[# hambruger] water:[# water]

If an order does not contain an item, then the count for that item is 0. Notice that each item is formatted as [name of the item][a colon symbol][count of the item] and all item groups are separated by a space.


from collections import Counter

def item_order(order, items=('salad', 'hamburger', 'water')):
    counter = Counter(order.split())
    return ' '.join(['{}: {}'.format(item, counter.get(item, 0))
    for item in items])
print (item_order('water water salad salad'))
