#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 * e-mail : rachelsysteme@gmail.com
 * gitHub : https://github.com/RS-malik-el
 * Donation : paypal.me/RachelSysteme
 *
 * @AUTEUR: RACHEL SYSTEME
 * DATE  : DECEMBRE 2021
 * DATE DE FIN : 14/01/2022
 * MODIFIER : 28/12/2022

 INFORMATION:
	Ce fichier contient les messages d'aide et les affiches dans une boite d'information

	UTILISER DANS LE FICHIER :
		**fenetrePrincipale.py
			Methode : 
				**BarreMenu()

"""

from tkinter import messagebox

Doc = """Documentation :\n
PROGRAMMATION ET TRANFERT DES DONNEES DE L'ARDUINO:\n
Inserer dans votre programme une boucle \"for\" telle que:
for(int i=0; i<4; i++){
 Serial.write(Data[i])
}
Avec \"Data\" la variable contenant les 4 bytes identifiant la carte.\n
CONFIGURATION:\n
Sélectionner le taux d\'échange des données
Connecter la carte arduino et cliquer sur le bouton reset afin
d'afficher le port série disponible\n

Pour plus d'informations, lisez le fichier Readme\n 
Abonnez - vous pour nous soutenir et partager la chaîne
Merci de votre compréhension!!!!!!!!!!!!!!
l\'équipe Rachel Système..........................
"""

def Documentation(master=None):
	messagebox.showinfo("Documentation", Doc)


RS = """A propos de Rachel Système \"RS\" :\n
Bonjour!!!
RS est un groupe de jeunes étudiants passionné de 
l\'infomatique et de la mécanique. Créer le 10 Juillet 2021,
vous pouvez nous suivre sur notre :\n
Youtube  :  https://bit.ly/3Fup7Vj
Facebook: https://bit.ly/3V3ajCZ
Linkedin  : https://bit.ly/3PrBxC4
E-mail : rachelsysteme@gmail.com \n
Abonnez - vous pour nous soutenir et partager la chaîne
l\'équipe Rachel Système..........................
"""

def A_propos_de_RS(master=None):
	messagebox.showinfo("A propos de Rachel Système", RS)


LG = """
Module RFID V 1.0.1 (arduino):\n
BUT : Ce logiciel permet d'enregistrer les identifiants des
  cartes RFID (la série de quatre bytes identifiant la carte),
  puis d'associer à la carte : une photo, un nom, un prénom....\n
Comment ça marche : Ce logiciel utilise le port série (port USB)
 afin de communiquer et l\'arduino. Connecter votre module RFID à 
  l'arduino et envoyer les identifiants de la carte RFID via le
  port série qui sera décodé et ensuite les informations liées à
  la carte apparaitront sur l'écran.\n
IMPORTANT:\n
 Après la réception des données ; le logiciel renvoie : \n
 "TRUE" si le badge est reconnu\n
 "FALSE" si le badge n'est pas reconnu\n
vous pouvez nous suivre sur notre :
Youtube  :  https://bit.ly/3Fup7Vj
Facebook: https://bit.ly/3V3ajCZ
Linkedin  : https://bit.ly/3PrBxC4
PayPal : paypal.me/RachelSysteme
E-mail : rachelsysteme@gmail.com \n
Abonnez - vous pour nous soutenir et partager la chaîne
Merci de votre compréhension!!!!!!!!!!!!!!
l\'équipe Rachel Système..........................
"""

def A_propos_du_logiciel(master=None):
	messagebox.showinfo("A propos du logiciel", LG)



if __name__ == '__main__':
	Documentation()
	A_propos_de_RS()
	A_propos_du_logiciel()