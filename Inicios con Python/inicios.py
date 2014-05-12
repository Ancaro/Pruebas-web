print "Hola Andres, lo lograste :')"
print "Ahora vas a empezar a aprender Python en forma"

#Listas (Arreglos)
L=[26,True,'andres',['Luisa',22]]
print L[3][0]

#Tuplas (Arreglos no modificables)
T=('andres',22,'Luisa',21,[23,True])
print T[4][1]

#Diccionarios (casi JSON)
D={'nombre':'Andres','edad':26,'ano':1987}
print D['nombre']

#Funciones con arreglos
L.append(False)
print L
L.pop()
print L
L.remove(2)
print L