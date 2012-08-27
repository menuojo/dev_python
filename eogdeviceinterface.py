# -*- coding: UTF-8 -*

from abc import ABCMeta, abstractmethod

class EOGDeviceInterface:
	__metaclass__ = ABCMeta

	"""Obtener datos que se pueden obtener desde el dispositivo EOG como son la posicion
	   horizontal, vertical y el pestaneo de los ojos. Puede obtenerse el dato para cada ojo en 
	   particular si el dispositivo lo soporta. Tambien se pueden obtener datos extras para dar 
        un punto de extensibilidad a la interza. Por ejemplo el voltaje de los sensores del 
	   dispositivo EOG.
	""" 
	@abstractmethod
	def getData(self):
		raise NotImplementedError( "Debe implementar este metodo" )		

	"""Obtiene los tipos de datos que el dispositivo es capaz de brindar. Por ejemplo, posicion 
	   vertical, horizontal, etc. Se podria especificar ademas precision de los datos, frecuencia 
	   de actualizacion de los datos,..
	"""
	@abstractmethod
	def getCapabilities(self):
		raise NotImplementedError( "Debe implementar este metodo" )		

	@abstractmethod
	def setCapabilities(self):
		raise NotImplementedError( "Debe implementar este metodo" )		

	@abstractmethod
	def getDefaultCapabilities(self):
		raise NotImplementedError( "Debe implementar este metodo" )		

	@abstractmethod
	def open(self):
		raise NotImplementedError( "Debe implementar este metodo" )		

	@abstractmethod
	def close(self):
		raise NotImplementedError( "Debe implementar este metodo" )		


class CapabilitiesData:

	LEFT_HORIZONTAL_POSITION_SUPPORT = False
	LEFT_VERTICAL_POSITION_SUPPORT = False
	LEFT_BLINK_SUPPORT = False
	RIGHT_HORIZONTAL_POSITION_SUPPORT = False
	RIGHT_VERTICAL_POSITION_SUPPORT = False
	RIGHT_BLINK_SUPPORT = False
	ACCURACY_SUPPORT = False

