from cryptography.fernet import Fernet
import sys, os, base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

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
  if len(sys.argv) != 3:
    print("\033[1;33mSorry I can't recognize your arguments, if you need help run this code with 'help' argument, but now let's do it step by step\033[0m")
    while True:
      action = input("Type 'e' do encrypt file, type 'd' to decrypt file: ")
      if action.lower() in ('e', 'd'):
        break
    while True:
      filename = input("Enter full file path: ")
      if os.path.exists(filename):
        break
      else:
        print(f"\033[1;31mFile '{filename}' does not exist.\033[0m")
  elif len(sys.argv) == 1 and sys.argv[1] == 'help':
    print("First argument should be 'e' or 'd' meaning encrypt or decrypt respectively. Second argument should be full path to your file.\nExample: python3 e /home/user1/my_diary\nExample: python3 d /home/user1/Downloads/my_diary.enc")
  else:
    action = sys.argv[1]
    filename = sys.argv[2]
  
  password = input("Enter your password: ").encode("utf-8")
  kdf = PBKDF2HMAC(
      algorithm=hashes.SHA256(),
      length=32,
      salt=b'qwerty',
      iterations=480000,
  )
  key = base64.urlsafe_b64encode(kdf.derive(password))
#   with open(os.path.dirname(filename) + "/passwd.key", 'wb') as key_file:
#     key_file.write(key)
#   filename = input("Enter the filename: ")
  
  if not os.path.exists(filename):
    print(f"\033[1;31mFile '{filename}' does not exist.\033[0m]")
    exit
  
  if action.lower() == 'e':
    # Encrypt a file
    encrypt_file(key, filename)
    print("Done")
  elif action.lower() == 'd':
    # Decrypt the encrypted file
    decrypt_file(key, filename)
    print("Done")
  else:
    print("I can't recognize action, please type 'e' or 'd'")
