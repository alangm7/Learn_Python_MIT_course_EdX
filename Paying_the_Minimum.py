"""Write a program to calculate the credit card balance after one year if a person
only pays the minimum monthly payment required by the credit card company each month."""

balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthly_interest_rate = (annualInterestRate / 12.0)
monthly_payment_lower = balance / 12
monthly_payment_upper = round((balance * ( 1 + monthly_interest_rate)**12)/12.0, 2)
monthly_payment = round((monthly_payment_lower + monthly_payment_upper) / 2.0, 2)
updated_balance = balance


while updated_balance > -0.01 and updated_balance < 0.01 :
    monthly_payment = round((monthly_payment_lower + monthly_payment_upper) / 2.0, 2)
    updated_balance = balance
    for month in range(1, 13):
        updated_balance -= monthly_payment
        updated_balance = round(updated_balance + (monthly_interest_rate * updated_balance), 2)
    if updated_balance < 0.01:
        monthly_payment_upper = monthly_payment
        #monthly_payment = round((monthly_payment_lower + monthly_payment_upper) / 2.0, 2)
    elif updated_balance > 0.01:
        monthly_payment_lower = monthly_payment
        #monthly_payment = (monthly_payment_lower + monthly_payment_upper) / 2.0
   
print "Lowest Payment: %.2f" % monthly_payment
