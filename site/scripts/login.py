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
username_in = form['username'].value
password_in = form['password'].value

#Check these against a user folder:
passwordfilename = '/var/www/hack2020/'+username_in+'/'+'password.txt'
with open(passwordfilename, 'r') as file:
    password_from_file = file.read()

if password_from_file.strip() == password_in.strip():
    print("Login successful, " + username_in)
else:
    print("Login unsuccessful, " + username_in)   
