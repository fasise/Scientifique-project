_____________RACHEL SYSTEME_________________
DATE : DECEMBRE 2021
DATE DE FIN : 19/01/2022

E-mail : rachelsysteme@gmail.com
YOUTUBE: https://www.youtube.com/channel/UCf4jGfp-BFp6GLd6eTptVMg?sub_confirmation=1

QUELQUES INFORMATIONS UTILES AU LOGICIEL

***PROBLEMES POUVONS SURVENIR LORS DU LANCEMENT DES BOITES DE DIALOGUES PERSONNALISEES" :

	Quand vous cliquez sur le bouton "START", le logiciel établit une communication et
	l'arduino et attend de recevoir les informations de la part de la carte Arduino.

	NB : lors de cette phrase, la fenêtre ne peux pas être déplacé et le bouton "ANNULER" ne
	Peut-être cliquer ; message d'erreur :(RS... Ne réponds pas.)

	Pour arrêter cela, il suffit de :
		Faire passer la carte à lire devant le lecteur RFID ou
		Déconnecter la carte connectée en retirant le câble.
		 Après lecture des données, cliquer de nouveau sur "START" pour une nouvelle attente des données

***CONFIGURATION :
	Sélectionner le taux d'échange "BAUDRATE" et le Port série pour établir une connexion et l'arduino.
	Cliquer sur le bouton "RESET" pour afficher les ports disponibles

	Appuyer sur :
		F1 : Pour agrandir la fenêtre
		Escape : pour revenir à la taille minimale de la fenêtre

***TRANSMISSION DES DONNEES DE L'ARDUINO AU LOGICIEL
	Insérer dans votre programme une boucle "for" tel que :

	for(int i=0; i<4; i++){
   	Serial.write(Data[i])
	}
	Avec "Data" la variable contenant les 4 bytes identifiant la carte en hexadécimale.

***TRANSMISSION DES DONNEES DU LOGICIEL A L'ARDUINO
	Après lecture du badge, le logicil renvois les mots suivants:
	"TRUE" : Si le badge est reconnu
	"FALSE" : Si le badge n'est pas reconnu 

_____________________________MERCI DE VOTRE COMPREHENSION_______________________
