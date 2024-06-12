# Copyright 2024 Ilya Demidov

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from cryptography.fernet import Fernet
import sys
import os
import base64
import getpass
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

HOW_TO_USE_TEXT = """Example: ./doc_enc_dec.sh enc -f my_diary.txt
where 'enc' means encrypt,
      '-f' means file
      'my_diary.txt' file name

Example: ./doc_enc_dec.sh dec -f my_diary.txt.enc
where 'dec' means decrypt,
      '-f' means file
      'my_diary.txt' file name

many other examples you can find in README.md
"""

# Aliases
HELP_ALIASES = ('-h', 'h', '-help', 'help')
ENCRYPT_ALIASES = ('e', 'enc', 'encr', 'encrypt')
DECRYPT_ALIASES = ('d', 'dec', 'decr', 'decrypt')
FILE_ALIASES = ('-f', '-file')
TEXT_ALIASES = ('-t', '-txt', '-text')

# Constants
FILE = "file"
CONTENT = "content"

def print_error(text):
    """
    Print error in red color and exit from script
    """
    print(f"\033[1;31m{text}\033[0m")
    exit(1)

def write_to_file(data, output_filename):
    """
    Write to file.

    Args:
      data: Data to write to file
      output_filename: File name
    """
    with open(output_filename, 'wb') as file:
        file.write(data)
    print("Done")

def write_to_enc_file(data, filename):
    """
    Write to file encrypted data. File name is original file name with .enc in the end

    Args:
      data: Encrypted data to write to file
      filename: Original file name
    """
    output_filename = filename + '.enc'
    write_to_file(data, output_filename)

def write_to_dec_file(data, filename):
    """
    Write to file decrypted data. File name is original file name without .enc in the end

    Args:
      data: Decrypted data to write to file
      filename: Original file name
    """
    output_filename = filename[:-4]
    write_to_file(data, output_filename)
      

def show_help():
    """
    Check if arguments correct and fits to documentation
    """
    if len(sys.argv) < 2 or any(arg in HELP_ALIASES for arg in sys.argv[1:]):
        print(HOW_TO_USE_TEXT)
        exit(0)

def get_data_as_content():
    """
    Get content from argument or from STDIN
    """
    # Check where get content from
    print("\033[1;33mBe carefull all text which you type or paste here remains in history. Don't forget to clear console history after that\033[0m")
    if len(sys.argv) > 3:
        data = sys.argv[3].encode("utf-8").strip()
    else:
      print("Type or paste your text bellow, press Enter and press Ctrl+D")
      data = sys.stdin.read().encode("utf-8").strip()
    
    return data

def get_filename():
    """
    Check where get file name from
    """
    if len(sys.argv) > 3:
      filename = sys.argv[3]
    else:
      filename = sys.stdin.read()

    return filename

def get_data_from_file():
    """
    Read content from file
    """
    filename = get_filename()
    
    if not os.path.exists(filename):
        print_error(f"File '{filename}' does not exist.")
    
    with open(filename, 'rb') as file:
      data = file.read()
    
    return data

def derive_key_from_input_password():
    """
    Derive key from input password
    """
    password = getpass.getpass("Enter your password: ").encode("utf-8")
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b'constant_salt_to_be_able_to_decrypt',
        iterations=480000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password))
    
if __name__ == '__main__':
    show_help()

    action_name = sys.argv[1]
    if sys.argv[2] in TEXT_ALIASES:
        source = CONTENT
        data = get_data_as_content()
    elif sys.argv[2] in FILE_ALIASES:
        source = FILE
        filename = get_filename()
        data = get_data_from_file()
    else:
        print_error("I can't recognize type of source, please read guide")

    key = derive_key_from_input_password()
    fernet = Fernet(key)

    if action_name.lower() in ENCRYPT_ALIASES:
        data = fernet.encrypt(data)
        write_to_enc_file(data, filename) if source == FILE else print(data.decode("utf-8"))
    elif action_name.lower() in DECRYPT_ALIASES:
        data = fernet.decrypt(data)
        write_to_dec_file(data, filename) if source == FILE else print(data.decode("utf-8"))
    else:
        print_error("I can't recognize action, please read guide")
      