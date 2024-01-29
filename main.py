# password generator
import random
import string
total = string.ascii_uppercase+string.digits+string.punctuation+string.ascii_lowercase
length = 16
password =''.join(random.sample(total,length))
print("Your password is :"+ password)