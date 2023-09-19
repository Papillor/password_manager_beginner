from cryptography.fernet import Fernet

'''

# Use this only once

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

admin_pwd = input("What is your word to encrypt ? ") 

key = load_key() + admin_pwd.encode()
fer = Fernet(key)


def add():
    name = input("Username: ")
    password = input("Password: ")

    with open('passwords.txt', 'a') as file:
        file.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")
     
def view():
    with open('passwords.txt', 'r') as file:
        for line in file.readlines():
            data = line.rstrip()
            user, passwd = data.split("|")
            print("User :", user, "| Password :", fer.decrypt(passwd.encode()).decode())
   
while True :
    mode = input ("Woudl you like to add a password or view the existing ones (add, view) ? Press q to quit. ").lower()
    if mode == "q":
        break    
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid option")
        continue