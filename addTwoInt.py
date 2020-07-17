#!/usr/bin/env python
import sys

def add():
    print("Nombre d'argument : " +str(len(sys.argv)-1))
    if len(sys.argv) != 3:
       print("Error.Please run the program again with 2 arguments")
       sys.exit(0)
    a = int( sys.argv[1] )
    b = int( sys.argv[2] )
    print(a+b)
   

if __name__ ==  "__main__":
    add()





