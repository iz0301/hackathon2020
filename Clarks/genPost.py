import time
import datetime
import pickle
import numpy as np
#Define the mechanism to save posts' data to a file:
def save_postdata(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

#Class to generate a post and its data:
class genPost:
    author = ""
    content = ""
    interestPercent = 0
    postID = 0
    likes = 0
    whoLiked = []
    loans = {}
    whoLoaned = []
    date = ""
    epoch_sec = 0
    
    def __init__(self, author, content, interestPercent):
        self.author = author
        self.content = content
        self.interestPercent = interestPercent
        #Get the time (since epoch) that we ran this script/instantiated this class, and then turn this into a "date posted" string:
        epoch_sec = time.time()
        date = datetime.datetime.fromtimestamp(epoch_sec)
        postID = len(os.listdir('/var/www/hack2020/'+author+'/post/')) + 1
        self.date = date
        self.postID = postID


#Generate a post:
username_in = "clarkvan33" #Ideally this will be acheived with cookies, not this manual input
post1_content = "Hello World - Give me money pls"
post1 = genPost(username_in, post1_content, 5)
#Checks:
#print(post1.text)
#print(post1.date)

#Save the post:
save_postdata(post1, '/var/www/hack2020/'+post1.author+'/post'+post1.post_id+'.pkl')