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
"""
import os
import serial
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import simpledialog
from tkinter import messagebox
import pickle as pic 
import fenetre.Boite_dialogue.SaveVisitBadge as SVB

Couleur    	 	 = "blue" # couleur de la barre inférieur et superieur
TextBottom  	 = "Développer par Rachel Système.......... Année 2021"

F_icone 			= "fenetre/icones/icone.ico" # icone de la boite de dialogue	
F_Zone_Saisie 		= "fenetre/icones/Fond_Zone_De_Saisie.jpeg" # Arrière plan de la zone de saisie
F_Zone_Photo 		= "fenetre/icones/Fond_Zone_De_Photo.jpeg" # Arrière plan de la zone de photo
Photo_Personnel 	= "fenetre/icones/Image_personnel.png" # image par defaut de la personne
		
I_bouton_fermer	= "fenetre/icones/Bouton_fermer.png" # Icone bouton enregistrer
I_bouton_ok	    = "fenetre/icones/Bouton_ok.png" # Icone bouton inserer image

# Textes par défauts
Texte = "Vide"
Default_msg_bottom = "CLIQUER SUR START ET PASSER LE BAGDE"
Success_msg_bottom = "BAGDE VALIDE"
Echec_msg_bottom   = "BAGDE NON REPERTORIE"

# Fichier contenant le port et le baudRate
FICHIER_1 = "fenetre/sous_fenetres/Connexion/Port&AccessBaud.rs.rachel"
FICHIER_2 = "fenetre/sous_fenetres/Connexion/Manager/ID_MANAGER.rs.rachel"
FICHIER_3 = "fenetre/sous_fenetres/Connexion/Manager/MANAGER.rs.rachel"

class F_Demarrer(tk.simpledialog.Dialog):
	"""
		Permet le traitement des données reçu via le port série
	"""	

	def __init__(self, parent, title="Démarrer lecture du badge"):
		super(F_Demarrer, self).__init__(parent,title)

	# Methode permettant d'inclure les widgets dans la boite de dialogue
	def body(self,master):

		self.Photo = Photo_Personnel # image part defaut
		self.msg_Bottom 	 = Default_msg_bottom

		# obtention de la taille de l'écran
		H_ecran = int(self.winfo_screenheight())
		W_ecran = int(self.winfo_screenwidth())
		
		# Calcule de la taille de la fenetre
		self.HAUTEUR = int(H_ecran/1.5)
		self.LARGEUR = int(W_ecran/1.7)
		
		# dimension des différents conteneur : conteneur photo et texte, cadre photo
		self.HS = int((self.HAUTEUR*6)/100) # hauteur de la barre supérieur
		self.HI = int((self.HAUTEUR*5)/100) # hauteur de la barre inferieur(marge Y cadre photo)

		self.HC = int((self.HAUTEUR*89)/100) # hauteur de la zone photo et zone de saisie

		self.HCP = int((self.HC*30)/100) # Auteur du cadre photo
		self.WCP = int((self.LARGEUR*21)/100) # Lageur du cadre photo
	

		self.resizable(width=False, height=False)
		self.geometry("{}x{}".format(self.LARGEUR,self.HAUTEUR))
		self.iconbitmap(F_icone) # icone de la boite de dialogue

		# Frame contenant la barre supérieur et inferieur
		frameSuperieur = tk.Frame(self, relief=tk.GROOVE, height=self.HS,bd=3, bg=Couleur)
		frameSuperieur.pack(side=tk.TOP, fill=tk.X)

		frameInferieur = tk.Frame(self, relief=tk.GROOVE, height=self.HI, bd=3, bg=Couleur)
		frameInferieur.pack(side=tk.BOTTOM, fill=tk.X)
		tk.Label(frameInferieur,text =TextBottom, bg=Couleur).pack()

		# Canvas principal
		# Canvas contenant tout les widgets et son arrière fond
		img0 = Image.open(F_Zone_Saisie)
		Image0 = img0.resize((self.LARGEUR,self.HC))
		self.image_fond0 = ImageTk.PhotoImage(Image0)

		self.canvaCentral = tk.Canvas(self,width=self.LARGEUR, height=self.HC,bd=5, relief=tk.SUNKEN)
		self.canvaCentral.pack(side=tk.LEFT,fill="both", expand=True)
		self.canvaCentral.create_image(0, 0, image=self.image_fond0,anchor="nw")

		# Methode affichant les infos par défaut
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
		# Methode contenant les positions des widgets
		self.positionWidgets()
		
		# Zone contenant le cadre et la photo du personnel
		img1 = Image.open(self.Photo)
		Image1 = img1.resize((self.WCP,self.HCP))
		self.image_personnel = ImageTk.PhotoImage(Image1)

		# Frame contenant le canvas porteur de la photo du personnel
		CadrePhoto = tk.Frame(self.canvaCentral, relief=tk.GROOVE,width=self.WCP,
			height=self.HCP, bd=3)
		CadrePhoto .pack(side=tk.LEFT, pady=self.HI)

		# Canvas portant la photo du personnel
		self.CanvaPhoto = tk.Canvas(CadrePhoto ,width=self.WCP, height=self.HCP,
			relief=tk.SUNKEN)
		self.CanvaPhoto.pack(fill="both", expand=True)
		self.CanvaPhoto.create_image(0, 0, image=self.image_personnel,anchor="nw")
		self.canvaCentral.create_window(self.pos_y0,self.pos_y0,anchor="nw",window=CadrePhoto)

		l  = int((self.LARGEUR*1.45)/100) # lageur du label colonne 1
		l1 = int((self.LARGEUR*7.48)/100) # lageur du label colonne 2
		h  = int((self.HAUTEUR*3.7)/100) # hauteur du label

		# NOM 
		self.Var_Nom = tk.StringVar()
		self.Var_Nom.set(Texte)
		frameNom = tk.Frame(self.canvaCentral, relief=tk.GROOVE,height=h, bd=3)
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

		# CNI / PASSEPORT
		self.Var_CNI = tk.StringVar()
		self.Var_CNI.set(Texte)
		frameCNI = tk.Frame(self.canvaCentral, relief=tk.GROOVE,height=h, bd=3)
		frameCNI.grid(row = 0, column=0, columnspan=2)
		tk.Label(frameCNI,text ="CNI/Passeport : ",width=l, bg="white").grid(row = 0, column=0)
		tk.Label(frameCNI,textvariable = self.Var_CNI,width=l1, 
			bg="white").grid(row = 0, column=1)
		self.canvaCentral.create_window(self.pos_x,self.pos_y8,anchor="nw",window=frameCNI)

		# Texte en dessous de la fenêtre
		y_pad = int((self.LARGEUR*6.23)/100)
		h_T   = int((self.HAUTEUR*0.60)/100)
		self.Var_msg_bottom = tk.StringVar()
		self.Var_msg_bottom.set(self.msg_Bottom)
		CadreTexte = tk.Frame(self.canvaCentral, relief=tk.GROOVE,bd=3)
		CadreTexte .pack(side=tk.BOTTOM, pady=y_pad)
		self.msgAcceuil = tk.Label(CadreTexte, textvariable = self.Var_msg_bottom,
			width=l1,height=h_T,bg="green",font="Arial 10 bold")
		self.msgAcceuil.pack()

		
	# Méthode permettant de restaurer les infos lors
	# l'attente du passage de badge
	def ResetInfos(self):
		self.Photo = Photo_Personnel
		# MISE A JOUR PHOTO
		img1 = Image.open(self.Photo)
		Image1 = img1.resize((self.WCP,self.HCP))
		self.image_personnel = ImageTk.PhotoImage(Image1)
		self.CanvaPhoto.create_image(0, 0, image=self.image_personnel,anchor="nw")

		self.Var_Nom.set(Texte)
		self.Var_Prenom.set(Texte)
		self.Var_Date.set(Texte)
		self.Var_Etat_Civil.set(Texte)
		self.Var_Genre.set(Texte)
		self.Var_Profession.set(Texte)
		self.Var_Poste.set(Texte)
		self.Var_Telephone.set(Texte)
		self.Var_CNI.set(Texte)

		#______________MESSAGE ZONE TEXTE
		self.Var_msg_bottom.set("PASSEZ LE BAGDE POUR ACCEDER A L'OPTION")
		
		
	# Methode permettant la mise à jour des information sur la fenêtre
	# si le badge passé est reconnu
	def UpdateInfos(self):
		# ISE A JOUR PHOTO
		img1 = Image.open(self.Photo)
		Image1 = img1.resize((self.WCP,self.HCP))
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

		# MESSAGE ZONE TEXTE
		self.Var_msg_bottom.set(Success_msg_bottom)


	# Méthode permettant la lecture des données
	# s'exécute si le bouton "start" est cliqué
	def NouvelleLecture(self):
		self.Connection_Reception_Donnee()	


	# Fonction permettant d'annuler et de supprimer la boite
	# si bouton "annuler" appuyer
	def FermerFenetre(self):
		# destruction de la fenètre
		self.destroy()


	# Methode permettant d'inclure les boutons dans la boite de dialogue
	def buttonbox(self):
		Y  = int((self.HAUTEUR*80)/100)

		# BOUTON FERMER
		img1 = Image.open(I_bouton_fermer)
		Image1 = img1.resize((self.WCP,self.HI))
		self.image_Bouton_fermer = ImageTk.PhotoImage(Image1)

		BoutonFermer = tk.Button(self.canvaCentral, image=self.image_Bouton_fermer,
			relief=tk.GROOVE, bd=3,width=self.WCP, height=self.HI, command=self.FermerFenetre)
		# positionement du bouton dans la zone concerné 
		self.canvaCentral.create_window(self.HI,Y,anchor="nw",window=BoutonFermer)


		# BOUTON START
		# Bouton enregistrer placer directement sur le canvas
		img2 = Image.open(I_bouton_ok)
		Image2 = img2.resize((self.WCP,self.HI))
		self.image_Bouton_ok = ImageTk.PhotoImage(Image2)

		BoutonStart = tk.Button(self.canvaCentral, image=self.image_Bouton_ok,
			relief=tk.GROOVE,bd=3,width=self.WCP, height=self.HI, command=self.NouvelleLecture)
		# positionement du bouton dans la zone concerné 
		self.canvaCentral.create_window(int((self.LARGEUR*75)/100) ,Y,anchor="nw",window=BoutonStart)

	
	# Méthode permettant la connection et l'arduino
	def Connection_Reception_Donnee(self):
		self.ResetInfos()
		self.update()
		
		# ouverture du fichier contenant le port et la baudrate
		try:
			with open(FICHIER_1,"rb") as fichier:
				mon_depickler		 = pic.Unpickler(fichier)
				self.port		     = str(mon_depickler.load())
				self.baud			 = str(mon_depickler.load())
				self.baud 			 = int(self.baud)

		except:
			tk.messagebox.showwarning(parent=self,title="Attention",
				message="port et baudrate non disponible")

		# CONNEXION A L'ARDUINO
		try:
			arduino = serial.Serial(self.port,self.baud,timeout=5)
			run = True
		except:
			tk.messagebox.showwarning(parent=self,title="Attention",
			message="arduino non disponible sélectionner le port série et la baudRate connecter la carte")
			run = False
			execute = False

		# réception des données
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
			
			if Data == "0X0":	
				execute = False
				self.Var_msg_bottom.set(Default_msg_bottom)
				self.update()

		# Recherche du fichier dans le dossier Manager 
		# au cas ou il s'agit du MANAGER
		if execute:
			try:
				# comparaison de l'ID reçu et celui du MANAGER
				with open(FICHIER_2,"rb") as fichier:
					mon_depickler		 = pic.Unpickler(fichier)
					self.ID 			 = mon_depickler.load()
			except:
				self.ID = None
		
			if self.ID == (Data+".rs"):
				look = True
				# enregistrement du badge dans le dossier badge lu
				SVB.SaveVisitBadge(ID=Data, save = "MANAGER")
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

					# Methode de mise à jours des informations reçu
					self.UpdateInfos()
					# envoie le message a l'arduino 
					arduino.flushOutput()
					arduino.flushInput()
					arduino.write(b'TRUE')
							
				except:
					pass
			else:
				look = False

			# Recherche du fichier dans le dossier IdPersonnel 
			# au cas ou il ne s'agit pas du MANAGER
			if look == False:
				try:
					with open("IdPersonnel/{}".format(Data+".rs.rachel"),
						"rb") as fichier:
						mon_depickler		 = pic.Unpickler(fichier)
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
						self.msg_Bottom 	 = Success_msg_bottom

					# enregistrement du badge dans le dossier badge lu
					SVB.SaveVisitBadge(ID=Data, save = "PERSONNEL")

					# Méthode de mise à jours des informations reçu
					self.UpdateInfos()
					# envoie le message a l'arduino 
					arduino.flushOutput()
					arduino.flushInput()
					arduino.write(b'TRUE')
				
				# si le fichier recherché n'est pas retrouvé		
				except UnboundLocalError:
					SVB.SaveVisitBadge(ID=Data)
					self.Var_msg_bottom.set(Echec_msg_bottom)
					self.update()
					arduino.flushOutput()
					arduino.flushInput()
					arduino.write(b'FALSE')
					
				except FileNotFoundError:
					SVB.SaveVisitBadge(ID=Data)
					self.Var_msg_bottom.set(Echec_msg_bottom)
					self.update()
					arduino.flushOutput()
					arduino.flushInput()
					arduino.write(b'FALSE')		

		# Fermeture du port	et destruction de la variable "arduino"
		try:
			arduino.close()
			arduino.__exit__()
		except:
			pass