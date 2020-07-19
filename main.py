#!/usr/bin/env python
import sys
from addTwoInt import add
print("Voulez vous additioner deux valeurs(1/0) : ")
print("1 = oui ")
print("0 = non")
a = input()
if (a ==1):
   add()
elif(a == 0):
   sys.exit(0)
