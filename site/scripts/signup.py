#!/usr/bin/python3 -u
import cgi
import cgitb
import sys
import os

cgitb.enable()

form = cgi.FieldStorage()
if "username" not in form or "password" not in form:
    print("Content-Type: text/html\n\n")
    sys.exit(0)

print("Content-Type: text/html\n\n")

#A check: print("Hello " + form['username'].value)
username = form['username'].value
password = form['password'].value

#Define the mechanism to save posts' data to a file:
def save_password(obj, filename):
	f = open('filename','w')
	f.write(password)
	f.close()


#If the username folder is not created yet, create it, and the password.txt file:
if not os.path.exists('/var/www/hack2020/'+username+'/'):
    os.mkdir('/var/www/hack2020/'+username+'/')
    save_password(password, '/var/www/hack2020/'+username+'/'+'password.txt'')