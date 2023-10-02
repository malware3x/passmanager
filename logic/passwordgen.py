import random
import string

def generate_password(length=8):    
    password = ''
    
    for i in range(length//8):
        password += random.choice(string.ascii_lowercase)
        
    for i in range(length//8):
        password += random.choice(string.ascii_uppercase) 

    for i in range(length//8):
        password += random.choice(string.digits)

    password = ''.join(random.sample(password,len(password)))
    
    return password