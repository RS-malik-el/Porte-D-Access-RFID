#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 * e-mail : rachelsysteme@gmail.com
 * gitHub : https://github.com/RS-malik-el
 * Donation : paypal.me/RachelSysteme

 * @AUTEUR: RACHEL SYSTEME
 * DATE  : DECEMBRE 2021
 * DATE DE FIN : 14/01/2022
"""
import os
import datetime as date
import pickle as pic 

"""
	INFORMATION:
		Ce fichier permet d'enregistré la date ainsi que l'heure du
		badge passé dans le menu 'Demarrer' 

	UTILISER DANS LE FICHIER :
		**Demarrer.py

		Methode:		
			**Connection_Reception_Donnee()

		NB:
			Type de fichier : ".rachel"

	PARAMETRES:
			Paramètre 1: 
				ID: Identifiant de la carte

			Paramètre 2: 
				save: Permet de savoir s'il s'agit du manager
					d'une personne tierçe, ou une carte non connue

		VALEUR POSSIBLE:
			Valeur 1 : "PERSONNEL"
				* Pour les badges enregistrés 

			Valeur 2 : "MANAGER"
				* Pour le badge manager 

			Valeur 3 : "UNKNOWN"
				* Pour les badges non enregistrés 
"""

def SaveVisitBadge(ID,save="UNKNOWN"):
	BaseDir_1 = "Badge lu/ACCESS PERSONNEL/ACCESS/"
	BaseDir_2 = "Badge lu/ACCESS PERSONNEL/REFUS/"

	Run = True
	# Chemin d'enregistrement ainsi que le fichier a faire la copie
	if save == "PERSONNEL":
		chemin = "IdPersonnel/"
		identification = ID
	elif save == "MANAGER":
		chemin = "fenetre/sous_fenetres/Connexion/Manager/"
		identification = "MANAGER"
	else:
		identification = ID+"-"
		Run = False

	if  Run == True:
		# Création du chemin d'enregistrement du fichier
		try:
			foldername = os.path.join(BaseDir_1 +str(date.date.today()))
			os.makedirs(foldername)
			chemin_1 = BaseDir_1 +str(date.date.today())
		except FileExistsError:
			chemin_1 = BaseDir_1 +str(date.date.today())

		try:
			# Lecture et sauvegarde de la copie des informations du badge lu
			# ainsi que la date et l'heure de copie
			with open("{}{}".format(chemin, identification +".rs.rachel"),'rb') as fichier:
				mon_depickler = pic.Unpickler(fichier)
								
				Photo 			= mon_depickler.load()
				nom 			= mon_depickler.load()
				prenom			= mon_depickler.load()
				DateDeNaissance = mon_depickler.load()
				EtatCivil 		= mon_depickler.load()
				Genre 			= mon_depickler.load()
				Profession 		= mon_depickler.load()
				Poste 			= mon_depickler.load()
				Telephone  		= mon_depickler.load()
				CNI 			= mon_depickler.load()	
				ID 				= mon_depickler.load()
				
			clock = date.datetime.now()
			
			# Ecriture des données dans le dossier "Badge lu/ACCESS PERSONNEL/ACCESS/"
			with open("{}/{}".format(chemin_1,identification+"-"+ str(date.date.today())+
				" "+str(clock.hour)+"h "+str(clock.minute)+"m "+str(clock.second)+".rachel"),
				'wb') as fichier:

				mesDonnees = pic.Pickler(fichier)
				mesDonnees.dump(Photo)
				mesDonnees.dump(nom)
				mesDonnees.dump(prenom)
				mesDonnees.dump(DateDeNaissance)
				mesDonnees.dump(EtatCivil)
				mesDonnees.dump(Genre)
				mesDonnees.dump(Profession)
				mesDonnees.dump(Poste)
				mesDonnees.dump(Telephone)
				mesDonnees.dump(CNI)
				mesDonnees.dump(ID)

		except:
			pass

	else:
		# Création du chemin d'enregistrement du fichier
		try:
			foldername = os.path.join(BaseDir_2 +str(date.date.today()))
			os.makedirs(foldername)
			chemin_1 = BaseDir_2 +str(date.date.today())
		except FileExistsError:
			chemin_1 = BaseDir_2 +str(date.date.today())

		clock = date.datetime.now()
			
		# Ecriture des données dans le dossier "Badge lu/ACCESS PERSONNEL/REFUS/"
		with open("{}/{}".format(chemin_1,identification + str(date.date.today())+
			" "+str(clock.hour)+"h "+str(clock.minute)+"m "+str(clock.second)+
			".rachel"), 'wb') as fichier:
			pass