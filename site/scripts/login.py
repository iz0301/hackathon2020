#!/usr/bin/python3 -u

import cgi
import cgitb
import sys

cgitb.enable()
#print 'Set-Cookie: lastvisit=' + str(time.time());

form = cgi.FieldStorage()
if "username" not in form or "password" not in form:
    print('Set-Cookie: username=');
    print('Set-Cookie: password=');
    print("Content-Type: text/html\n\n")
    sys.exit(0)


#A check: print("Hello " + form['username'].value +" "+ form['lastname'].value)
username_in = form['username'].value
password_in = form['password'].value

#Check these against a user folder:
passwordfilename = '/var/www/hack2020/'+username_in+'/'+'password.txt'
with open(passwordfilename, 'r') as file:
    password_from_file = file.read()

if password_from_file.strip() == password_in.strip():
    #print("Login successful, " + username_in)
    print('Set-Cookie: logged_in=1');
    print('Set-Cookie: username=' + username_in);
    print('Set-Cookie: password=' + password_in.strip());
else:
    #print("Login unsuccessful, " + username_in)
    print('Set-Cookie: logged_in=0');
    print('Set-Cookie: username=' + username_in);
    print('Set-Cookie: password=' + password_in.strip());


print("Content-Type: text/html\n\n")
