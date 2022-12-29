#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 * e-mail : rachelsysteme@gmail.com
 * gitHub : https://github.com/RS-malik-el
 * Donation : paypal.me/RachelSysteme
 *
 * @AUTEUR: RACHEL SYSTEME
 * DATE  : DECEMBRE 2021
 * DATE DE FIN : 10/01/2022
"""

import os
import tkinter.filedialog as fd
from tkinter import messagebox
import pickle as pic 


class SelectFile:
	"""
		INFORMATION:
			Ce fichier permet de selectionner les fichiers ".rachel" afin
			d'enregistré le contenu dans l'attribut "self.info" 
			qui sera utilisé dans le module ci - dessous pour être afficher

			*Fichier utilisé dans le fichier "InfosDuPersonnel.py"

		PARAMETRES:
			Paramètre 1: 
				fichier: Renseignez l'addresse par défaut à ouvrir afin de
					choisir le bon fichier.

				VALEUR POSSIBLE: Ses mots clé permettent de savoir quel dossier ouvrir
					VAleur 1: "PERSONNEL"
						Si le dossier nommé: "IdPersonnel" n'existe pas, on le crée
						puis on l'ouvre pour sélectionner le fichier sinon s'il
						existe déja, on l'ouvre directement pour sélectionner le
						fichier souhaiter.

					VAleur 2: "BADGE_LU"
						Si le dossier nommé: "Badge lu" n'existe pas, on le crée
						puis on l'ouvre pour sélectionner le fichier sinon s'il
						existe déja, on l'ouvre directement pour sélectionner le
						fichier souhaiter.


			Paramètre 2: 
				title: Définit par défaut à : "Ouvrir un fichier"
					Titre de la fenêtre

			
		ATTRIBUT:
			self.info: Variable de type 'Liste' contenant les informations
				du dossier ouvert.
				Enregistre 11 éléments si aucune erreurs ne survient. 
	"""

	def __init__(self,fichier,title="Ouvrir un fichier"):
		super(SelectFile, self).__init__()

		Title = title
		Fichier = fichier
		
		"""Création du dossier s'il n'existe pas et affichage
		d'une boite d'information en cas de création de dossier
		"""
		if Fichier == "PERSONNEL" :
			try:
				os.mkdir("IdPersonnel")		
				chemin = "IdPersonnel"
				messagebox.showinfo(text="Attention",msg="Aucun badge n'a été enregistré")
			except FileExistsError:
				chemin = "IdPersonnel"

		if Fichier == "BADGE_LU":
			try:
				os.mkdir("Badge lu")		
				chemin = "Badge lu"
				messagebox.showinfo(text="Attention",msg="Aucun badge n'a été lu")
			except FileExistsError:
				chemin = "Badge lu"

		self.info = [""]

		# Ouverture du dossier renseigné
		type_de_fichier =[("fichier rachel",".rachel")] 
		self.fichier = fd.askopenfilename(title=Title,filetypes=type_de_fichier,
			initialdir= chemin)	
		
		# En cas d'erreur on passe
		try:
			with open('{}'.format(self.fichier),'rb') as fichier:
				mon_depickler = pic.Unpickler(fichier)

				# CHEMIN D'ACCES PHOTO
				self.info[0] = mon_depickler.load()

				# NOM
				nom = mon_depickler.load()
				self.info.append(nom) 

				# PRENOM
				prenom = mon_depickler.load()
				self.info.append(prenom) 

				# DATE OF BIRTH
				dateofbirth = mon_depickler.load()
				self.info.append(dateofbirth) 

				# ETAT CIVIL
				etatcivil = mon_depickler.load()
				self.info.append(etatcivil)

				# GENRE
				genre = mon_depickler.load()
				self.info.append(genre) 

				# PROFESSION
				profession = mon_depickler.load()
				self.info.append(profession)
 				
 				# POSTE
				poste = mon_depickler.load()
				self.info.append(poste) 

				# TELEPHONE
				telephone = mon_depickler.load()
				self.info.append(telephone)  	
			 	
			 	# CNI/PASSEPORT
				cni = mon_depickler.load()
				self.info.append(cni) 

				# IDCARTE
				IDcarte = mon_depickler.load()
				self.info.append(IDcarte) 
				
		except FileNotFoundError:
			pass
		except:
			pass