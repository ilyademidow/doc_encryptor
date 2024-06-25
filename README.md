# Doc Encryptor
![ico](https://github.com/ilyademidow/doc_encryptor/blob/main/ico.jpg)

A Python CLI script for user-friendly documents encryption and decryption using the industry-standard AES in CBC mode with a 128-bit key for encryption. HMAC using SHA256 for authentication algorithm.

Safeguard your documents for backup, cloud storage, or secure exchange. Unlike some "black box" solutions, you can see exactly what happens to your data as source code is simple and open - data stays encrypted and is not shared to third parties. Take back control of your data security.

**WARNING:** Encrypting your files is a great first step, but true security is layered. Uploading encrypted files publicly can still expose them. Partner with strong passwords and follow cybersecurity rules.

### License: MIT

### Prerequisites:
- You have installed Python3

### "Installation"
Download whole this project and give execution permissions to `doc_enc_dec.sh`. _In Linux and MacOS systems it can be performed like:_
```
chmod +x doc_enc_dec.sh
```

Ready, now you can use it!

---
# How to use

Encrypt file:
```
./doc_enc_dec.sh enc -f my_diary.txt
```
Decrypt file: 
```
./doc_enc_dec.sh dec -f /home/user1/Downloads/my_diary.txt.enc
```

Where 
- `enc` and `dec` are actions (`enc` means encrypt, `dec` means decrypt)
- `-f` are content source (`-f` means file)
- `my_diary.txt` is example of your file name 
   
   If your file is placed in the same directory where you run the script, otherwise it needs to use full path `/home/user1/Downloads/my_diary.txt.enc` as it was shown in second example 

### Also it can encrypt plain text

**BE CAREFULL:** all text which typed in console remains in console history. Consider approach to clear console history afterwards

Encrypt text:

```
./doc_enc_dec.sh enc -t "my super sensitive data"
```
Decrypt text:
```
./doc_enc_dec.sh dec -t gAAAAABmahVFCt6hJM4u0irgKLVYBilsnyjSyDXi5wpx2x0LMpfiPp-PW3g31GQ4i17KHY0BYgDeWLIopExK56y7hPpQrth-c37vNp2emaNWSZT2dg_pv2w=
```

or also if text is very long you can put it in STDIN
```
./doc_enc_dec.sh dec -t
```
paste text bellow then press `Enter` and then `Ctrl+D`

And of course you can use pipe commands as 
```
cat my_diary.txt | ./doc_enc_dec.sh enc -t
```
and so on


### Appendix
Also you can use another aliases for encryption as `e`, `enc`, `encr`, `encrypt` and for decryption as `d`, `dec`, `decr`, `decrypt`
