#!/usr/bin/python3 -u
import cgi
import cgitb
import sys
import os

cgitb.enable()

form = cgi.FieldStorage()
if "username" not in form or "password" not in form:
    print('Set-Cookie: username=');
    print('Set-Cookie: password=');
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
    save_password(password, '/var/www/hack2020/'+username+'/'+'password.txt')
 else:
 	print('You are already signed up. Contact an administrator if you forgot your password.')

#Now, log them in straight away:
#A check: print("Hello " + form['username'].value +" "+ form['lastname'].value)

#Check the username and password against a user folder:
passwordfilename = '/var/www/hack2020/'+username+'/'+'password.txt'
with open(passwordfilename, 'r') as file:
    password_from_file = file.read()

if password_from_file.strip() == password.strip():
    #print("Login successful, " + username_in)
    print('Set-Cookie: logged_in=1');
    print('Set-Cookie: username=' + username);
    print('Set-Cookie: password=' + password.strip());
else:
    #print("Login unsuccessful, " + username_in)
    print('Set-Cookie: logged_in=0');
    print('Set-Cookie: username=' + username);
    print('Set-Cookie: password=' + password.strip());


print("Content-Type: text/html\n\n")
