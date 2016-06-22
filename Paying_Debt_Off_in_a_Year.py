"""Now write a program that calculates the minimum fixed
monthly payment needed in order pay off a credit card balance within 12 months.
By a fixed monthly payment,
we mean a single number which does not change each month,
but instead is a constant amount that will be paid each month.
"""

balance = 3329
annualInterestRate = 0.2

minPayment = 0
newBalance = balance
while newBalance > 0:
    newBalance = balance
    minPayment += 10
    for month in range(12):
        newBalance -= minPayment
        newBalance *= (1 + (annualInterestRate / 12))
print("Lowest payment: {0:d}".format(minPayment))
