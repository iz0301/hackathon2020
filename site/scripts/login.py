#!/usr/bin/python3 -u

import cgi
import cgitb
import sys

cgitb.enable()
print("Content-Type: text/html\n\n")

form = cgi.FieldStorage()
if "username" not in form or "password" not in form:
    print("<H1>Error</H1>")
    print("Please fill in the username and password fields.")
    sys.exit(0)

#A check: print("Hello " + form['username'].value +" "+ form['lastname'].value)
username_in = form['username']
password_in = form['password']

#Check these against a user folder:
passwordfilename = username_in+'.'+password_in+'.txt'
if passwordfilename = password_in:
	print("Login successful," + username_in)

