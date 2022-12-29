#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 * e-mail : rachelsysteme@gmail.com
 * gitHub : https://github.com/RS-malik-el
 * Donation : paypal.me/RachelSysteme
 * 
 * AUTEUR: RACHEL SYSTEME
 * DATE : DECEMBRE 2021
 * DATE DE FIN : 10/01/2022
 * MODIFIER : 28/12/2022
 * 
 * @Tester sous windows

	DESCRIPTION DU FICHIER
	Fichier principal du programme, exécuter le afin de démarrer le programme

	INFORMATION: MODULES NECESSAIRE A AJOUTER
		* datetime 
		* pillow
		* pyserial
		* tktooltip

	FONCTIONNEMENT:
		Ce programme consiste à créer une fenêtre GUI qui intéragis avec Arduino.
		* Stock les informations d'une carte RFID
		* Affiche les informations stockées si la carte passé sur le lecteur est enregistré.
		* Renvoie "TRUE" ou "FALSE" selon que la carte passé est enregistrée ou pas
"""
import fenetre.fenetrePrincipale as fp

fenetre = fp.mainWindow()
fenetre.run()