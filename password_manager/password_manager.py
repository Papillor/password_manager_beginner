from cryptography.fernet import Fernet
import getpass

def write_key(password):
    key = Fernet.generate_key()
    key_with_password = key + password.encode()  
    # Save the key in the ke.key file
    with open("key.key", "wb") as key_file:
        key_file.write(key_with_password)

def load_key(password):
    with open("key.key", "rb") as key_file:
        key_with_password = key_file.read()
    key = key_with_password[:-len(password.encode())]
    return key

def add(fer):
    name = input("Username: ")
    password = getpass.getpass("Password: ")

    with open('passwords.txt', 'a') as file:
        file.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")

def view(fer):
    with open('passwords.txt', 'r') as file:
        for line in file.readlines():
            data = line.rstrip()
            user, passwd = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passwd.encode()).decode())

def main():
    # Write user password
    password = getpass.getpass("Enter your password: ")

    try:
        key = load_key(password)
    except FileNotFoundError:
        print("Key not found. Generating a new key.")
        write_key(password) 
        key = load_key(password)

    # Create Fernet object with key
    fer = Fernet(key)

    while True:
        mode = input("Would you like to add a password or view the existing ones (add, view)? Press q to quit. ").lower()
        if mode == "q":
            break
        elif mode == "add":
            add(fer)
        elif mode == "view":
            view(fer)
        else:
            print("Invalid option")
            continue

if __name__ == "__main__":
    main()
