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


#A check: print("Hello " + form['username'].value)
username = form['username'].value
password = form['password'].value
amt_money = 1000 #Default starting money value - substitute for linking your bank account

#Define the mechanism to save posts' data to a file:
def save_data(obj, filename):
	f = open(filename,'w')
	f.write(obj)
	f.close()

#If the username folder is not created yet, create it, and create the password.txt and amt_money.txt files. Also, make the posts directory:
if not os.path.exists('/var/www/hack2020/'+username+'/'):
    os.mkdir('/var/www/hack2020/'+username+'/')
    os.mkdir('/var/www/hack2020/'+username+'/posts/')
    save_data(password, '/var/www/hack2020/'+username+'/'+'password.txt')
    save_data(amt_money, '/var/www/hack2020/'+username+'/'+'amt_money.txt')
else:
    print("Content-Type: text/html\n\n")
    print('You are already signed up. Contact an administrator if you forgot your password. Otherwise, we will log you in now.')
    quit()

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
