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

import time
import serial
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import simpledialog
from tkinter import messagebox
import pickle as pic


TIME = 3 # Temps d'attente avant destruction de la fenêtre

Couleur    	 	= "blue" # couleur de la barre inférieur et superieur
TextBottom  	= "Développer par Rachel Système.......... Année 2021"

F_icone 		= "fenetre/icones/icone.ico" # icone de la boite de dialogue	
F_Zone_Saisie 	= "fenetre/icones/Fond_Zone_De_Saisie.jpeg" # Arrière plan de la fenêtre
Photo_Personnel = "fenetre/icones/Image_personnel.png" # image par defaut de la personne
		
I_bouton_fermer	= "fenetre/icones/Bouton_fermer.png" # Icone bouton enregistrer
I_bouton_ok	    = "fenetre/icones/Bouton_ok.png" # Icone bouton inserer image

# Textes par défauts
Texte = "Vide" 
Default_msg_bottom = "CLIQUER SUR START ET PASSER LE BAGDE"
Success_msg_bottom = "BAGDE VALIDE"
Echec_msg_bottom   = "BAGDE NON RECONNU"

# Fichier contenant le port et le baudRate
FICHIER_1 = "fenetre/sous_fenetres/Connexion/Port&AccessBaud.rs.rachel"
FICHIER_2 = "fenetre/sous_fenetres/Connexion/Manager/ID_MANAGER.rs.rachel"
FICHIER_3 = "fenetre/sous_fenetres/Connexion/Manager/MANAGER.rs.rachel"

class Demarrer(tk.simpledialog.Dialog):
	"""
		INFORMATION:
			Ce fichier permet de créer une fenêtre afin de vérifier et de donner
			accès au MANAGER dans l'onglet qu'il souhaites accéder 	

			Attribut: 
					self.Manager->True : S'il s'agit du MANAGER
					self.Manager->False: S'il ne s'agit pas du MANAGER

			*UTILISER DANS LE FICHIER :
				**SaveVisitManagerBadge.py

			PARAMETRES:
				Paramètre 1: 
					parent: Fenêtre parent ou principal

				Paramètre 2:
					title: Définit par défaut, titre de la fenêtre
	"""


	def __init__(self, parent, title="Seul le Manager peut acceder à cette option"):
		self.Manager = False
		super(Demarrer, self).__init__(parent,title)


	# Methode permettant d'inclure les widgets dans la boite de dialogue
	def body(self,master):
		self.Photo = Photo_Personnel # image part defaut
		self.msg_Bottom 	 = Default_msg_bottom

		# obtention de la taille de l'écran
		H_ecran = int(self.winfo_screenheight())
		W_ecran = int(self.winfo_screenwidth())
		
		# Calcul de la taille minimale de la fenetre
		self.HAUTEUR = int(H_ecran/1.5)
		self.LARGEUR = int(W_ecran/1.7)
		
		# Dimension des différents conteneur : Canvas Arrière plan & cadre photo
		self.HS = int((self.HAUTEUR*6)/100) # hauteur de la barre supérieur
		self.HI = int((self.HAUTEUR*5)/100) # hauteur de la barre inferieur(marge Y cadre photo)

		self.HC = int((self.HAUTEUR*89)/100) # hauteur du Canvas principal (arrière plan)

		self.HCP = int((self.HC*30)/100) # Auteur du cadre photo
		self.WCP = int((self.LARGEUR*21)/100) # Lageur du cadre photo

		self.resizable(width=False, height=False)
		self.geometry("{}x{}".format(self.LARGEUR,self.HAUTEUR))

		self.iconbitmap(F_icone) # icone de la boite de dialogue


		# Frame contenant la barre supérieur et inferieur
		frameSuperieur = tk.Frame(self, relief=tk.GROOVE, height=self.HS, bd=3,
			bg=Couleur)
		frameSuperieur.pack(side=tk.TOP, fill=tk.X)

		frameInferieur = tk.Frame(self, relief=tk.GROOVE, height=self.HI, bd=3,
			bg=Couleur)
		frameInferieur.pack(side=tk.BOTTOM, fill=tk.X)
		tk.Label(frameInferieur,text =TextBottom, bg=Couleur).pack()


		# Canvas principal
		# Canvas contenant tout les widgets et son arrière fond
		img0 = Image.open(F_Zone_Saisie) # Ouverture d'image
		Image0 = img0.resize((self.LARGEUR,self.HC)) # Redimensionnement de l'image

		# convertion d'image en image utilisable par Tk
		self.image_fond0 = ImageTk.PhotoImage(Image0) 

		self.canvaCentral = tk.Canvas(self,width=self.LARGEUR, height=self.HC,bd=5,
			relief=tk.SUNKEN)
		self.canvaCentral.pack(side=tk.LEFT,fill="both", expand=True)
		self.canvaCentral.create_image(0, 0, image=self.image_fond0,anchor="nw")

		# Methode affichant les infos du personnel par défaut
		self.informationDefaut()


	# Methode contenant les positions des widgets
	def positionWidgets(self):
		# Position texte sur les infos du bagde
		self.pos_x = int((self.LARGEUR*31)/100)
		ecart = int((self.HAUTEUR*6.90)/100)
		self.pos_y0 = int((self.HAUTEUR*4)/100)
		self.pos_y1 = int(self.pos_y0 + ecart)
		self.pos_y2 = int(self.pos_y1 + ecart)
		self.pos_y3 = int(self.pos_y2 + ecart)
		self.pos_y4 = int(self.pos_y3 + ecart)
		self.pos_y5 = int(self.pos_y4 + ecart)
		self.pos_y6 = int(self.pos_y5 + ecart)
		self.pos_y7 = int(self.pos_y6 + ecart)
		self.pos_y8 = int(self.pos_y7 + ecart)
	
	
	# Methode contenant les informations par defaut
	def informationDefaut(self):
		# Appel méthode
		self.positionWidgets()
		l  = int((self.LARGEUR*1.45)/100) # lageur du label colonne 1
		l1 = int((self.LARGEUR*7.48)/100) # lageur du label colonne 2
		h  = int((self.HAUTEUR*3.7)/100) # hauteur du label

		# Cadre de photo
		img1 = Image.open(self.Photo) # Ouverture d'image
		Image1 = img1.resize((self.WCP,self.HCP)) # Redimensionnement de l'image

		# convertion d'image en image utilisable par Tk
		self.image_personnel = ImageTk.PhotoImage(Image1) 

		# Frame contenant le canvas porteur de la photo du personnel
		CadrePhoto = tk.Frame(self.canvaCentral, relief=tk.GROOVE,width=self.WCP,
			height=self.HCP, bd=3)
		CadrePhoto.pack(side=tk.LEFT, pady=self.HI)

		# Canvas portant la photo du personnel
		self.CanvaPhoto = tk.Canvas(CadrePhoto ,width=self.WCP, height=self.HCP,
			relief=tk.SUNKEN)
		self.CanvaPhoto.pack(fill="both", expand=True)
		self.CanvaPhoto.create_image(0, 0, image=self.image_personnel,anchor="nw")
		self.canvaCentral.create_window(20,20,anchor="nw",window=CadrePhoto)

		# NOM 
		self.Var_Nom = tk.StringVar()
		self.Var_Nom.set(Texte)
		frameNom = tk.Frame(self.canvaCentral, relief=tk.GROOVE,height=30, bd=3)
		frameNom.grid(row = 0, column=0, columnspan=2)
		tk.Label(frameNom,text ="NOM(S) :",width=l, bg="white").grid(row = 0, column=0)
		tk.Label(frameNom,textvariable =self.Var_Nom,width=l1,
			bg="white").grid(row = 0, column=1)
		self.canvaCentral.create_window(self.pos_x,self.pos_y0,anchor="nw",window=frameNom)

		# PRENOM
		self.Var_Prenom = tk.StringVar()
		self.Var_Prenom.set(Texte)
		framePrenom = tk.Frame(self.canvaCentral, relief=tk.GROOVE,height=h, bd=3)
		framePrenom.grid(row = 0, column=0, columnspan=2)
		tk.Label(framePrenom,text ="PRENOM(S) : ",width=l, bg="white").grid(row = 0, column=0)
		tk.Label(framePrenom,textvariable = self.Var_Prenom,width=l1,
			bg="white").grid(row = 0, column=1)
		self.canvaCentral.create_window(self.pos_x,self.pos_y1,anchor="nw",window=framePrenom)

		# DATE
		self.Var_Date = tk.StringVar()
		self.Var_Date.set(Texte)
		frameDate = tk.Frame(self.canvaCentral, relief=tk.GROOVE,height=h, bd=3)
		frameDate.grid(row = 0, column=0, columnspan=2)
		tk.Label(frameDate,text ="DATE : ",width=l, bg="white").grid(row = 0, column=0)
		tk.Label(frameDate,textvariable = self.Var_Date,width=l1,
			bg="white").grid(row = 0, column=1)
		self.canvaCentral.create_window(self.pos_x,self.pos_y2,anchor="nw",window=frameDate)

		# ETAT CIVIL
		self.Var_Etat_Civil = tk.StringVar()
		self.Var_Etat_Civil.set(Texte)
		frameEtat_Civil = tk.Frame(self.canvaCentral, relief=tk.GROOVE,height=h, bd=3)
		frameEtat_Civil.grid(row = 0, column=0, columnspan=2)
		tk.Label(frameEtat_Civil,text ="Etat_Civil : ",width=l, bg="white").grid(row = 0, column=0)
		tk.Label(frameEtat_Civil,textvariable = self.Var_Etat_Civil,width=l1,
			bg="white").grid(row = 0, column=1)
		self.canvaCentral.create_window(self.pos_x,self.pos_y3,anchor="nw",window=frameEtat_Civil)

		# GENRE
		self.Var_Genre = tk.StringVar()
		self.Var_Genre.set(Texte)
		frameGenre = tk.Frame(self.canvaCentral, relief=tk.GROOVE,height=h, bd=3)
		frameGenre.grid(row = 0, column=0, columnspan=2)
		tk.Label(frameGenre,text ="Genre : ",width=l, bg="white").grid(row = 0, column=0)
		tk.Label(frameGenre,textvariable = self.Var_Genre,width=l1,
			bg="white").grid(row = 0, column=1)
		self.canvaCentral.create_window(self.pos_x,self.pos_y4,anchor="nw",window=frameGenre)

		# PROFESSION
		self.Var_Profession = tk.StringVar()
		self.Var_Profession.set(Texte)
		frameProfession = tk.Frame(self.canvaCentral, relief=tk.GROOVE,height=h, bd=3)
		frameProfession.grid(row = 0, column=0, columnspan=2)
		tk.Label(frameProfession,text ="Profession : ",width=l, bg="white").grid(row = 0, column=0)
		tk.Label(frameProfession,textvariable = self.Var_Profession,width=l1,
			bg="white").grid(row = 0, column=1)
		self.canvaCentral.create_window(self.pos_x,self.pos_y5,anchor="nw",window=frameProfession)

		# POSTE
		self.Var_Poste = tk.StringVar()
		self.Var_Poste.set(Texte)
		framePoste = tk.Frame(self.canvaCentral, relief=tk.GROOVE,height=h, bd=3)
		framePoste.grid(row = 0, column=0, columnspan=2)
		tk.Label(framePoste,text ="Poste : ",width=l, bg="white").grid(row = 0, column=0)
		tk.Label(framePoste,textvariable = self.Var_Poste,width=l1,
			bg="white").grid(row = 0, column=1)
		self.canvaCentral.create_window(self.pos_x,self.pos_y6,anchor="nw",window=framePoste)

		# TELEPHONE
		self.Var_Telephone = tk.StringVar()
		self.Var_Telephone.set(Texte)
		frameTelephone = tk.Frame(self.canvaCentral, relief=tk.GROOVE,height=h, bd=3)
		frameTelephone.grid(row = 0, column=0, columnspan=2)
		tk.Label(frameTelephone,text ="PROFESSION : ",width=l, bg="white").grid(row = 0, column=0)
		tk.Label(frameTelephone,textvariable = self.Var_Telephone, width=l1,
			bg="white").grid(row = 0, column=1)
		self.canvaCentral.create_window(self.pos_x,self.pos_y7,anchor="nw",window=frameTelephone)

		# CNI
		self.Var_CNI = tk.StringVar()
		self.Var_CNI.set(Texte)
		frameCNI = tk.Frame(self.canvaCentral, relief=tk.GROOVE,height=h, bd=3)
		frameCNI.grid(row = 0, column=0, columnspan=2)
		tk.Label(frameCNI,text ="CNI/Passeport : ",width=l, bg="white").grid(row = 0, column=0)
		tk.Label(frameCNI,textvariable = self.Var_CNI,width=l1, 
			bg="white").grid(row = 0, column=1)
		self.canvaCentral.create_window(self.pos_x,self.pos_y8,anchor="nw",window=frameCNI)

		# Texte en dessous de la fenetre
		y_pad = int((self.LARGEUR*6.23)/100)
		h_T   = int((self.HAUTEUR*0.60)/100)
		self.Var_msg_bottom = tk.StringVar()
		self.Var_msg_bottom.set(self.msg_Bottom)
		CadreTexte = tk.Frame(self.canvaCentral, relief=tk.GROOVE,bd=3)
		CadreTexte .pack(side=tk.BOTTOM, pady=y_pad)
		self.msgAcceuil = tk.Label(CadreTexte, textvariable = self.Var_msg_bottom,
			width=60,height=h_T ,bg="green",font="Arial 10 bold").pack()

		
	# Methode permettant de restaurer les infos 
	def ResetInfos(self):
		# MISE A JOUR PHOTO
		self.Photo = Photo_Personnel
		img1 = Image.open(self.Photo) # Ouverture d'image
		Image1 = img1.resize((self.WCP,self.HCP)) # Redimensionnement de l'image

		# convertion d'image en image utilisable par Tk
		self.image_personnel = ImageTk.PhotoImage(Image1) 
		self.CanvaPhoto.create_image(0, 0, image=self.image_personnel,anchor="nw")
	
		self.Var_Nom.set(Texte) 		# NOM
		self.Var_Prenom.set(Texte) 		# PRENOM
		self.Var_Date.set(Texte) 		# DATE
		self.Var_Etat_Civil.set(Texte) 	# ETAT CIVIL
		self.Var_Genre.set(Texte) 		# GENRE
		self.Var_Profession.set(Texte)	# PROFESSION
		self.Var_Poste.set(Texte)		# POSTE
		self.Var_Telephone.set(Texte)	# TELEPHONE
		self.Var_CNI.set(Texte)			# CNI/PASSEPORT

		# MESSAGE ZONE TEXTE
		self.Var_msg_bottom.set("PASSEZ LE BAGDE POUR ACCEDER A L'OPTION")
		
		
	# Methode permettant la mise à jour des information sur la fenetre
	def UpdateInfos(self):
		# MISE A JOUR PHOTO
		img1 = Image.open(self.Photo) # Ouverture d'image
		Image1 = img1.resize((self.WCP,self.HCP))# Redimensionnement de l'image

		# convertion d'image en image utilisable par Tk
		self.image_personnel = ImageTk.PhotoImage(Image1) 
		self.CanvaPhoto.create_image(0, 0, image=self.image_personnel,anchor="nw")

		self.Var_Nom.set(self.nom)
		self.Var_Prenom.set(self.prenom)
		self.Var_Date.set(self.DateDeNaissance)
		self.Var_Etat_Civil.set(self.EtatCivil)
		self.Var_Genre.set(self.Genre)
		self.Var_Profession.set(self.Profession)
		self.Var_Poste.set(self.Poste)
		self.Var_Telephone.set(self.Telephone)
		self.Var_CNI.set(self.CNI)
		self.Var_msg_bottom.set(Success_msg_bottom)
	

	# Méthode permettant la nouvelle lecture de carte
	def NouvelleLecture(self):
		self.Connection_Reception_Donnee()	


	# Méthode permettant la fermeture de la fenêtre
	def FermerFenetre(self):
		self.destroy()


	# Methode permettant d'inclure les boutons dans la boite de dialogue
	def buttonbox(self):
		Y  = int((self.HAUTEUR*80)/100)
		# BOUTON "FERMER"
		img1 = Image.open(I_bouton_fermer) # Ouverture d'image
		Image1 = img1.resize((self.WCP,self.HI)) # Redimensionnement de l'image

		# convertion d'image en image utilisable par Tk
		self.image_Bouton_fermer = ImageTk.PhotoImage(Image1) 

		#Création bouton "fermer"
		BoutonFermer = tk.Button(self.canvaCentral, image=self.image_Bouton_fermer,
			relief=tk.GROOVE, bd=3,width=self.WCP, height=self.HI,
			command=self.FermerFenetre)
		#positionement du bouton dans la zone concerné 
		self.canvaCentral.create_window(self.HI,Y,anchor="nw",window=BoutonFermer)

		# BOUTON START
		img2 = Image.open(I_bouton_ok) # Ouverture d'image
		Image2 = img2.resize((self.WCP,self.HI)) # Redimensionnement de l'image

		# convertion d'image en image utilisable par Tk
		self.image_Bouton_ok = ImageTk.PhotoImage(Image2) 

		# Création BOUTON START
		BoutonStart = tk.Button(self.canvaCentral, image=self.image_Bouton_ok,
			relief=tk.GROOVE,bd=3,width=self.WCP, height=self.HI,
			command=self.NouvelleLecture)
		# Positionement du bouton dans la zone concerné 
		self.canvaCentral.create_window(int((self.LARGEUR*75)/100),Y,anchor="nw",window=BoutonStart)

	
	# Module permettant la connection et l'aduino
	def Connection_Reception_Donnee(self):
		self.ResetInfos()
		self.update()
		
		try:
			with open(FICHIER_1,"rb") as fichier:
				mon_depickler		 = pic.Unpickler(fichier)
				self.port		     = str(mon_depickler.load())
				self.baud			 = str(mon_depickler.load())
				self.baud 			 = int(self.baud)

		except:
			tk.messagebox.showwarning(parent=self,title="Attention",
				message="port and baudrate non disponible")


		try:
			execute = False
			# CONNEXION A L'ARDUINO
			arduino = serial.Serial(self.port,self.baud,timeout=5)
			run = True
		except:
			tk.messagebox.showwarning(parent=self,title="Attention",
				message="arduino non disponible sélectionner le port série et la baudRate connecter la carte")
			run = False

		# reception des données
		if run : 
			try: 
				Data = arduino.read(size=4)
				Data = int.from_bytes(Data,"big")
				Data = hex(Data)
				Data = str(Data.upper())
				execute = True
			except:
				tk.messagebox.showwarning(title="Attention",
					message="arduino non disponible")
				
			if Data == "0X0" :
				execute = False
				self.Var_msg_bottom.set(Default_msg_bottom)
				arduino.flushOutput()
				arduino.flushInput()	
				arduino.close()
				arduino.__exit__()

		# Mise a jour de la fenêtre
		if execute:
			try:
				with open(FICHIER_2,"rb") as fichier:
					mon_depickler		 = pic.Unpickler(fichier)
					self.ID 			 = mon_depickler.load()
					
					if self.ID == (Data+".rs"):
						self.msg_Bottom = Success_msg_bottom

						try:
							with open(FICHIER_3,'rb') as fichier:
								mon_depickler = pic.Unpickler(fichier)
								
								self.Photo 			 = mon_depickler.load()
								self.nom 			 = mon_depickler.load()
								self.prenom 		 = mon_depickler.load()
								self.DateDeNaissance = mon_depickler.load()
								self.EtatCivil 		 = mon_depickler.load()
								self.Genre 			 = mon_depickler.load()
								self.Profession 	 = mon_depickler.load()
								self.Poste 			 = mon_depickler.load()
								self.Telephone  	 = mon_depickler.load()
								self.CNI 			 = mon_depickler.load()

							self.UpdateInfos()
							self.update()
							self.Manager = True
							time.sleep(TIME)
							self.destroy()
							
						except FileNotFoundError:
							self.Manager = False
						except:
							self.Manager = False

					else:
						self.Var_msg_bottom.set(Echec_msg_bottom)
						self.update()
						self.Manager = False

			except UnboundLocalError:
				self.Var_msg_bottom.set(Echec_msg_bottom)
				self.update()
				self.Manager = False
			except FileNotFoundError:
				self.Var_msg_bottom.set(Echec_msg_bottom)
				self.update()
				self.Manager = False