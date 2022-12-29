* DATE : DECEMBRE 2021
* DATE DE FIN : 19/01/2022
* MODIFIER : 28/12/2022

Suite à l'intérêt manifester par certains internautes que ce programme
a été retouchés afin de corriger certains soucis. J'espère que ses 
améliorations vous ont été utiles. Une version plus améliorée est déjà en
cours de développement.
Afin de soutenir notre œuvre et de nous encourager à faire encoure plus,
vous pouvez nous faire une donation via PayPal au lien ci-dessous.
N'hésitez surtout pas de vous abonner à la chaîne, de la partager et d'aimer nos vidéos.
Merci...


* e-mail : rachelsysteme@gmail.com
* gitHub : https://github.com/RS-malik-el
* Donation : paypal.me/RachelSysteme
* YOUTUBE: https://www.youtube.com/channel/UCf4jGfp-BFp6GLd6eTptVMg?sub_confirmation=1


QUELQUES INFORMATIONS UTILES AU LOGICIEL
 	Après lecture des données, cliquer de nouveau sur "START" pour une nouvelle attente des données.
	Vous ne disposé que de 5 secondes pour passer la carte.
	Supprimer l'idée du Manager contenu dans le dossier : fenetre/sous_fenetres/Connexion/Manager/
	si vous voulez le changé.

CONFIGURATION :
	Sélectionner le taux d'échange "BAUDRATE" et le Port série pour établir une connexion et l'arduino.
	Cliquer sur le bouton "RESET" pour afficher les ports disponibles

	Appuyer sur :
		F1 : Pour agrandir la fenêtre
		Escape : pour revenir à la taille minimale de la fenêtre

TRANSMISSION DES DONNEES DE L'ARDUINO AU LOGICIEL
	Insérer dans votre programme une boucle "for" tel que :

	for(int i=0; i<4; i++){
   		Serial.write(Data[i])
	}
	Avec "Data" la variable contenant les 4 bytes identifiant la carte en hexadécimale.

TRANSMISSION DES DONNEES DU LOGICIEL A L'ARDUINO
	Après lecture du badge, le logiciel renvoi les mots suivants:
	"TRUE" : Si le badge est reconnu
	"FALSE" : Si le badge n'est pas reconnu 

...............................MERCI DE VOTRE COMPREHENSION...............................