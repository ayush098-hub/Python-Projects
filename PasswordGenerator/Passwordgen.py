import random


lowercase='abcdefghijklmnopqrstuvwxyz'
uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits='0123456789'
symbols='~!@#$%^&*()_+=-'

length=int(input("Enter length of password: "))

characters=lowercase+uppercase+digits+symbols
passwordlist=[]


for i in range(0,length):
    passwordlist.append(random.choice(characters))
password=''
password=password.join(passwordlist)
print(password)



