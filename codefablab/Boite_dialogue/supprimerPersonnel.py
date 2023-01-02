#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AUTEUR: RACHEL SYSTEME
DATE  : DECEMBRE 2021
DATE DE FIN : 14/01/2022
"""
import os
import tkinter.filedialog as fd
from tkinter import messagebox
import Boite_dialogue.SaveVisitManagerBadge as SVMB

"""
____________________DESCRIPTION DU FICHIER_______________________

INFORMATION:
	*Ce fichier permet de supprimer le contenu d'un fichier ".rachel"
	contenu dans le dossier "IdPersonnel" qui contient les informations 
	reliées à carte à passer devant le lecteur RFID

	*Sélectionner un fichier afin de le supprimer
 

UTILISER DANS LE FICHIER :
	**fenetrePrincipale.py
		Methode : 
			**FenetreSupprimerID()
PARAMETRES:
	Paramètre 1: 
		parent: Fenêtre parent ou principale

	Paramètre 2:
		fichier: Crée un dossier du même Nom que l'onglet ouvert
			par le MANAGER afin d'enregistré l'heure à laquelle l'onglet
			a été ouvert.

"""

def suppressionFichier(parent, fichier):
	Parent  = parent
	Fichier = fichier
	# Enregistre l'heure à laquelle le MANAGER a ouvert l'onglet
	Save_Card_Manager = SVMB.SaveVisitManagerBadge(Parent,fichier = Fichier)

	"""
		Si le Manager donne access
		La fenêtre se crée sinon rien ne se passe
	"""
	if Save_Card_Manager == True:
		try:
			os.mkdir("IdPersonnel")
		except:
			chemin = "IdPersonnel"
		try:
			type_de_fichier =[("fichier rachel",".rachel")] 
			fichier = fd.askopenfilename(title="Selectionner fichier à supprimer",
				filetypes=type_de_fichier,initialdir = chemin)

			os.remove(fichier)
			messagebox.showinfo("Suppression fichier", "Fichier supprimer avec succès")
		except:
			messagebox.showwarning("Suppression fichier", "Echec suppression du fichier")