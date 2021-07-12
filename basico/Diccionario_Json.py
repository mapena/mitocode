import json
#manejo de lista
mi_lista = ['a','b','c']
print("mi_lista:", mi_lista)
print("mi_lista 2do elemento:", mi_lista[1])
for x in mi_lista:
    print("for mi_lista elemento :",x)

#manejo de diccionario, para almacenar las variables de diccionarios se necesita la libreria JSON para guardarlas.
persona = {
 'nombre':'luis',
 'edad':25,
 'altura': 1.75,   
 'notas': [10,20,30,40]
}

print("persona:",persona)
print("persona-nombre:",persona['nombre'])
print("persona-notas:",persona['notas'])
print("persona-notas 2da nota:",persona['notas'][1])

lista_personas = [
    {
        'nombre':'luis',
        'edad':25,
        'altura': 1.75,   
        'notas': [10,20,30,40]
    },
    {
        'nombre':'pedro',
        'edad':35,
        'altura': 1.75,   
        'notas': [10,20,30,40]
    },
    {
        'nombre':'juan',
        'edad':15,
        'altura': 1.5,   
        'notas': [10,20,30,40]
    }

]

print("lista_persona - nombre (pedro):", lista_personas[1]['nombre']) 
for x in lista_personas:
    print("for lista_personas x elemento :",x)


base_datos = []
# ingresar los datos en forma manual
#[{'nombre': 'pedro', 'edad': '10'}, {'nombre': 'juan', 'edad': '20'}, {'nombre': 'luis', 'edad': '30'}, {'nombre': 'marcelo', 'edad': '40'}, {'nombre': 'lucas', 'edad': '50'}]
for i in range(5):
    persona2 = {}
    nombre = input('ingrese nombre:')
    edad = input('ingrese edad:')
    persona2['nombre'] = nombre
    persona2['edad'] = edad
    base_datos.append(persona2)


print(base_datos)


# abro archivo de write, y el id para python es archivo1
with open('miarchivo.txt', 'w') as archivo1:
     # graba archivo con formato json
    json.dump(base_datos, archivo1)
    print("archivo exportado")


with open('miarchivo.txt', 'r') as archivo2:
    base_datos=json.load(archivo2)
    print("archivo leido")

print (base_datos)
