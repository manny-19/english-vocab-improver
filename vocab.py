import random
from PyDictionary import PyDictionary

file = open("words.txt","r")
word = file.read().split("\n")
print(len(word))
