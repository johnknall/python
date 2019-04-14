#!/usr/bin/python
import random
import string
#import secrets

def randomStringL(stringLenth=42):
    letters = string.ascii_lowercase
    return ''.join(random.SystemRandom().choice(letters)for i in range(stringLenth))

print "Your random string is",randomStringL()

def randomStringLU(stringLenth=42):
    letters = string.ascii_letters
    return ''.join(random.SystemRandom().choice(letters)for i in range(stringLenth))

print "Your random string is",randomStringLU()
print "Your random string is",randomStringLU(21)

def randomStringULN(stringLenth=42):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.SystemRandom().choice(lettersAndDigits)for i in range(stringLenth))

print "Your random string is",randomStringULN()
print "Your random string is",randomStringULN(21)

def randomStringULNS(stringLenth=42):
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.SystemRandom().choice(lettersAndDigits)for i in range(stringLenth))

print "Your random string is",randomStringULNS()
print "Your random string is",randomStringULNS(21)
