# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 15:02:00 2020

@author: Debs
"""
#password generator
import string, random
def password_generator(passwordLength = input()):
    letters = string.ascii_letters
    numbers = string.digits
    char = string.punctuation
    pool = ''.join(letters + numbers + char)
    password = ''
    new_password = random.choice (pool)
    password+=new_password
    return ''.join(random.choice(pool) for i in range (passwordLength))
password_generator(7)