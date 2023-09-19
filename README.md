# Password Manager - Beginner

--> Tutorial followed : 5 Mini Python Projects - For Beginners [Tech with Tim]

/!\ This program is not a safe way to store sensitive information

## Installation

You will need to install this module :

```bash
pip install cryptography
```

## Launch project

```bash
python3 ./password_manager.py
```

## Warnings
For the encryption to work, you have to uncomment this part, launch the project and comment it again.

```python
# Use this only once

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
```

## Documentation

https://cryptography.io/en/latest/
