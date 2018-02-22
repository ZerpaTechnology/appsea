
from modulos.controlador import Controlador

from Controladores.http.default import default 

class Inicio(default):
	def __init__(self,data,headers=None):

		default.__init__(self,data,headers)
	

		self.vista="index"
		
		if data["metodo"]==None and data["control"]==None and data["action"]==None:
			self.servir()
		self.modelo=data["model"]["paginas"]
		

	def acerca(self):
		self.add_vista("acerca")
		self.servir()
	def servicios(self):
		self.add_vista("servicios")
		self.servir()
	def faqs(self):
		self.add_vista("faqs")
		self.servir()
	def contacto(self):
		self.add_vista("contacto")
		self.servir()
	def Instalaciones(self):
		self.add_vista("instalaciones")
		self.servir()

	def metodo_desconocido(self):
		if self.data["control"]=="gallery":
			self.add_vista("gallery")
			self.servir()
		elif self.data["control"]=="full-width":
			self.add_vista("full-width")
			self.servir()
		elif self.data["control"]=="sidebar-left":
			self.add_vista("sidebar-left")
			self.servir()
		elif self.data["control"]=="sidebar-right":
			self.add_vista("sidebar-right")
			self.servir()
		elif self.data["control"]=="basic-grid":
			self.add_vista("basic-grid")
			self.servir()
		

		
		