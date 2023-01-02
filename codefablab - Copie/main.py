#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AUTEUR: RACHEL SYSTEME
DATE  DE DEBUT: DECEMBRE 2021
DATE DE FIN : 10/01/2022

________________________DESCRIPTION DU FICHIER___________________________

Fichier principal du programme, exécuter le afin de démarrer le programme

INFORMATION: MODULES NECESSAIRE A AJOUTER
	*datetime 
	*pillow
	*pyserial
	*tktooltip
		installation sur windows 10 : ouvrir le cmd
			py -m pip install datetime
			py -m pip install pillow
			py -m pip install pyserial
			py -m pip install tkinter-tooltip==1.2.1

NB: 
	fenetrePrincipale.py : Fichier contenant la définition de tout le programme

FONCTIONNEMENT:
	Ce programme consiste à créer une fenêtre GUI qui intéragis avec Arduino.
		*Stock les informations d'une carte RFID
		*Affiche les informations stockées si la carte passé sur le lecteur
		est enregistré.
		*Renvoie "TRUE" ou "FALSE" selon que la carte passé est enregistrée ou pas

NB:  
	DISFONCTIONNEMENT DU PROGRAMME:
		*Passer deux fois la carte sur le lecteur RFID afin d'envoyer le message
		"TRUE" ou "FALSE" à l'arduino
		*Une fois la fenêtre "DEMARRER" ouverte, ne pas appuyer le bouton "ANNULER"

	PLUS D'INFORMATIONS:
		LIRE LE DOC "readme"
		Suivez la vidéo :
			Lien: https://youtu.be/NB6gdh4_NL4

"""
import fenetrePrincipale as fp

fenetre = fp.mainWindow()

fenetre.run()
