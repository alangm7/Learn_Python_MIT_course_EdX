"""Write a program to calculate the credit card balance after one year if a person
only pays the minimum monthly payment required by the credit card company each month."""

balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

minPayment = ''  
totalPaid = 0
month = 1
while month <= 12:
    minPayment = monthlyPaymentRate * balance
    balance -=  minPayment 
    balance += (annualInterestRate/12.0)*balance 
    print 'Month:' + str(month)
    print 'Minimum monthly payment:'+ str(round(minPayment,2)) 
    print 'Remaining balance:' + str(round(balance,2)) 
    totalPaid += minPayment
    month += 1
print 'Total paid:'+ str(round(totalPaid,2))
print 'Remaining balance:' + str(round(balance,2) )
