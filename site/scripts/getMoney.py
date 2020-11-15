#------------------------------------------------------------------------------
#Aside: Check all cookies
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
#------------------------------------------------------------------------------
loans = []
file1 = open('/var/www/hack2020/'+username+'/'+'loans_received.txt', r)
lines = file1.readLines()
for line in lines():
    loans[i] = json.loads(line)
amt_money = sum(loans['amt_money'])
print(amt_money)