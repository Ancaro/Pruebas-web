class Estudiante(object):
	def __init__(self,nombre_r,edad_r,curso_r):
		self.nombre=nombre_r
		self.edad=edad_r
		self.curso=curso_r
	def presentate(self):
		return "Hola, mi nombre es %s, tengo %i anos y estoy en %s" % (self.nombre,self.edad,self.curso)

e=Estudiante('Andres',26,'Nivel Dios')
print e.presentate()
