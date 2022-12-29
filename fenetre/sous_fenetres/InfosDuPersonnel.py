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

import tkinter as tk
from tkinter import simpledialog
import fenetre.sous_fenetres.SelectFileToRead as SF
import fenetre.Boite_dialogue.SaveVisitManagerBadge as SVMB


F_icone = "fenetre/icones/icone.ico"#icone de la boite de dialogue	
Couleur    	 	 = "blue"#couleur de la barre inférieur et superieur

#Message en bas de fenêtre
TextBottom  	 = "Développer par Rachel Système.......... Année 2021"


class InfosPersonnel(tk.simpledialog.Dialog):
	"""	
		INFORMATION:
			*Ce fichier permet d'afficher les informations d'un fichier ".rachel"

			*Ce fichier est utilisé dans les methodes suivante du 
			fichier "fenetrePrincipal.py
				Module : 
					FenetreInfosPersonnel(self,master=None)
					FenetreBadgeRecent(self,master=None)

			NB:
			Les informations s'affichent seulement si la l'attribut
			self.Liste = 11 et la varible "Save_Card_Manager = True"
			au cas contraire une fenêtre vide s'affiche
		
		PARAMETRES:
			Paramètre 1: 
				parent: Fenêtre parent ou principal

			Paramètre 2: 
				fichier: Crée un dossier du même Nom que l'onglet ouvert
				par le MANAGER afin d'enregistré l'heure à laquelle l'onglet
				a été ouvert.

				UTILISER POUR LE MODULE:
					Fichier : Boite_dialogue/SaveVisitManagerBadge.py
					Module : SaveVisitManagerBadge()

			Paramètre 3:
				dossier: Renseignez le mot clé afin d'ouvrir le bon addresse du fichier.

				VALEUR POSSIBLE: Ses mots clé permettent de savoir quel dossier ouvrir
					VAleur 1: "PERSONNEL"
						Pour ouvrir le dossier: "IdPersonnel" 

					VAleur 2: "BADGE_LU"
						Pour ouvrir le dossier: "Badge lu"

				UTILISER POUR LE MODULE:
					Fichier :sous_fenetres/SelectFileToRead.py
					Module : SelectFile() 
			
			Paramètre 4:
				title: Définit par défaut, titre de la fenêtre
	"""


	def __init__(self, parent,fichier,dossier="PERSONNEL",title="Information du personnel"):
		
		Parent = parent
		Fichier = fichier
		self.initdir = dossier

	
		# Enregistre l'heure à laquelle le MANAGER a ouvert l'onglet
		Save_Card_Manager = SVMB.SaveVisitManagerBadge(Parent,fichier = Fichier)
		
		# Si le Manager donne access la fenêtre se crée sinon rien ne se passe
		if Save_Card_Manager == True:
			super(InfosPersonnel, self).__init__(parent, title)
		

	def body(self,master):
		"""
			Appel à la méthode du module SelectFileToRead 
			l'attribut self.Liste est égal à l'attribut "info" de cette méthode
		"""
		liste = SF.SelectFile(self.initdir)
		self.Liste = liste.info
		

		# Obtention de la taille de l'écran
		H_ecran = int(self.winfo_screenheight())
		W_ecran = int(self.winfo_screenwidth())
		
		# Calcul et dimensionnement de la taille de la fenêtre
		HAUTEUR = 310
		LARGEUR = 400

		self.resizable(width=False, height=False)
		self.geometry("{}x{}".format(LARGEUR,HAUTEUR))

		self.iconbitmap(F_icone)# icone de la boite de dialogue
		

		# Dimension 
		self.HS = int((HAUTEUR*6)/100) # hauteur de la barre supérieur
		self.HI = int((HAUTEUR*5)/100) # hauteur de la barre inferieur

		self.HC = int((HAUTEUR*89)/100) # hauteur Canvas contenant les informations
		self.WC = int((LARGEUR*90)/100) # Largeur Canvas contenant les informations
		

		# Frame contenant la barre supérieur et inferieur
		frameSuperieur = tk.Frame(self, relief=tk.GROOVE, height=self.HS, bd=3, bg=Couleur)
		frameSuperieur.pack(side=tk.TOP, fill=tk.X)

		frameInferieur = tk.Frame(self, relief=tk.GROOVE, height=self.HI, bd=3, bg=Couleur)
		frameInferieur.pack(side=tk.BOTTOM, fill=tk.X)
		LabelTextBottom = tk.Label(frameInferieur,text =TextBottom, bg=Couleur).pack()
		

		# Création du Canvas et du Frame portant les informations à afficher
		Canva = tk.Canvas(self ,width=self.WC, height=self.HC, relief=tk.FLAT)
		Canva.pack(fill="both", expand=True)

		frame = tk.Frame(Canva, relief=tk.GROOVE, height=self.HC,width=self.WC)
		frame.grid(padx=5, columnspan=2, rowspan=10)


		"""
			Les informations s'affichent seulement si la l'attribut
		   	self.Liste = 11 au cas contraire une fenêtre vide s'affiche
		"""
		if len(self.Liste) == 11:
			largeur  = 45
			largeur0 = 12
			tk.Label(frame,text="PHOTO", width=largeur0).grid(row=0, column=0)
			tk.Label(frame,text=self.Liste[0], width=largeur).grid(row=0, column=1)

			tk.Label(frame,text="NOM(S)", width=largeur0).grid(row=1, column=0)
			tk.Label(frame,text=self.Liste[1], width=largeur).grid(row=1, column=1)

			tk.Label(frame,text="PRENOM(S)", width=largeur0).grid(row=2, column=0)
			tk.Label(frame,text=self.Liste[2], width=largeur).grid(row=2, column=1)

			tk.Label(frame,text="DATE", width=largeur0).grid(row=3, column=0)
			tk.Label(frame,text=self.Liste[3], width=largeur).grid(row=3, column=1)

			tk.Label(frame,text="ETAT CIVIL", width=largeur0).grid(row=4, column=0)
			tk.Label(frame,text=self.Liste[4], width=largeur).grid(row=4, column=1)

			tk.Label(frame,text="GENRE", width=largeur0).grid(row=5, column=0)
			tk.Label(frame,text=self.Liste[5], width=largeur).grid(row=5, column=1)

			tk.Label(frame,text="PROFESSION", width=largeur0).grid(row=6, column=0)
			tk.Label(frame,text=self.Liste[6], width=largeur).grid(row=6, column=1)

			tk.Label(frame,text="POSTE", width=largeur0).grid(row=7, column=0)
			tk.Label(frame,text=self.Liste[7], width=largeur).grid(row=7, column=1)

			tk.Label(frame,text="TELEPHONE", width=largeur0).grid(row=8, column=0)
			tk.Label(frame,text=self.Liste[8], width=largeur).grid(row=8, column=1)

			tk.Label(frame,text="CNI/PASSEPORT", width=largeur0).grid(row=9, column=0)
			tk.Label(frame,text=self.Liste[9], width=largeur).grid(row=9, column=1)

			tk.Label(frame,text="IDENTIFIANT", width=largeur0).grid(row=10, column=0)
			tk.Label(frame,text=self.Liste[10], width=largeur).grid(row=10, column=1)

		
	# Ferme la fenêtre
	def fermer(self):
		self.destroy()

	def buttonbox(self):
		# Bouton quitter la fenêtre
		tk.Button(self,relief=tk.GROOVE, text="OK", bg="yellow",
			bd=3,width=20, height=10, command=self.fermer).pack()