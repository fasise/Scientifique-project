#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import serial.tools.list_ports

class ListePortCom:
	"""
	____________________DESCRIPTION DU FICHIER_______________________

	INFORMATION:
		*Ce fichier permet de trouver les ports série disponible

	Attribut: 
			self.PortDispo : Contient la liste des ports disponible
			
	UTILISER DANS LE FICHIER :
		**fenetrePrincipale.py
			Methode : 
				**ListePortDispo()
	"""

	def __init__(self):
		super(ListePortCom, self).__init__()
		
		self.PortDispo = [""] # liste contenant les ports disponible
		
		# Obtention des ports disponible
		for port in list(serial.tools.list_ports.comports(include_links=False)):
			self.PortDispo.append(port)

		# Suppression de l'index Vide de la liste
		if len(self.PortDispo) > 0:
			del self.PortDispo[0]