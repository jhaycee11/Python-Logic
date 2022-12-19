import os
import base64
import hashlib

username = 'jhaycee'    # Sample Username
password = 'samplepass' # Sample Pass
db = {}                 # Sample DataBase
salt = base64.b64encode(os.urandom(32)) # Salt or random string to add in password

# converting to hash, converting pass to bytes with utf8, adding salt, iterate times
digest = hashlib.pbkdf2_hmac('sha256', bytes(password, 'utf-8'), salt, 10000)  

db[username] = digest   # Adding digest(password in sha256) into username as password

#checking password if equal
def is_log_in(password):
    digest = hashlib.pbkdf2_hmac('sha256', bytes(password, 'utf-8'), salt, 10000)
    return db[username] == digest


print(is_log_in(password))