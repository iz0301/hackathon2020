import time
import datetime
import pickle
#Define the mechanism to save posts' data to a file:
def save_postdata(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

#Class to generate a post and its data:
class genPost:
    author = None
    likes = 0
    addedLikes = 0
    loans = 0
    addedLoans = 0
    epoch_sec = 0
    date = ""
    text = ""
    def __init__(self, author, text):
        self.author = author
        self.text = text
    #Get the time (since epoch) that we ran this script/instantiated this class, and then turn this into a date posted string:
    import time
    import datetime
    epoch_sec = time.time()
    date = datetime.datetime.fromtimestamp(epoch_sec)

#Generate a post:
post1 = genPost("Clark V", "Hello World")
#Checks:
print(post1.author)
print(post1.text)
#print(post1.time) #Will be a large integer (seconds since 1970)
print(post1.date)
#print(post1.likes) #Should be zero, for now

#Save the post:
save_postdata(post1, 'post1.pkl')

#Now, I have begun to look into CGI: Common Gateway Interface, to convert a user's website interactions to the nedded variables to make the post.