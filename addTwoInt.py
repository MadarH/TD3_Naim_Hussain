#!/usr/bin/env python
import sys

def add():
    print("Nombre d'argument : " +str(len(sys.argv)-1))
    if len(sys.argv) != 3:
       print("Veuillez inserrer deux chiffres : ")
       print("Premier chiffre : ")
       a = input()
       print("Second chiffre : ")
       b = input()
    else:
       a = int( sys.argv[1] )
       b = int( sys.argv[2] )
    print(a+b)
   

if __name__ ==  "__main__":
    add()





