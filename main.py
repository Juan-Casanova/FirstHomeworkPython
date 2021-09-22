import operator

nombre = input("Cual es el nombre del archivo: ")
listaDePalabras = []
contadorDePalabras = {}
list2 = {}

def checadorNombre(nombre):
    try:
        file = open(nombre)
        texto = file.read()
        listaDePalabras = texto.split(" ")
        for palabra in listaDePalabras:
            contadorDePalabras[palabra] = contadorDePalabras.get(palabra, 0)+1
        checadorMaxMin()
    except:
        name1 = input("No existe el nombre ingrese uno valido: ")
        checadorNombre(name1)

def checadorMaxMin():

    list = sorted(contadorDePalabras.items(), key=lambda kv: kv[1], reverse = True)
    for x in list:
        if list.index(x) < 11:
            print(x)

checadorNombre(nombre)