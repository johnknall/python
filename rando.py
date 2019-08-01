#!/usr/bin/env python3.7
import random
import string
#import secrets

def randomStringL(stringLenth=42):
    letters = string.ascii_lowercase
    return ''.join(random.SystemRandom().choice(letters)for i in range(stringLenth))

print ("Your random lowercase string is",randomStringL())

def randomStringLU(stringLenth=42):
    letters = string.ascii_letters
    return ''.join(random.SystemRandom().choice(letters)for i in range(stringLenth))

print ("Your random mixed case string is",randomStringLU())

def randomStringULN(stringLenth=42):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.SystemRandom().choice(lettersAndDigits)for i in range(stringLenth))

print ("Your random alphanumeric string is",randomStringULN())

def randomStringULNS(stringLenth=42):
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.SystemRandom().choice(lettersAndDigits)for i in range(stringLenth))

print ("Your random everything string is",randomStringULNS())
