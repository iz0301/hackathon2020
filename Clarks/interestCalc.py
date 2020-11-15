#!/usr/bin/python3 -u
import cgi
import cgitb
import json
import sys
import os

cgitb.enable()
print("Content-Type: text/html\n\n")

form = cgi.FieldStorage()
if "amt_money" not in form or "interestPercent" not in form or "don_or_loan" not in form or "repay_Length" not in form or "to" not in form:
    print("field not in form")
    sys.exit(0)

#A check: print("Hello " + form['username'].value)
amt_money = form['amt_money'].value
interestPercent = form['interestPercent'].value
don_or_loan = form['don_or_loan'].value
repayLength = form['repayLength'].value
to = form['to'].value
#Convert the numerical values to floats:
amt_money = float(amt_money)
interestPercent = float(interestPercent)
repayLength = float(repayLength)

#Define the mechanism to save loans' data to the correct files:
def save_data(objs, objsfilename, dirname):
	#Dir name will be the username folder, since all our stats are text files within that folder
	#objsfilename will be a single financial file probably
	for i in len(range(objs)):
		filename = dirname + str(objsfilename[i]) + '.txt'
		f = open(filename,'w')
		f.write(obj)
		f.close()


#Define the function to calculate the financial data from the inputs:
def calc_amounts(amt_money, interestPercent, don_or_loan, repayLength):
	# This program calculates repayments on an interest rate loan/mortgage, and stores the stats in a dictionary
	if(don_or_loan == 'Donation')
		totalPay = 0
		numPayments = 0
		repayLength = 0
		intervalPay = 0
	

	interval = "month"
	#Could have options, but hard coded is easier
	#Convert the interest rate to a decimal number:
	interestRate = interestPercent / 100

	#working out the number of payments per year over the course of the loan period.
	if (interval == "week"):
	    numPayments = 365.2422/7
	elif (interval == "month"):
	    numPayments = 12
	elif (interval == "year"):
	    numPayments = 1
	else:
	    print("Invalid interval of payments. Try again.")
	    sys.exit(0)

	#Formula
	#A = P((1+r/n)^(n*t))

	#   A = Total Repayment (totalPay)
	#   P = Principal Loan Amount (principal)
	#   r = Annual Interest Rate, as a decimal (interestRate)
	#   n = Number of Payments per unit t [i.e. years] (numPayments)
	#   t = Length of the loan [in years] (repayLength)

	totalPay = amt_money*((1+interestRate/numPayments)**(numPayments*repayLength))

	#Now divide this by the total number of payments over all the years of the load to find the payment in each interval:
	intervalPay = totalPay/(numPayments*repayLength)

	




	print("You will borrow $" + str(amt_money) + " and pay it back over " + str(repayLength) + " years, with a yearly interest rate of " + str(interestPercent) + "%.")

	print("Repayments will occur each " + interval + ", so there will be %.2f payments in all." % (numPayments*repayLength))

	print("Each repayment will be $%.2f." % intervalPay)

	print("The total charge/payment for this loan (including paying back the initial amount) will be $%.2f." % totalPay)












#------------------------------------------------------------------------------
#Aside: Check all cookies
#Read the cookies that have been established:
handler = {} # A dictionary which will house the cookie names and cookie values
if 'HTTP_COOKIE' in os.environ:
    cookies = os.environ['HTTP_COOKIE']
    cookies = cookies.split('; ')
    for cookie in cookies:
        cookie = cookie.split('=')
        handler[cookie[0]] = cookie[1]
#handler now has all 3 cookies we want.
#Now, do checks with these cookies:
username = ""
if 'logged_in' in handler and handler['logged_in'] == '1': #(Checked if logged in)
    with open('/var/www/hack2020/'+handler['username']+'/'+'password.txt','r') as file:
        fp = file.read()

    if handler['password'].strip() == fp.strip():
        username = handler['username']
    else:
        print('Wrong password!')
        quit()
else:
    print('not logged in')
    quit()
#------------------------------------------------------------------------------
calc_amounts(amt_money, interestPercent, don_or_loan, repayLength)
#Now that we have all the stats and the interest for the loan, save the data to the correct files:
dirname = '/var/www/hack2020/'+username+'/'
save_data([amt_money, interestPercent, ], ['following.txt',])
#(not finished yet)