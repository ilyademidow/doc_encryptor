# Doc Encryptor
![ico](https://github.com/ilyademidow/doc_encryptor/blob/main/ico.jpg)

A Python CLI script for user-friendly file encryption and decryption using the industry-standard AES in CBC mode with a 128-bit key for encryption. HMAC using SHA256 for authentication algorithm.

Safeguard your files for backup, cloud storage, or secure exchange. Unlike some "black box" solutions, you can see exactly what happens to your data - it stays encrypted and never shared to third parties. Take back control of your data security.

**WARNING:** Encrypting your files is a great first step, but true security is layered. Uploading encrypted files publicly can still expose them. Partner with strong passwords and follow cybersecurity rules

### License: MIT


## How to use
Encrypt file:
```
python3 e my_diary.txt
```
Decrypt file: 
```
python3 d /home/user1/Downloads/my_diary.txt.enc
```

Where `e` and `d` are actions. `e` means encrypt, `d` means decrypt

`my_diary.txt` is example of your file if your file is placed in the same directory where you run the script, otherwise it needs to use full path as shown in second example `/home/user1/Downloads/my_diary.txt.enc`