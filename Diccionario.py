mi_diccionario = {"Nombre": "hernan", "edad": 19, "direccion": "daxti"}
mi_diccionario2 = {"Nombre": "Carlos", "edad": 19, "Direccion": "daxti"}
mi_diccionario3 = {"Nombre": "luis", "edad": 18, "Direccion": "San Luis"}
print(mi_diccionario)
print(mi_diccionario2)
print(mi_diccionario3)

print(mi_diccionario3['Nombre']) #hernan
print(mi_diccionario.get('Direccion')) #consulta direccion

#para modificar un elemento usar [] usando el key y asignado otro nombre
mi_diccionario2['Nombre'] = "Lalo"
print(mi_diccionario2)

#si key no existe lo añade
mi_diccionario['codigo postal'] = 54240
print(mi_diccionario)

#values().- devuelve los valores del diccionario
print(list(mi_diccionario.values()))

#popitem. - elimina el ultimo elemento del diccionario
mi_diccionario.popitem()
print(mi_diccionario)

#pop se puede eliminar un elemento en particular
salida = mi_diccionario.pop('edad')
print(mi_diccionario)

#update .- llama un diccionario y tiene como entrada otro diccionario
t1 = {'a' : 100, 'b': 200}
t2 = {'e' : 50, 'd' : 400}
t1.update(t2)
print(t1)