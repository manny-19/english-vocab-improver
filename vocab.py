import random
from typing import ValuesView
from PyDictionary import PyDictionary
import time
from plyer import notification

dict = PyDictionary
file = open("words.txt","r")   #opeing the file containing words
words = file.read().split("\n")  #reading the file and splitting the words and store them in a list
#print(len(words))

def get_word():
    valid_word = False  #keeps going until a valid word is found
    while(not valid_word):
        index = random.randint(0,9983)
        word = words[index]
        
        if(word[0].islower() and len(word)>2):
            valid_word = True
            return word
        
#print(get_word)

def define_word():
    valid_word = False  #skipping words that do nat have definition in pydictionary
    while(not valid_word):
        global word
        global d
        word = get_word()
        word = word.upper()
        if(dict.meaning(word, disable_errors = True)):
            #print(word.upper(),"\n")
            defs = dict.meaning(word)
            for key,value in defs.items():
                d = str(key) + ": " + str(value)
                break
            valid_word = True
        

            
if __name__ == '__main__':
    while True:
        #word = get_word()
        define_word()
        notification.notify(
            title = word,    #prints word as title
            message = d,     #prints meaning as message
            timeout = 10     #display notifiaction for 10 sec
        )
        time.sleep(60*60*8)  #repeats after every 8 hours        