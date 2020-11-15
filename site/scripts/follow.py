#!/usr/bin/python3 -u
import cgi
import cgitb
import json
import sys


cgitb.enable()
print("Content-Type: text/html\n\n")

form = cgi.FieldStorage()
if "username" not in form:
    print("username not in form")
    sys.exit(0)

value = form.getlist("username")
print(value)
following = ",".join(value)


