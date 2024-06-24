import random
import string
options = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
pass_length = 8
password = ""
for i in range(pass_length):
    password += random.choice(options)
print(password)