# Copyright 2024 Ilya Demidov

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from cryptography.fernet import Fernet
import sys
import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

HOW_TO_USE_TEXT = "First argument should be 'e' or 'd' meaning encrypt or decrypt respectively. Second argument should be full path to your file.\nExample: python3 e /home/user1/my_diary\nExample: python3 d /home/user1/Downloads/my_diary.enc"


def encrypt_file(key, filename):
    """
    Encrypts a file using the provided key.

    Args:
      key: The encryption key (bytes).
      filename: The path to the file to encrypt.
    """
    with open(filename, 'rb') as file:
        data = file.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open(filename + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)


def decrypt_file(key, filename):
    """
    Decrypts a file using the provided key.

    Args:
      key: The encryption key (bytes).
      filename: The path to the encrypted file (with '.enc' extension).
    """
    with open(filename, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(filename[:-4], 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] in ('-h', 'h', '-help', 'help'):
        print(HOW_TO_USE_TEXT)
        exit(0)
    
    if len(sys.argv) != 3:
        print("\033[1;33mSorry I can't recognize your arguments, if you need help run this code with 'help' argument\033[0m\n\n" + HOW_TO_USE_TEXT)
        exit(0)
    else:
        action = sys.argv[1]
        filename = sys.argv[2]
    
    if action not in ('e', 'd'):
        print("\033[1;31mI can't recognize action, please type 'e' or 'd'\033[0m]")
        exit(1)

    password = input("Enter your password: ").encode("utf-8")
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b'qwerty',
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))

    if not os.path.exists(filename):
        print(f"\033[1;31mFile '{filename}' does not exist.\033[0m]")
        exit(1)

    if action.lower() == 'e':
        # Encrypt a file
        encrypt_file(key, filename)
        print("Done")
    elif action.lower() == 'd':
        # Decrypt the encrypted file
        decrypt_file(key, filename)
        print("Done")
