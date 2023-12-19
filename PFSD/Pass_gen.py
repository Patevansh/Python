import string
import random

def pass_gen(n):
    characters=string.ascii_letters + string.digits + string.punctuation
    password=""
    for i in range(n):
        password+=random.choice(characters)
    print(password)
pass_gen(10)
print("\n",string.ascii_letters)
print("\n",string.digits)
print("\n",random.choice(string.digits))
print("\n",type(string.ascii_letters))
print("\n",type(string.digits))