import pickle
#Define the mechanism to save signup data to a file:
def save_signupdata(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

#Class to generate a new user and its data ("Signing up"):
class signup:
    username = ""
    password = ""
    email = ""
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

#Sign up the user:
user1 = signup("clarkvan33", "passwordlol", "clarkvan33@gmail.com")
#Checks:
print(user1.username)

#Save the post:
save_signupdata(user1, 'user1.pkl')

#Now, I have begun to look into CGI: Common Gateway Interface, to convert a user's website interactions to the nedded variables to make the post.