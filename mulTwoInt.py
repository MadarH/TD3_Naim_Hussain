import sys

print(sys.argv)

a = int( sys.argv[1] )
b = int( sys.argv[2] )


if(len(sys.argv)) == 3:
	print("Le nombre d'arguments est:"), (len(sys.argv))
	
else:
	print("Erreur, le nombre d'arguments est:"), (len(sys.argv))
	sys.exit(0)


print("La reponse est:")
print(a*b)



