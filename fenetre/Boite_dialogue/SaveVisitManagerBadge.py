#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 * e-mail : rachelsysteme@gmail.com
 * gitHub : https://github.com/RS-malik-el
 * Donation : paypal.me/RachelSysteme
 *
 * @AUTEUR: RACHEL SYSTEME
 * DATE  : DECEMBRE 2021
 * DATE DE FIN : 11/01/2022
 * MODIFIER : 28/12/2022
"""

import os
import datetime as date
import fenetre.sous_fenetres.CheckManager as CM
import pickle as pic 

FICHIER_1 = "fenetre/sous_fenetres/Connexion/Manager/MANAGER.rs.rachel"

"""
	INFORMATION:
		Ce fichier permet d'enregistré le badge du MANAGER ainsi que l'heure
		lors de l'ouverture d'un onglet 

		* Ce fichier est utilisé dans les fichiers suivant :
			** InfosDuPersonnel.py
			** NouvelleCarte.py
			** ModifierCarte.py
			** supprimerPersonnel.py
		
		RETURN:
			bool->True : Si la copie c'est effectuée (MANAGER)
			bool->False: Si la copie ne c'est pas effectuée (Carte tièrce)

		NB:
			Type de fichier : ".rachel"

	PARAMETRES:
			Paramètre 1: 
				parent: Fenêtre parent ou principal

			Paramètre 2: 
				fichier: Crée un dossier du même Nom que l'onglet ouvert
				par le MANAGER afin d'enregistré l'heure à laquelle l'onglet
				a été ouvert.

	ROLE MODULE:
		fenetre.sous_fenetres.CheckManager as CM
			Methode: CM.F_Demarrer(Parent)
				Cette méthode permet d'ouvrir une fenêtre afin de vérifier si
				c'est bien le MANAGER qui tente d'ouvrir l'onglet. 
			
			Attribut: 
				self.Manager->True : S'il s'agit du MANAGER
				self.Manager->False: S'il ne s'agit pas du MANAGER
"""


def SaveVisitManagerBadge(Parent,fichier):

	# Crée le dossier selon l'onglet ouvert par le MANAGER
	Fichier = fichier
	check = CM.Demarrer(Parent)
	
	# Lecture et sauvegarde de la copie des informations du MANAGER ainsi
	# que la date et l'heure de copie 	
	if check.Manager == True:

		# Création du dossier s'il n'existe pas
		try:
			foldername = os.path.join("Badge lu/OPTIONS MANAGER/"+
				str(date.date.today())+"/{}".format(Fichier))

			os.makedirs(foldername)

			chemin_1 = "Badge lu/OPTIONS MANAGER/"+str(date.date.today())+"/{}".format(Fichier)

		except FileExistsError:
			chemin_1 = "Badge lu/OPTIONS MANAGER/"+str(date.date.today())+"/{}".format(Fichier)

		try:
			# Ouverture du ficher pour faire une copie
			with open(FICHIER_1,'rb') as fichier:

				mon_depickler = pic.Unpickler(fichier)
							
				Photo 			= mon_depickler.load() # CHEMIN D'ACCES PHOTO
				nom 			= mon_depickler.load() # NOM
				prenom 			= mon_depickler.load() # PRENOM
				DateDeNaissance = mon_depickler.load() # DATE OF BIRTH
				EtatCivil 		= mon_depickler.load() # ETAT CIVIL
				Genre 			= mon_depickler.load() # GENRE
				Profession 		= mon_depickler.load() # PROFESSION
				Poste 			= mon_depickler.load() # POSTE
				Telephone  		= mon_depickler.load() # TELEPHONE
				CNI 			= mon_depickler.load() # CNI/PASSEPORT	
				ID 				= mon_depickler.load() # ID CARTE
				
			clock = date.datetime.now()
			
			# Copie des données dans le dossier
			with open("{}/{}".format(chemin_1,"MANAGER-"+str(date.date.today())+
					" "+str(clock.hour)+"h "+str(clock.minute)+"m "+str(clock.second)+
					".rachel"),'wb') as fichier:

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

			return True

		except:
			return False

	else:
		return False
