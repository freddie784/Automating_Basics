name = ''
password = ''
while password != "JoeMamma":
    print('Who are you?')
    name = input()
    if name == "Joe":
        print("Hello, Joe what is the password (pun)?")
        password = input()
print('Access Granted!')