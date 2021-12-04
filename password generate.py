import random
passlen = int(input("Enter the length of the password\n"))
s = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()_-=+[{}]"
p = "".join(random.sample(s,passlen))
print(p)