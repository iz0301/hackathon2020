#!/usr/bin/python3 -u
import sys
import os
import pickle
import json

print('Content-Type: text/html\n\n')

#Read the cookies that have been established:
handler = {} # A dictionary which will house the cookie names and cookie values
if 'HTTP_COOKIE' in os.environ:
    cookies = os.environ['HTTP_COOKIE']
    cookies = cookies.split('; ')
    for cookie in cookies:
        cookie = cookie.split('=')
        handler[cookie[0]] = cookie[1]
#handler now has all 3 cookies we want.
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


#Define the mechanism to show posts, sorted by time:
#Assume all users all following all users (for now):
def show_jsonPosts(usernames): #If the assumption is dropped, a 'following' list would go here, too, to determine the usernames to loop through.
    #Note: 'usernames' is the list of all usernames whose posts you want to see
    #Returns: posts: a list of all the posts to be shown in the feed, in JSON format
    posts = []
    for u in usernames: #Each line of the usernames text file; or just a usernames array, as we will define it for now.
        print('test1')
        dirname = '/var/www/hack2020/'+u+'/posts/'
        for j in range(1, 1 + len(os.listdir(dirname))):
            with open(dirname+'post'+str(j), 'rb') as f:
                data = pickle.load(f)
                post = json.dumps(data)
                posts.append(post)
    return posts

#Collect the posts:
#For now, define the list of all usernames:
usernames = ['clarkvan33', 'caldrich', 'sylvia', 'isaac']
feed_posts = show_jsonPosts(usernames)
print(feed_posts)
