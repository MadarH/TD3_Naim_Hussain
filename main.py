#!/usr/bin/env python

#addition
import sys
from addTwoInt import add
print("Voulez vous additioner deux valeurs : ")
print("1 = oui ")
print("0 = non")

print("Votre choix: ")
a = input()
if (a ==1):
   add()
elif(a == 0):
   print("Proceder a la multiplication.")


#multiplication
from TwoIntFunc import mul
print("Voulez vous multiplier deux valeurs : ")
print("1 = oui ")
print("0 = non")

print("Votre choix: ")
a = input()
if (a == 1):
   mul()
elif(a == 0):
   sys.exit(0)
