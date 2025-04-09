import os

def fileRead():
    with open('doc.txt', 'r') as x:
        value = x.read()
        print(value)

def fileWrite():
    pass

fileRead()