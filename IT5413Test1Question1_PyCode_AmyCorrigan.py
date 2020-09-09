# since it's a single user
# setting a hard coded username and password
uName = 'user1'
pWord = 'password123!@#'

# having user enter the username
# setting to string to accept all type of chars/num/symbols/etc
enterUserName = str(input('Please enter your username: '))

# having user enter the password
# setting to string to accept all type of chars/num/symbols/etc
enterPassWord = str(input('Please enter your password: '))
# checking to see if the uname and pwrd combination are exactly the same
if (enterUserName == uName) and (enterPassWord == pWord):
   print('You are now logged in')                   #WE HAVE A MATCH
else:
   print('You have entered the wrong username/password combination')  #NO MATCH