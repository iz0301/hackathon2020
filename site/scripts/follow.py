#!/usr/bin/python3 -u
import cgi
import cgitb
import json

cgitb.enable()

print('hello world')

form = cgi.FieldStorage()
print(form)
value = form.getlist("username")
following = ",".join(value)

print("Content-Type: text/html\n\n")
