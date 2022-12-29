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
"""
import os
import datetime as date
import tkinter as tk
from tkinter import ttk # pour combox
from PIL import Image, ImageTk
from tkinter import simpledialog
from tkinter import messagebox
import tkinter.filedialog as fd
import pickle as pic 
import fenetre.Boite_dialogue.SaveVisitManagerBadge as SVMB

F_icone 			= "fenetre/icones/icone.ico" # icone de la boite de dialogue	
F_Zone_Saisie 		= "fenetre/icones/Fond_Zone_De_Saisie.jpeg" # Arrière plan de la zone de saisie
F_Zone_Photo 		= "fenetre/icones/Fond_Zone_De_Photo.jpeg" # Arrière plan de la zone de photo
I_bouton_Annuler 	= "fenetre/icones/Bouton_annuler.png" # Icone bouton annuler
I_bouton_engistrer	= "fenetre/icones/Bouton_enregistrer.png" # Icone bouton enregistrer
I_bouton_insert_img = "fenetre/icones/Bouton_inser_image.png" # Icone bouton inserer image
I_bouton_reset_img  = "fenetre/icones/Bouton_reset.png" # Icone bouton restaurer image
Photo_Personnel 	= "fenetre/icones/Image_personnel.png" # image par defaut de la personne

Couleur    	 	 = "blue" # couleur de la barre inférieur et superieur
L_Color			 = "white" # coleur zone de saisie
TextBottom  	 = "Développer par Rachel Système.......... Année 2021"
T_MsgBox    	 = "Confirmer votre choix" # Titre fenetrebox
Msg_annuler 	 = "Voulez - vous vraiment Annuler ?" 
Msg_save		 = "Voulez - vous vraiment enregistré les donneées ?"
Msg_insert_Image = "Voulez - vous vraiment inserer cette image ?"
Msg_reset		 = "Voulez - vous vraiment restaurer la fenètre ?"
Title  			 = "Selectionner le fichier à modifier" # Message fenêtre de sélection fichier


Text_Defaut_Nom 		= "Entrer votre Nom(s)"
Text_Defaut_Prenom 		= "Entrer votre Prénom(s)"
Text_Defaut_Date 		= "jj/mm/aaaa"
Text_Defaut_Genre 		= "Entrer votre choix"
Text_Defaut_Etat_Civil 	= "Entrer votre choix"
Text_Defaut_Profession 	= "Exemple : Informaticien"
Text_Defaut_poste		= "Entrer votre poste"
Text_Defaut_Telephone 	= "Téléphone"
Text_Defaut_CNI     	= "Numéro Passeport / CNI"
Text_Defaut_ID_Carte 	= "hex ID"

# liste des choix possible
listGenre 	   = ["FEMME","HOMME"]
listEtatCivil  = ["Célibataire","En couple","Marié(e)","Divorcé","Femme au foyer", "AUCUN"]
listProfession = ["ELEVE","ETUDIANT(E)", "TRAVAILLEUR", "TRAVAILLEUSE", "SANS EMPLOI","AUCUN"]

# MAXIMUM DES CARACTERES A SAISIR
MaxChartNom 		= 25
MaxChartPrenom 		= 35
MaxCharDate			= 10
MaxChartProfession 	= 35
MaxChartPoste 		= 35
MaxChartTelephone	= 9
MaxChartCNI     	= 22
MaxIntIDcarte 		= 8


class F_ModifierCarte(tk.simpledialog.Dialog):
	"""
		INFORMATION:
			*Ce fichier permet de modifier le contenu d'un fichier ".rachel"
			contenu dans le dossier "IdPersonnel" et contient les informations 
			reliées à la carte à passer devant le lecteur RFID

			*Sélectionner un fichier et modifier le à votre guise
			avant de le sauvegarder de nouveau

			*Si aucun fichier à modifier n'est sélectionné, le fenêtre enregistrera
			toutes les infos saisies  dans un nouveau fichier. 

		UTILISER DANS LE FICHIER :
			**fenetrePrincipale.py
				Methode : 
					**FenetreModifierCarte()

		PARAMETRES:
			Paramètre 1: 
				parent: Fenêtre parent ou principale

			Paramètre 2:
				title: Définit par défaut, titre de la fenêtre
	"""

	def __init__(self, parent,title="Modifier les informations de la Carte"):
		Parent = parent
		# Enregistre l'heure à laquelle le MANAGER a ouvert l'onglet
		Save_Card_Manager = SVMB.SaveVisitManagerBadge(Parent,fichier = "MODIFIER CARTE")
		
		# Si le Manager donne access la fenêtre se crée sinon rien ne se passe
		if Save_Card_Manager == True:
			super(F_ModifierCarte, self).__init__(parent,title)
		

	# Methode permettant d'inclure les widgets dans la boite de dialogue
	def body(self,master):

		self.Photo_inserer	 = Photo_Personnel
		self.Nom 			 = ""
		self.Prenom 		 = ""
		self.DateDeNaissance = ""
		self.EtatCivil		 = ""
		self.Genre 			 = ""
		self.Profession		 = ""
		self.Poste 			 = ""
		self.Telephone 	     = ""
		self.CNI    		 = ""
		self.IDcarte 		 = ""

		# Ouverture du dossier de sélection fichier à modifier
		type_de_fichier =[("fichier rachel",".rachel")] 
		self.Dossier = fd.askopenfilename(title=Title,filetypes=type_de_fichier,
			initialdir= "IdPersonnel")

		# obtention de la taille de l'écran
		H_ecran = int(self.winfo_screenheight())
		W_ecran = int(self.winfo_screenwidth())
		
		# Calcule de la taille de la fenetre
		self.HAUTEUR = int(H_ecran/1.5)
		self.LARGEUR = int(W_ecran/1.7)
		
		self.resizable(width=False, height=False)
		self.geometry("{}x{}".format(self.LARGEUR,self.HAUTEUR))

		# icone de la boite de dialogue
		self.iconbitmap(F_icone)

		# Dimension des différents conteneur : conteneur photo et texte, cadre photo
		self.HS = int((self.HAUTEUR*6)/100) # hauteur de la barre supérieur
		self.HI = int((self.HAUTEUR*5)/100) # hauteur de la barre inferieur(marge Y cadre photo)

		self.HC = int((self.HAUTEUR*89)/100) # hauteur de la zone photo et zone de saisie
		self.WCI = int((self.LARGEUR*30)/100) # Largeur de la zone photo
		self.WCS = int(self.LARGEUR - self.WCI) # Largeur de la zone saisie

		self.HCP = int((self.HC*30)/100) # Auteur du cadre photo
		self.WCP = int((self.WCI*70)/100) # Lageur du cadre photo

		# Frame contenant la barre supérieur et inferieur
		frameSuperieur = tk.Frame(self, relief=tk.GROOVE, height=self.HS, bd=3, bg=Couleur)
		frameSuperieur.pack(side=tk.TOP, fill=tk.X)

		frameInferieur = tk.Frame(self, relief=tk.GROOVE, height=self.HI, bd=3, bg=Couleur)
		frameInferieur.pack(side=tk.BOTTOM, fill=tk.X)
		LabelTextBottom = tk.Label(frameInferieur,text =TextBottom, bg=Couleur).pack()

		# Appel aux méthodes
		self.ZonePhotoPersonnel()
		self.ZoneSaisieInfo()
		self.Restaurer() # Information par defaut


	# Methode contenant les caracteristiques de la zone de phote
	def ZonePhotoPersonnel(self):
		# Zone contenant la photo et son arrière plan
		img0 = Image.open(F_Zone_Photo)
		Image0 = img0.resize((self.WCI,self.HC))
		self.image_fond0 = ImageTk.PhotoImage(Image0)

		self.ZonePhoto = tk.Canvas(self,width=self.WCI, height=self.HC,bg="yellow",
			relief=tk.SUNKEN)
		self.ZonePhoto.pack(side=tk.LEFT,fill="both", expand=True)
		self.ZonePhoto.create_image(0, 0, image=self.image_fond0,anchor="nw")

		# Zone contenant le cadre et la photo du personnel
		img1 = Image.open(self.Photo_inserer)
		Image1 = img1.resize((self.WCP,self.HCP))
		self.image_personnel = ImageTk.PhotoImage(Image1)

		# Frame contenant le canvas porteur de la photo du personnel
		CadrePhoto = tk.Frame(self.ZonePhoto, relief=tk.GROOVE,width=self.WCP,
			height=self.HCP,bd=3)
		CadrePhoto.pack(pady=self.HI)

		# Canvas portant la photo du personnel
		self.CanvaPhoto = tk.Canvas(CadrePhoto ,width=self.WCP, height=self.HCP,
			relief=tk.SUNKEN)
		self.CanvaPhoto.pack(fill="both", expand=True)
		self.CanvaPhoto.create_image(0, 0, image=self.image_personnel,anchor="nw")


	# Methode contenant les caracteristiques de la zone de saisie
	def ZoneSaisieInfo(self):

		W_frame  = int((self.WCS*67)/100) # largaur du frame
		W_entry  = int((self.WCS*10)/100)  # largeur zone entry 
		W_combox = int((self.WCS*9.5)/100) # largeur zone combox
		W_label  = int((self.WCS*2)/100) # largeur du label

		# position de chaque frame suivant Y
		ecart = int((self.HAUTEUR*7.8)/100)
		self.frame_y0 = int((self.HAUTEUR*3.98)/100)
		self.frame_y1 = int(self.frame_y0 + ecart)
		self.frame_y2 = int(self.frame_y1 + ecart)
		self.frame_y3 = int(self.frame_y2 + ecart)
		self.frame_y4 = int(self.frame_y3 + ecart)
		self.frame_y5 = int(self.frame_y4 + ecart)
		self.frame_y6 = int(self.frame_y5 + ecart)
		self.frame_y7 = int(self.frame_y6 + ecart)
		self.frame_y8 = int(self.frame_y7 + ecart)
		self.frame_y9 = int(self.frame_y8 + ecart)

		# Zone de saisie et son arrière plan
		img2 = Image.open(F_Zone_Saisie)
		Image2 = img2.resize((self.WCS,self.HC))
		self.image_fond1 = ImageTk.PhotoImage(Image2)
		self.ZoneSaisie = tk.Canvas(self,width=self.WCS, height=self.HC,
			relief=tk.SUNKEN)
		self.ZoneSaisie.pack(fill="both", expand=True)
		self.ZoneSaisie.create_image(0, 0, image=self.image_fond1,anchor="nw")

		# NOM
		self.frameNom = tk.Frame(self.ZoneSaisie,relief=tk.FLAT,width=W_frame,
			height=self.HS,bd=5)
		self.frameNom .grid(row=0, column=0, columnspan=2)
		tk.Label(self.frameNom,text="NOM(S)",width=W_label).grid(row=0, column=0)

		# Entrer nom
		self.Var_Nom = tk.StringVar()
		tk.Entry(self.frameNom, textvariable=self.Var_Nom,width=W_entry,
			bg=L_Color).grid(row=0, column=1)
		self.ZoneSaisie.create_window(self.HS,self.frame_y0,anchor="nw",window=self.frameNom)
		self.Var_Nom.trace("w", lambda *args: self.LimiteCaractere(
			entry_text =self.Var_Nom, nb=MaxChartNom))

		# PRENOM
		self.framePrenom = tk.Frame(self.ZoneSaisie,relief=tk.FLAT,width=W_frame,
			height=self.HS, bd=5)
		self.framePrenom.grid(row=1, column=0, columnspan=2)
		tk.Label(self.framePrenom,text="PRENOM(S)",width=W_label).grid(row=0, column=0)
		
		# Entrer PRENOM
		self.Var_Prenom = tk.StringVar()
		tk.Entry(self.framePrenom, textvariable=self.Var_Prenom,width=W_entry,
			bg=L_Color).grid(row=0, column=1)
		self.ZoneSaisie.create_window(self.HS,self.frame_y1,anchor="nw",window=self.framePrenom)
		self.Var_Prenom.trace("w", lambda *args: self.LimiteCaractere(
			entry_text =self.Var_Prenom, nb=MaxChartPrenom))

		# DATE DE NAISSANCE
		self.frameDate = tk.Frame(self.ZoneSaisie,relief=tk.FLAT,width=W_frame,
			height=self.HS, bd=5)
		self.frameDate.grid(row=1, column=0, columnspan=2)
		tk.Label(self.frameDate,text="Né(e) le",width=W_label).grid(row=0, column=0)
		
		# Entrer DATE DE NAISSANCE
		self.Var_DateDeNaissance = tk.StringVar()
		tk.Entry(self.frameDate, textvariable=self.Var_DateDeNaissance,width=W_entry,
			bg=L_Color).grid(row=0, column=1)
		self.ZoneSaisie.create_window(self.HS,self.frame_y2,anchor="nw",window=self.frameDate)
		self.Var_DateDeNaissance.trace("w", lambda *args: self.LimiteCaractere(
			entry_text =self.Var_DateDeNaissance, nb=MaxCharDate))

		# GENRE
		self.frameGenre = tk.Frame(self.ZoneSaisie,relief=tk.FLAT,width=W_frame,
			height=self.HS, bd=5)
		self.frameGenre.grid(row=1, column=0, columnspan=2)
		tk.Label(self.frameGenre,text="Genre",width=W_label).grid(row=0, column=0)
		
		# Entrer GENRE
		# Création d'un combox affichant la liste de genre
		self.ComboGenre = ttk.Combobox(self.frameGenre,values=listGenre,width=W_combox,
			state ="readonly")
		self.ComboGenre.grid(row=0, column=1)
		self.ZoneSaisie.create_window(self.HS,self.frame_y3,anchor="nw",window=self.frameGenre)

		# ETAT CIVIL
		self.frameEtatCivil = tk.Frame(self.ZoneSaisie,relief=tk.FLAT,width=W_frame,
			height=self.HS, bd=5)
		self.frameEtatCivil.grid(row=1, column=0, columnspan=2)
		tk.Label(self.frameEtatCivil,text="Etat civil",width=W_label).grid(row=0, column=0)
		
		# Entrer CIVIL
		# Création d'un combox affichant la liste des ETATS CIVIL
		self.ComboEtatCivil= ttk.Combobox(self.frameEtatCivil,values=listEtatCivil,width=W_combox,
			state="readonly")
		self.ComboEtatCivil.grid(row=0, column=1)
		self.ZoneSaisie.create_window(self.HS,self.frame_y4,anchor="nw",window=self.frameEtatCivil)

		# PROFESSION
		self.frameProfession = tk.Frame(self.ZoneSaisie,relief=tk.FLAT,width=W_frame,
			height=self.HS, bd=5)
		self.frameProfession.grid(row=1, column=0, columnspan=2)
		tk.Label(self.frameProfession,text="Profession",width=W_label).grid(row=0, column=0)
		
		# Entrer PROFESSION
		self.Var_Profession = tk.StringVar()
		tk.Entry(self.frameProfession, textvariable=self.Var_Profession,width=W_entry,
			bg=L_Color).grid(row=0, column=1)
		self.ZoneSaisie.create_window(self.HS,self.frame_y5,anchor="nw",window=self.frameProfession)
		self.Var_Profession.trace("w", lambda *args: self.LimiteCaractere(
			entry_text =self.Var_Profession, nb=MaxChartProfession))
		
		# POSTE OCCUPER
		self.framePoste = tk.Frame(self.ZoneSaisie,relief=tk.FLAT,width=W_frame,
			height=self.HS,bd=5)
		self.framePoste.grid(row=0, column=1, columnspan=2)
		tk.Label(self.framePoste,text="Poste Occupé",width=W_label).grid(row=0, column=0)
		
		# Entrer _POSTE OCCUPER
		self.Var_Poste = tk.StringVar()
		tk.Entry(self.framePoste, textvariable=self.Var_Poste,width=W_entry,
			bg=L_Color).grid(row=0, column=1)
		self.ZoneSaisie.create_window(self.HS,self.frame_y6,anchor="nw",window=self.framePoste)
		self.Var_Poste.trace("w", lambda *args: self.LimiteCaractere(
			entry_text =self.Var_Poste, nb=MaxChartPoste))

		# TELEPHONE
		self.frameTelephone = tk.Frame(self.ZoneSaisie,relief=tk.FLAT,width=W_frame,
			height=self.HS, bd=5)
		self.frameTelephone.grid(row=1, column=0, columnspan=2)
		tk.Label(self.frameTelephone,text="Téléphone",width=W_label).grid(row=0, column=0)
		
		# Entrer TELEPHONE
		self.Var_Telephone = tk.StringVar()
		tk.Entry(self.frameTelephone, textvariable=self.Var_Telephone,width=W_entry,
			bg=L_Color).grid(row=0, column=1)
		self.ZoneSaisie.create_window(self.HS,self.frame_y7,anchor="nw",window=self.frameTelephone)
		self.Var_Telephone.trace("w", lambda *args: self.LimiteCaractere(
			entry_text =self.Var_Telephone, nb=MaxChartTelephone))

		# CNI
		self.frameCNI = tk.Frame(self.ZoneSaisie,relief=tk.FLAT,width=W_frame,
			height=self.HS,bd=5)
		self.frameCNI.grid(row=1, column=0, columnspan=2)
		tk.Label(self.frameCNI,text="CNI/Passeport",width=W_label).grid(row=0, column=0)
		
		# Entrer CNI
		self.Var_CNI = tk.StringVar()
		tk.Entry(self.frameCNI, textvariable=self.Var_CNI,width=W_entry,
			bg=L_Color).grid(row=0, column=1)
		self.ZoneSaisie.create_window(self.HS,self.frame_y8,anchor="nw",window=self.frameCNI)
		self.Var_CNI.trace("w", lambda *args: self.LimiteCaractere(
			entry_text=self.Var_CNI, nb=MaxChartCNI))

		# IDENTIFIANT DE LA CARTE
		self.frameIDcarte = tk.Frame(self.ZoneSaisie,relief=tk.FLAT,width=W_frame,
			height=self.HS,bd=5)
		self.frameIDcarte.grid(row=1, column=0, columnspan=2)
		tk.Label(self.frameIDcarte,text="ID Carte",width=W_label).grid(row=0, column=0)
		
		# Entrer IDENTIFIANT DE LA CARTE
		self.Var_IDcarte = tk.StringVar()
		tk.Entry(self.frameIDcarte, textvariable=self.Var_IDcarte,width=W_entry,
			bg=L_Color).grid(row=0, column=1)
		self.ZoneSaisie.create_window(self.HS,self.frame_y9,anchor="nw",window=self.frameIDcarte)
		self.Var_IDcarte.trace("w", lambda *args: self.LimiteCaractere(
			entry_text=self.Var_IDcarte, nb=MaxIntIDcarte))
	

	# FONCTION PERMETTANT DE LIMITER LE NOMBRE DES CARACTERES A SAISIR
	def LimiteCaractere(self, entry_text, nb):
		if len(entry_text.get()) > 0:
			entry_text.set(entry_text.get()[:nb])



	# INSERTION D'IMAGE
	def ChangeImage(self,master=None):
		# CHEMIN D'ACCESS DE L'IMAGE
		# liste contenant le type de fichier à ouvrir
		type_de_fichier =[("fichier png",".png"),("fichier jpeg",".jpeg"),("fichier jpg",".jpg")] 
		self.Photo_inserer = fd.askopenfilename(title="Inserer une image",filetypes=type_de_fichier)	

		# CONFIRMATION DE L'ACTION
		reponse = tk.messagebox.askyesno(parent=self,title=T_MsgBox, message=Msg_insert_Image)

		if reponse:
			try:
				# CHANGEMENT D'IMAGE
				img1 = Image.open(self.Photo_inserer)
			except AttributeError:
				self.Photo_inserer = Photo_Personnel
				img1 = Image.open(self.Photo_inserer)

			Image1 = img1.resize((self.WCP,self.HCP))
			self.image_personnel = ImageTk.PhotoImage(Image1)
			self.CanvaPhoto.create_image(0, 0, image=self.image_personnel,anchor="nw")
			
		
	# Fonction permettant d'annuler et de supprimer la boite si bouton annuler appuyer
	def Annuler(self):
		reponse = tk.messagebox.askyesno(parent=self,title=T_MsgBox, message=Msg_annuler)
		if reponse:
			# destruction de la fenètre
			self.destroy()
		

	# Fonction permettant d'enregistrer les infos surla boite si bouton enregistrer appuyer
	def Enregister(self):
		# Messagebox de confirmation
		reponse = tk.messagebox.askyesno(parent=self,title=T_MsgBox, message=Msg_save)
		
		# recupération des valeurs 
		try:
			if self.Photo_inserer == "":
				self.Photo_inserer = Photo_Personnel
		except AttributeError:
			self.Photo_inserer = Photo_Personnel

		self.Nom 			 = self.Var_Nom.get()
		self.Prenom 		 = self.Var_Prenom.get()
		self.DateDeNaissance = self.Var_DateDeNaissance.get()
		self.EtatCivil		 = self.ComboEtatCivil.get()
		self.Genre 			 = self.ComboGenre.get()
		self.Profession		 = self.Var_Profession.get()
		self.Poste 			 = self.Var_Poste.get()
		self.Telephone 	     = self.Var_Telephone.get()
		self.CNI    		 = self.Var_CNI.get()
		self.IDcarte		 = self.Var_IDcarte.get()

		if reponse:
			# Si case vide affiche le message suivant lors du tentative de l'enregistrement
			if self.Nom=="" or self.Prenom=="" or self.DateDeNaissance=="" or self.Poste=="" or self.Profession=="" or self.CNI =="" or self.IDcarte=="":

				tk.messagebox.showwarning(parent=self,title="Attention",
					message="Veuillez - remplir la case vide s'il vous plaît !!!")

			else:
				os.remove(self.Dossier) # supprimer le ficher precédent pour le remplacer

				Genre = str(self.Genre)
				EtatCivil = str(self.EtatCivil)

				# Ecriture des données dans le fichier IdPersonnel
				with open("IdPersonnel/{}".format("0X"+ self.IDcarte.upper() + ".rs.rachel"),
					'wb') as fichier:

	   				mesDonnees = pic.Pickler(fichier)
	   				mesDonnees.dump(self.Photo_inserer)
	   				mesDonnees.dump(self.Nom.upper())
	   				mesDonnees.dump(self.Prenom.title())
	   				mesDonnees.dump(self.DateDeNaissance)
	   				mesDonnees.dump(EtatCivil)
	   				mesDonnees.dump(Genre)
	   				mesDonnees.dump(self.Profession)
	   				mesDonnees.dump(self.Poste.upper())
	   				mesDonnees.dump(self.Telephone)
	   				mesDonnees.dump(self.CNI)
	   				mesDonnees.dump("0X"+ self.IDcarte.upper()+".rs")
					
				# destruction de la fenètre
				self.destroy()


	# Restaure les informations par défaut de la carte
	def Restaurer(self):
		if self.Dossier != "":
			try:
				with open(self.Dossier, "rb") as fichier:
			   		mesDonnees = pic.Unpickler(fichier)

			   		self.Photo_inserer 	 = mesDonnees.load()
			   		self.Nom 			 = mesDonnees.load()
			   		self.Prenom 		 = mesDonnees.load()
			   		self.DateDeNaissance = mesDonnees.load()
			   		self.EtatCivil 		 = mesDonnees.load()
			   		self.Genre 			 = mesDonnees.load()
			   		self.Profession 	 = mesDonnees.load()
			   		self.Poste 			 = mesDonnees.load()
			   		self.Telephone 		 = mesDonnees.load()
			   		self.CNI 			 = mesDonnees.load()
			   		self.IDcarte 		 = mesDonnees.load()
			except:
				pass

			cpt = 0
			IDcarte = ""
			# suppresion des caracteres "OX" et ".rs"
			for x in self.IDcarte:
			   	cpt += 1

			   	if cpt > 2 and cpt < 11:
			   		IDcarte += x
			   				
			self.Var_Nom.set(self.Nom) 
			self.Var_Prenom.set(self.Prenom)
			self.Var_DateDeNaissance.set(self.DateDeNaissance)
			self.ComboEtatCivil.set(self.EtatCivil)
			self.ComboGenre.set(self.Genre)
			self.Var_Profession.set(self.Profession)
			self.Var_Poste.set(self.Poste)
			self.Var_Telephone.set(self.Telephone)
			self.Var_CNI .set(self.CNI)
			self.Var_IDcarte.set(IDcarte)

			# PHOTO DU PERSONNEL
			img1 = Image.open(self.Photo_inserer)
			Image1 = img1.resize((self.WCP,self.HCP))
			self.image_personnel = ImageTk.PhotoImage(Image1)
			self.CanvaPhoto.create_image(0,0,image=self.image_personnel,anchor="nw")	

			self.update()		
			
			
		else:
			messagebox.showinfo("Information", "Aucun fichier sélectionner")


	# Methode permettant d'inclure les boutons dans la boite de dialogue
	def buttonbox(self):
		# BOUTON INSERER PHOTO
		# Frame contenant le bouton inserer photo du personnel
		frameInsertPhoto = tk.Frame(self.ZonePhoto, relief=tk.FLAT,width=self.WCP, 
			height=self.HI, bd=3)
		frameInsertPhoto.pack()

		img2 = Image.open(I_bouton_insert_img)
		Image2 = img2.resize((self.WCP,self.HI))
		self.image_Bouton_Insert = ImageTk.PhotoImage(Image2)

		BoutonInsertPhoto = tk.Button(frameInsertPhoto, image=self.image_Bouton_Insert,
			relief=tk.GROOVE,bd=3, command=self.ChangeImage)
		BoutonInsertPhoto.pack()

		# BOUTON ANNULER
		# Frame contenant le bouton Annuler
		frameBoutonAnnuler = tk.Frame(self.ZonePhoto, relief=tk.FLAT,width=self.WCP, 
			height=self.HI, bd=3)
		frameBoutonAnnuler.pack(side=tk.BOTTOM)

		img1 = Image.open(I_bouton_Annuler)
		Image1 = img1.resize((self.WCP,self.HI))
		self.image_Bouton_Annuler = ImageTk.PhotoImage(Image1)

		BoutonAnnuler = tk.Button(frameBoutonAnnuler, image=self.image_Bouton_Annuler, 
			relief=tk.GROOVE,bd=3, command=self.Annuler)
		BoutonAnnuler.pack()

		# BOUTON ENREGISTRER
		# Bouton enregistrer placer directement sur le canvas
		img2 = Image.open(I_bouton_engistrer)
		Image2 = img2.resize((self.WCP,self.HI))
		self.image_Bouton_Save = ImageTk.PhotoImage(Image2)

		# Création bouton enregistrer
		BoutonSave = tk.Button(self.ZoneSaisie, image=self.image_Bouton_Save, 
			relief=tk.GROOVE,bd=3,width=self.WCP, height=self.HI, command=self.Enregister)
		
		# positionement du bouton dans la zone concerné 
		self.ZoneSaisie.create_window(int((self.WCS*65)/100),int((self.HC*92)/100),
			anchor="nw",window=BoutonSave)

		# BOUTON RESTAURER
		# Bouton enregistrer placer directement sur le canvas
		img3 = Image.open(I_bouton_reset_img)
		Image3 = img3.resize((self.WCP,self.HI))
		self.image_Bouton_Reset = ImageTk.PhotoImage(Image3)

		# Création bouton enregistrer
		BoutonReset = tk.Button(self.ZoneSaisie, image=self.image_Bouton_Reset,relief=tk.GROOVE,
			bd=3,width=self.WCP, height=self.HI, command=self.Restaurer)

		# positionement du bouton dans la zone concerné 
		self.ZoneSaisie.create_window(self.HI,int((self.HC*92)/100),anchor="nw",window=BoutonReset)
