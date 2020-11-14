#!/usr/bin/python3 -u
import cgi
import cgitb
import sys
import os
import time
import datetime
import pickle
#import numpy as np

cgitb.enable()

form = cgi.FieldStorage()
if "content" not in form or "interestPercent" not in form:
    print("Content-Type: text/html\n\n")
    sys.exit(0)

print("Content-Type: text/html\n\n")

#A check: print("Hello " + form['username'].value)
content_in = form['content'].value
interestPercent_in = form['interestPercent'].value

#Read the cookies that have been established:
handler = {}
if 'HTTP_COOKIE' in os.environ:
    cookies = os.environ['HTTP_COOKIE']
    cookies = cookies.split('; ')
    for cookie in cookies:
        cookie = cookie.split('=')
        handler[cookie[0]] = cookie[1]
#Hopefully, handler now has all 3 cookies we want.
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

#Define the mechanism to save posts' data to a file:
def save_postdata(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

#Class to generate a post and its data:
class genPost:
    username = ""
    content = ""
    principal = 0
    interestPercent = 0
    postID = 0
    likes = 0
    whoLiked = []
    loans = {}
    whoLoaned = []
    date = ""
    epoch_sec = 0
    
    def __init__(self, username, content, interestPercent):
        self.username = username
        self.content = content
        self.interestPercent = interestPercent
        #Get the time (since epoch) that we ran this script/instantiated this class, and then turn this into a "date posted" string:
        epoch_sec = time.time()
        date = datetime.datetime.fromtimestamp(epoch_sec)
        postID = len(os.listdir('/var/www/hack2020/'+username+'/posts/')) + 1
        self.date = date
        self.postID = postID

#If the posts folder is not created yet, create it:
if not os.path.exists('/var/www/hack2020/'+username+'/posts/'):
    os.mkdir('/var/www/hack2020/'+username+'/posts/')

#Generate a post:
post = genPost(username, content_in, interestPercent_in)
#Checks:
#print(post.text)
#print(post.date)

#Save the post:
save_postdata(post, '/var/www/hack2020/'+post.username+'/posts/post'+str(post.postID)+'.pkl')
