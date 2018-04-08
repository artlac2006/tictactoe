#!/usr/bin/python3

def gagner(val):
	if (cases[1]==val) & (cases[2]==val) & (cases[3]==val) | \
           (cases[1]==val) & (cases[4]==val) & (cases[7]==val) | \
           (cases[1]==val) & (cases[5]==val) & (cases[9]==val) | \
           (cases[2]==val) & (cases[5]==val) & (cases[8]==val) | \
           (cases[3]==val) & (cases[6]==val) & (cases[9]==val) | \
           (cases[7]==val) & (cases[8]==val) & (cases[9]==val) | \
           (cases[3]==val) & (cases[5]==val) & (cases[7]==val) | \
           (cases[4]==val) & (cases[5]==val) & (cases[6]==val) :
		print("Joueur "+val+" a gagné!")
		quit(0)
def aff():
	print(" "+cases[1]+" | "+cases[2]+" | "+cases[3]+" ")
	print("-----------")
	print(" "+cases[4]+" | "+cases[5]+" | "+cases[6]+" ")
	print("-----------")
	print(" "+cases[7]+" | "+cases[8]+" | "+cases[9]+" ")


def lol(par):
	print("Quel est votre jeu, joueur "+par+" ?")
	print("   |   |   ")
	print("")
	print("  _______  ")
	reponse = input()
	print("Vous jouez "+reponse)
	cases[int(reponse)] = par
	aff()
	gagner(par)
	

cases = [' ','1','2','3','4','5','6','7','8','9']
aff()
lol('X')
lol('O')
lol('X')
lol('O')
lol('X')
lol('O')
lol('X')
lol('O')
lol('X')
print("Partie nulle!")
