from getpass import getpass 
from hashlib import sha1
msg=input("enter your message : ") 
m=sha1(msg.encode()) h=m.hexdigest()
print("SHA1 : "+h)
