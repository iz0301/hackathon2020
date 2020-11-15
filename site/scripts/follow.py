#!/usr/bin/python3 -u
import cgi
import cgitb
import json

cgitb.enable()

if "username" not in form:
    print("Content-Type: text/html\n\n")
    sys.exit(0)

form = cgi.FieldStorage()
print(form)
value = form.getlist("username")
following = ",".join(value)

print("Content-Type: text/html\n\n")
