import getpass
database = {'apple': '67295', 'banana': '372502', 'orange':'1011'}
username = input('Enter Your Username: ')
password = getpass.getpass('Enter Your Password: ')
tries = 1
for i in database.keys():
    if username == i:
        print(f'{i}... ', end='')
        while (password != database.get(i)) and (tries < 3):
            password = getpass.getpass('Enter Your Password: ')
            tries += 1
        break
if tries < 3:
    print('Verified')
else:
    print('Fail to access')