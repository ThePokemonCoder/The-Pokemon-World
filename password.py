print('this is a test subject for password auth')
username = input('Please enter your username: ')
if username == 'admin':
    print('correct you may access')
    password = input('Please enter your password: ')
    if password == 'pizzeyum3':
        print('You may enter')
        
    else:
        print('Try Again')
else:
    print('wrong')