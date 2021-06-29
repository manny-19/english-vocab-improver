import random
from PyDictionary import PyDictionary

file = open("hey.txt","r")
word = file.read().split("\n")
print(len(word))
