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
import tkinter as tk
from tkinter import ttk
from tktooltip import ToolTip
from tkinter import messagebox
from PIL import Image, ImageTk
import pickle as pic # module permettant d'écrire les fichiers
import serial.tools.list_ports
import fenetre.Boite_dialogue.BoiteInfo as BI
import fenetre.Boite_dialogue.supprimerPersonnel as SP
import fenetre.sous_fenetres.NouvelleCarte as NC
import fenetre.sous_fenetres.ModifierCarte as MC 
import fenetre.sous_fenetres.Demarrer as DM
import fenetre.sous_fenetres.SaveManager as SM
import fenetre.sous_fenetres.InfosDuPersonnel as IP
import fenetre.sous_fenetres.CheckManager as CM

# titre de la fenetre principale
F_titre = "Rachel Système : Module RFID V 1.0.1 (arduino)"
# chemin d'accèss de l'icone de la fenetre principale
F_icone = "fenetre/icones/icone.ico"
# Couleur barre d'outils et barre inferieur
Coleur = "blue"

TextBottom = "Développer par Rachel Système.......... Année 2021"

# Dimension des boutons de la barre d'outil
B_W = 25
B_H = 25

# Chemin d'access des icones des boutons
F_imageFond  = "fenetre/icones/Image_fond.png"
F_demarrer 	 = "fenetre/icones/Demarrer.png"
F_ListeCarte = "fenetre/icones/ListeID.png"
F_newCarte   = "fenetre/icones/NewID.png"
F_Aproposde  = "fenetre/icones/icone.ico"
F_ResetPort  = "fenetre/icones/reset_port.png"
F_quitter 	 = "fenetre/icones/Quitter.png"

# variable contenant le message 
PortDispo = "select port" 

# Fichier contenant le port et le baudRate
FICHIER_1 = "fenetre/sous_fenetres/Connexion/Port&AccessBaud.rs.rachel"
FICHIER_2 = "fenetre/sous_fenetres/Connexion/Manager/MANAGER.rs.rachel"
FICHIER_3 = "fenetre/sous_fenetres/Connexion/Manager/ID_MANAGER.rs.rachel"
FOLDER    = "fenetre/sous_fenetres/Connexion"

class mainWindow:
	"""	
		INFORMATION:
			*Ce fichier permet de créer la fenêtre principale

			*Fait appel à tous les fichiers nécessaire pour le bon fonctionnement
			du programme
	"""
	def __init__(self):

		# Variable permettant de stocker la valeur de la touche selectionné
		# pour agrandir ou reduire l'écran
		self.touche = " "

		# Déclaration de l'object tkinter 
		self.fenetrePrincipale = tk.Tk()
		# fenetre non redimensionnable
		self.fenetrePrincipale.resizable(width=False, height=False)

		# Titre et icone de la fenetre
		self.fenetrePrincipale.title(F_titre)
		self.fenetrePrincipale.iconbitmap(F_icone)

		# methode contenenat les propriétés de le fenetre
		self.ProprieteFenetre()

		# Création du canvas principal conteneur de l'image de fond
		img0 = Image.open(F_imageFond)
		Image0 = img0.resize((self.W_imgFond,self.H_imgFond))
		self.image_fond = ImageTk.PhotoImage(Image0)

		# Création de la Zone central contenant les widgets (Canvas conteneur de l'image de fond)
		self.F_CentralCanvas = tk.Canvas(self.fenetrePrincipale,width=self.W_imgFond,
			height=self.H_imgFond)
		self.F_CentralCanvas.pack(fill="both", expand=True)
		self.F_CentralCanvas.create_image(0, 0, image=self.image_fond,anchor="nw")

		# Appel aux methodes
		self.BarreMenu()
		self._BarOutils()
		self._BottomBar()

		""" vérification de l'existance des fichiers :
			*MANAGER.rs.rachel : contient les infos du MANAGER
			*ID_MANAGER.rs.rachel : contient l'identifiant de la carte

		NB: 
			*personnel pouvant acceder à toutes les options proposé
			
			*si les fichiers n'existe pas, une fenêtre s'ouvre pour
			 enregistrer les infos du MANAGER ou du personnel pouvant
			 acceder à toutes les options proposé
		"""
		try:
			with open(FICHIER_2,'rb') as fichier:
				mon_depickler = pic.Unpickler(fichier)
				self.M_ID = mon_depickler.load()#chemin d'access photo
				self.M_ID = mon_depickler.load()#NOM
				self.M_ID = mon_depickler.load()#PRENOM
				self.M_ID = mon_depickler.load()#DATE OF BIRTH
				self.M_ID = mon_depickler.load()#GENRE
				self.M_ID = mon_depickler.load()#ETAT CIVIL
				self.M_ID = mon_depickler.load()#VILLE
				self.M_ID = mon_depickler.load()#PAYS
				self.M_ID = mon_depickler.load()#PROFESSION
				self.M_ID = mon_depickler.load()#SECTEUR
				self.M_ID = mon_depickler.load()#IDCARTE

			with open(FICHIER_3,'rb') as fichier:
				pass
			
		except:
			SM.F_CarteManager(parent=self.fenetrePrincipale)
		

	""" 
		Définition des proprieté de la fenètre:
		Redimentionnement de la fenetre F1(Agrandir) Escape ou Echap(Reduire)
	"""
	def ProprieteFenetre(self):
		# obtention de la taille de l'écran
		self.H_ecran = int(self.fenetrePrincipale.winfo_screenheight())
		self.W_ecran = int(self.fenetrePrincipale.winfo_screenwidth())
		
		# s'exécute au lancement du programme pour definir la taille de la fenêtre
		if self.touche == " ":
			self.DimensionMinimalFenetre() # appel a la méthode
			# Definition des dimension et centrage de la fenetre
			self.fenetrePrincipale.geometry("{}x{}+{}+{}".format(self.MIN_LARGEUR,
				self.MIN_HAUTEUR,self.pos_x,self.pos_y))
			self.fenetrePrincipale.state('normal')
			self.fenetrePrincipale.update()
		
		# mise a jour de la fenêtre si bouton F1 ou Esc appuyer
		self.fenetrePrincipale.bind("<Key>", self.GestionTailleFenetre)	
		

	# Gestion de l'évenement redimentionnement de la fenêtre
	def GestionTailleFenetre(self,event):		
		self.touche = event.keysym
		if self.touche  == "F1":
			self.FenetreMaximal()
		if self.touche  == "Escape":
			self.FenetreMinimal()
	

	# Calcule des dimention minimale de la fenêtre
	def DimensionMinimalFenetre(self):
		# calcule de la taille minimale de la fenetre
		self.MIN_HAUTEUR = int(self.H_ecran/1.2)
		self.MIN_LARGEUR = int(self.W_ecran/1.2)

		# Dimension minimal de l'image de fond
		self.H_imgFond = self.MIN_HAUTEUR
		self.W_imgFond = self.MIN_LARGEUR 

		# centrage de la fenetre : calcul des coordonnées
		self.pos_x = int((self.W_ecran - self.MIN_LARGEUR)/2)
		self.pos_y = int((self.H_ecran - self.MIN_HAUTEUR)/4)

		# taille minimal de la fenetre
		self.fenetrePrincipale.minsize(self.MIN_LARGEUR,self.MIN_HAUTEUR)


	# Configuration de la fenêtre Manimale
	def FenetreMinimal(self):
		self.DimensionMinimalFenetre() # appel au module
		# Définition des dimension et centrage de la fenetre
		self.fenetrePrincipale.geometry("{}x{}+{}+{}".format(self.MIN_LARGEUR,
			self.MIN_HAUTEUR,self.pos_x,self.pos_y))
		self.fenetrePrincipale.state('normal')
		self.fenetrePrincipale.update()

	# Configuration de la fenêtre Maximale
	def FenetreMaximal(self):
		# Dimension minimal de l'image de fond
		self.H_imgFond = (self.H_ecran - 68)
		self.W_imgFond = self.W_ecran 

		img0 = Image.open(F_imageFond)
		Image0 = img0.resize((self.W_imgFond,self.H_imgFond))
		self.image_fond = ImageTk.PhotoImage(Image0)

		# mise a jour de la taille de la fenêtre
		self.fenetrePrincipale.state("zoomed")
		self.fenetrePrincipale.update()

		# mise à jour de la du l'arrière plan
		self.F_CentralCanvas.create_image(0, 0, image=self.image_fond,anchor="nw")



	""" 
		Methode utilisant le module NouvelleCarte qui contient la classe
		F_NouvelleCarte() permettant de créer la fenètre d'enregistrer de nouvelle carte
	"""
	def FenetreNouvelleCarte(self,master=None):
		self.configureConnexion()
		NC.F_NouvelleCarte(parent = self.fenetrePrincipale)


	""" 
		Methode utilisant le module ModifierCarte qui contient la classe
		F_ModifierCarte() permettant de créer la fenètre de modification et / ou
		d'enregistrer de carte
	"""
	def FenetreModifierCarte(self,master=None):
		self.configureConnexion()
		MC.F_ModifierCarte(parent=self.fenetrePrincipale)


	""" 
		Methode utilisant le module InfosDuPersonnel qui contient la classe
		InfosPersonnel() permettant de voir les informations du personnel
	"""
	def FenetreInfosPersonnel(self,master=None):
		self.configureConnexion()
		IP.InfosPersonnel(parent=self.fenetrePrincipale,fichier="INFOS PERSONNEL")	


	""" 
		Methode utilisant le module InfosDuPersonnel qui contient la fonction
		suppressionFichier() permettant de supprimer les informations du personnel,
		les fichiers des informations récentes des cartes lu
	"""
	def FenetreSupprimerID(self,master=None):
		self.configureConnexion()
		SP.suppressionFichier(parent = self.fenetrePrincipale, fichier="SUPPRIMER PERSONNEL")
	

	""" 
		Methode utilisant le module InfosDuPersonnel qui contient la classe
		InfosPersonnel() permettant de voir les informations des badges récemment
		lu
	"""
	def FenetreBadgeRecent(self,master=None):
		self.configureConnexion()
		IP.InfosPersonnel(parent=self.fenetrePrincipale,fichier="BADGE_LU",
			dossier="BADGE_LU",title="informations Badge récent")	


	"""
		Obtention et enregistrement du port disponible et du baudrate dans un fichier 
		via la fenêtre principale du logiciel afin d'établier la connexion et l'arduino
		dans les fonctions et méthodes nécessitant le "port série et le baudrate"
		pour son bon fonctionnement.
	"""
	def configureConnexion(self):
		# Obtention du port serie
		getport = self.ComboPort.get()
		Available_port =""
		"""
			Lecture des caractères correspondant au port disponible jusqu'au vide(" ")
			exemple : "COM5 - (Arduino Mega at COM5)"
			Available_port = "COM5" à la fin de la boucle for
		"""
		for x in getport:
			if x == " ":
				if Available_port == "select":
					Available_port = ""
				break
			Available_port += x 

		# obtention du baud
		getbaud = str(self.ComboBaudRate.get())

		try:
			getbaud = int(getbaud)
		except:
			tk.messagebox.showwarning(parent=self.fenetrePrincipale,title="Attention",
				message="baudrate non selectionné")

		try:
			# Création du dossier s'il existe pas
			try:
				os.mkdir(FOLDER)
			except FileExistsError:
				pass

			# Stockage des infos du PORT et du BAUDRATE pour utilisation
			# futur dans différentes méthodes
			with open(FICHIER_1,"wb") as fichier:
				mon_pickler	 = pic.Pickler(fichier)
				mon_pickler.dump(Available_port)
				mon_pickler.dump(getbaud)
		except:
			tk.messagebox.showwarning(parent=self.fenetrePrincipale,
				title="Attention",message="port et baudrate non disponible")



	# Fenêtre de lecture des cartes RFID
	def FenetreDemarrer(self,master=None):
		self.configureConnexion()
		DM.F_Demarrer(self.fenetrePrincipale)



	""" 
		Configuration de la fenetre principale
	"""
	def BarreMenu(self):

		self.menubar = tk.Menu(self.F_CentralCanvas)

		# Création du menu "Acceuil" et ses sous-menu
		self.menuAcceuil = tk.Menu(self.menubar, tearoff=0)
		self.menuAcceuil.add_command(label="Démarrer", accelerator="CTRL+D",
			command=self.FenetreDemarrer)
		self.menuAcceuil.add_command(label="Infos personnel", accelerator="CTRL+I",
			command=self.FenetreInfosPersonnel)
		self.menuAcceuil.add_command(label="Supprimer personnel", accelerator="CTRL+P",
			command=self.FenetreSupprimerID)
		self.menuAcceuil.add_command(label="Bagde lu", accelerator="CTRL+P",
			command=self.FenetreBadgeRecent)
		self.menuAcceuil.add_separator()
		self.menuAcceuil.add_command(label="Quitter", accelerator="CTRL+Q",
			command=self._Close)
		self.menubar.add_cascade(label="Acceuil", menu=self.menuAcceuil)

		# prise en compte des raccourcis
		self.fenetrePrincipale.bind("<Control-d>", self.FenetreDemarrer)
		self.fenetrePrincipale.bind("<Control-i>", self.FenetreInfosPersonnel)
		self.fenetrePrincipale.bind("<Control-p>", self.FenetreBadgeRecent)
		self.fenetrePrincipale.bind("<Control-q>", self._Close)
		self.fenetrePrincipale.bind("<Control-D>", self.FenetreDemarrer)
		self.fenetrePrincipale.bind("<Control-I>", self.FenetreInfosPersonnel)
		self.fenetrePrincipale.bind("<Control-p>", self.FenetreBadgeRecent)
		self.fenetrePrincipale.bind("<Control-Q>", lambda x: quit())

		# Création du menu "Ajouter" et ses sous-menu
		self.menuAjouter = tk.Menu(self.menubar, tearoff=0)
		self.menuAjouter.add_command(label="Nouvelle carte", accelerator="CTRL+N", command=self.FenetreNouvelleCarte)
		self.menuAjouter.add_command(label="Modifier carte", accelerator="CTRL+M", command=self.FenetreModifierCarte)
		self.menubar.add_cascade(label="Ajouter", menu=self.menuAjouter)
		
		# prise en compte du raccourci
		self.fenetrePrincipale.bind("<Control-n>", self.FenetreNouvelleCarte)
		self.fenetrePrincipale.bind("<Control-N>", self.FenetreNouvelleCarte)
		self.fenetrePrincipale.bind("<Control-m>", self.FenetreModifierCarte)
		self.fenetrePrincipale.bind("<Control-M>", self.FenetreModifierCarte)

		# Création du menu "Aide" et ses sous-menu
		self.menuAide = tk.Menu(self.menubar, tearoff=0)
		self.menuAide.add_command(label="Documentation", accelerator="ALT+D", command=BI.Documentation)
		self.menuAide.add_command(label="A propos de RS ", accelerator="ALT+P", command=BI.A_propos_de_RS)
		self.menuAide.add_command(label="A propos du logiciel ", accelerator="ALT+H", command=BI.A_propos_du_logiciel)
		self.menubar.add_cascade(label="Aide", menu=self.menuAide)

		# prise en compte du raccourci
		self.fenetrePrincipale.bind("<Alt-d>", BI.Documentation)
		self.fenetrePrincipale.bind("<Alt-D>", BI.Documentation)
		self.fenetrePrincipale.bind("<Alt-p>", BI.A_propos_de_RS)
		self.fenetrePrincipale.bind("<Alt-P>", BI.A_propos_de_RS)
		self.fenetrePrincipale.bind("<Alt-h>", BI.A_propos_du_logiciel)
		self.fenetrePrincipale.bind("<Alt-H>", BI.A_propos_du_logiciel)

		# configuration du menu
		self.fenetrePrincipale.config(menu=self.menubar)



	# Configuration de la barre d'outils
	def _BarOutils(self):
		# Frame porteur de la barre d'outil
		toolbar = tk.Frame(self.F_CentralCanvas, relief=tk.GROOVE, bd=3, bg=Coleur)

		# Bouton Démarrer
		img1 = Image.open(F_demarrer)
		Image1 = img1.resize((B_W,B_H))
		self.ImgDemarrer = ImageTk.PhotoImage(Image1)
		# Creation et affichage du bouton "Démarrer"
		startButton = tk.Button(toolbar,relief=tk.GROOVE,image=self.ImgDemarrer,
			height= B_H,width=B_W,command=self.FenetreDemarrer)
		ToolTip(startButton, msg="Démarrer\nlecture badge")
		startButton.pack(side=tk.LEFT,padx=2,pady=2)

		# Bouton Liste des "Infos personnel"
		img2 = Image.open(F_ListeCarte)
		Image2 = img2.resize((B_W,B_H))
		self.ImgListeCarte = ImageTk.PhotoImage(Image2)
		# creation et affichage du bouton "Infos personnel"
		BoutonListeCarte = tk.Button(toolbar,relief=tk.GROOVE,image=self.ImgListeCarte,
			height= B_H,width=B_W,command=self.FenetreInfosPersonnel)
		ToolTip(BoutonListeCarte, msg="Infos personnel")
		BoutonListeCarte.pack(side=tk.LEFT,padx=2,pady=2)

		# Bouton Nouvelle Carte
		img3 = Image.open(F_newCarte)
		Image3 = img3.resize((B_W,B_H))
		self.ImgNewID = ImageTk.PhotoImage(Image3)
		# creation et affichage du bouton "Nouvelle Carte"
		NewIDButton = tk.Button(toolbar,relief=tk.GROOVE,image=self.ImgNewID,
			height= B_H,width=B_W,command=self.FenetreNouvelleCarte)
		ToolTip(NewIDButton, msg="Nouvelle Carte")
		NewIDButton.pack(side=tk.LEFT,padx=2,pady=2)

		# Bouton "A propos de RS"
		img4 = Image.open(F_Aproposde)
		Image4 = img4.resize((B_W,B_H))
		self.ImgAproposde = ImageTk.PhotoImage(Image4)
		#creation et affichage du bouton "A propos de RS"
		NewAproposde = tk.Button(toolbar,relief=tk.GROOVE,image=self.ImgAproposde,
			height= B_H,width=B_W,command=BI.A_propos_de_RS)
		ToolTip(NewAproposde, msg="A propos de RS")
		NewAproposde.pack(side=tk.LEFT,padx=2,pady=2)

		# Bouton "Fermer la fenètre"
		img5 = Image.open(F_quitter)
		Image5 = img5.resize((B_W,B_H))
		self.ImgQuitter = ImageTk.PhotoImage(Image5)
		# Création et affichage du bouton "Fermer la fenètre"
		exitButton = tk.Button(toolbar,relief=tk.GROOVE,image=self.ImgQuitter,
			height= B_H,width=B_W,command=self._Close)
		ToolTip(exitButton, msg="Fermer la fenêtre")
		exitButton.pack(side=tk.RIGHT,padx=5,pady=2)
		
		# Configuration du combox choix BAUDRATE
		# label affichant le message "baudRate"
		tk.Label(toolbar, text="baudRate", bg="white").pack(side=tk.LEFT,padx=10)
   		# liste des valeurs de baudRate (taux d'échange)
		listOfBaudRateValue = ["1200","2400","4800","9600","19200","38400","57600","115200"]
		# Création d'un combox affichant la liste des valeurs de baudRate
		self.ComboBaudRate = ttk.Combobox(toolbar,values=listOfBaudRateValue,
			width=15,height=B_H,state ="readonly")
		self.ComboBaudRate.set("Select baudRate")
		self.ComboBaudRate.pack(side=tk.LEFT)

		# Configuration du combox choix Port série
		# label affichant le message "PORT SERIE"
		tk.Label(toolbar, text="Port", bg="white").pack(side=tk.LEFT,padx=10)
	
		# Création d'un combox affichant les ports
		self.ComboPort = ttk.Combobox(toolbar,width=40,height=B_H,state ="readonly")
		self.ComboPort.set(PortDispo)
		self.ComboPort.pack(side=tk.LEFT)

		# Bouton Reset port
		img5 = Image.open(F_ResetPort)
		Image5 = img5.resize((B_W,B_H))
		self.ImgResetPort = ImageTk.PhotoImage(Image5)
		# Création et affichage du bouton "Reset Port"
		ResetPort = tk.Button(toolbar,relief=tk.GROOVE,height=B_H,width=B_W,
			image=self.ImgResetPort,command=self._ListePortDispo)
		ToolTip(ResetPort, msg="Reset port")
		ResetPort.pack(side=tk.LEFT,padx=2,pady=2)

		# affichage de la barre d'outil
		toolbar.pack(side=tk.TOP, fill=tk.X)


	# Methode permettant de metre à jour le nombre de port disponible
	def _ListePortDispo(self,master=None):
		listOfPortValue =[]
		for port in list(serial.tools.list_ports.comports(include_links=False)):
			listOfPortValue.append(port)

		self.ComboPort.config(values=listOfPortValue)


	# Configuration de la barre inférieur
	def _BottomBar(self):
		BottomBar = tk.Frame(self.F_CentralCanvas, relief=tk.GROOVE,
			height= 30, bd=2, bg=Coleur)
		labelPort = tk.Label(BottomBar, text=TextBottom, bg=Coleur).pack()
		BottomBar.pack(side=tk.BOTTOM, fill=tk.X)


	# Suppression du fichier contenant le port série s'il existe
	def _Close(self,master=None):
		r = messagebox.askquestion( "Fermer la fenêtre",
									"Voulez - vous fermer la fenêtre ?"
									)
		if r == "yes":
			try:
				os.remove(FICHIER_1)	
			except FileNotFoundError:
				pass
			self.fenetrePrincipale.destroy()


	# Méthode qui permet d'affiché et de gérer les évements tkinter
	def run(self):
		self.fenetrePrincipale.protocol("WM_DELETE_WINDOW", self._Close)
		self.fenetrePrincipale.mainloop()