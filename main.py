# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 19:33:04 2020

@author: shata
"""
#Password Generator in Python
import string
import random
s1=string.ascii_lowercase
#print(s1)
s2=string.ascii_uppercase
#print(s2)
s3=string.digits
#print(s3)
s4=string.punctuation
#print(s4)
pwdlen=int(input("enter length of password\n"))
s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
#print(s)
random.shuffle(s)
#print(s)
print("".join(s[0:pwdlen]))
