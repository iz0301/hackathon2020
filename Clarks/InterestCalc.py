# This program calculates repayments on an interest rate loan/mortgage.

principal = input("How much is the initial loan amount(in $)? \n")
interestPercent = input("What is the agreed-upon yearly interest rate (in %)? \n")
interval = input("Will this rate compound each week, month, or year? \n")
repayLength = input("How many years will the interest accrue? \n")

#converting the string input variables to float
principal = float(principal)
interestPercent = float(interestPercent)
repayLength = float(repayLength)

#Convert the interest rate to a decimal number
interestRate = interestPercent / 100

#A check:
#print(interestRate)

#working out the number of payments per year over the course of the loan period.
if (interval == "week"):
    numPayments = 365.2422/7
elif (interval == "month"):
    numPayments = 12
elif (interval == "year"):
    numPayments = 1
elif (interval == "continuously"):
    numPayments = "continuous" #Not yet implemented below
else:
    print("Invalid interval of payments. Try again.")

#Formula
#A = P((1+r/n)^(n*t))

#   A = Total Repayment (totalPay)
#   P = Principal Loan Amount (principal)
#   r = Annual Interest Rate, as a decimal (interestRate)
#   n = Number of Payments per unit t [i.e. years] (numPayments)
#   t = Length of the loan [in years] (repayLength)

totalPay = principal*((1+interestRate/numPayments)**(numPayments*repayLength))

#Now divide this by the total number of payments over all the years of the load to find the payment in each interval:
intervalPay = totalPay/(numPayments*repayLength)

print("You will borrow $" + str(principal) + " and pay it back over " + str(repayLength) + " years, with a yearly interest rate of " + str(interestPercent) + "%.")

print("Repayments will occur each " + interval + ", so there will be %.2f payments in all." % (numPayments*repayLength))

print("Each repayment will be $%.2f." % intervalPay)

print("The total charge/payment for this loan (including paying back the initial amount) will be $%.2f." % totalPay)

#Things left to tweak:
#Output the dollar values with the correct decimals for cents
#Output the number of payments as a whole number? This might not work for every case of payment type.
#How to run this file in terminal: cd into correct directory for this script, then write ipython interestCalc.py