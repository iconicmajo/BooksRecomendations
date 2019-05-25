from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from numpy import *

#Autores:María José Lemus, André Rodriguez, Javier Salazar 18764
#Proyecto 2 Estructuras de Datos
#Fecha: 24/05/2019
#Descripción: Sistema de recomendaciones de libros, ya sea por autor, numero de paginas, costo del libro, genero del libro

#Se importa el grafo desde neo4j
#Nota: Se necesita instalar neo4jrestclient para que se conecte a la base de datos
from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client

#Conexión a la base de datos, usando el puerto, el usuario y la contraseña de la base de datos
db = GraphDatabase("http://localhost:7474", username="neo4j", password="1234")

generos = ["Novela Negra", "Dramatico", "Terror", "Prosa", "Ensayo", "Narrativa", "Novela",
           "Ciencia Ficcion", "Periodistico", "Sagas", "Aventura", "Poesia"]

#Funcion para las preguntas
def Preguntar(pregunta, respuestas):
    bandera = True
    respuesta = ""
    while bandera:
        respuesta = input(pregunta+"\n1. Si\n2. No\n").lower().strip()
        if respuesta == "si" or respuesta == "no":
            bandera = False
        else:
            print("Ingrese un valor correcto")
    if respuesta == "no":
        for i in respuestas:
            if i in generos:
                generos.remove(i)

#Funcion del main
def main():
    mal = "Ingrese un valor correcto"
    print(
        "Bienvenido BookRec\nProcederemos a Realizarle una serie de preguntas con las cuales podemos determinar los "
        "libros mas "
        "de ahuevo para usted.\nAntes de inciar la encuesta tomaremos unos datos de usted. Los datos no seran "
        "compartidos a "
        " terceros.")
    banderaedad = True
    nombre = genero = niveleducativo = ""
    edad = 0
    # -----------------------Se pide información al usuario------------------------------#
    while (nombre.strip() == ""):
        nombre = input("¿Cuál es tu nombre? ").strip()
        user = db.nodes.create(name=nombre)
        Usuarios.add(user)
        if (nombre == ""):
            print(mal)
    while (banderaedad):
        try:
            edad = int(input("¿Qué edad tiene actualmente? "))
            age = db.nodes.create(name=edad)
            Edades.add(age)
            banderaedad = False
        except:
            print(mal)
    while (genero.strip() == ""):
        genero = input("¿Con qué genero se identifica? ").strip()
        gender = db.nodes.create(name=genero)
        Generos.add(gender)
        if (genero == ""):
            print(mal)
    bandera = True
    while bandera:
        niveleducativo = input("¿Cual es su nivel educativo?\na. Bachillerato\nb. Licenciatura\nc. "
                               "Posgrado\n").lower()
        
        if niveleducativo == "":
            print(mal)
        else:
            educative = db.nodes.create(name=niveleducativo)
            Nivel_Educativo.add(educative)
        if niveleducativo == "a":
            bandera = False
        elif niveleducativo == "b":
            bandera = False
        elif niveleducativo == "c":
            bandera = False
        else:
            print(mal)
    #----------------------Se realizan las preguntas-----------------------------------
    preguntas = ["Te gusta leer", "Te gusta el romance",
                 "Te gusta la poesia", "Te gusta la ciencia ficción",
                 "Te gustan las historias de terror",
                 "Te gustan las historias policiacas", "Te gustan las sagas",
                 "Te gusta la aventura"]
    respuestas = [["Ensayo", "Periodistico"],["Dramatico", "Narrativa"], ["Poesia", "Prosa"], ["Ciencia Ficcion"], ["Terror"], ["Novela Negra"], ["Sagas"], ["Sagas"]]
    for x in range(0, 8):
        Preguntar(preguntas[x], respuestas[x])
    print(generos)
    result = db.nodes.create(name=generos)
    genders_Result.add(result)
    result.relationships.create("Los libros que le recomendamos son: ", user)
    user.relationships.create("La edad del usuario es: ", age)
    user.relationships.create("El grado academico del usuario es: ", educative)
    bandera=True
    respaginas = True
    while bandera:
        muchaspaginas= input("Le importa la cantidad de páginas\n").lower().strip()
        if muchaspaginas == "si" or muchaspaginas == "no":
            bandera=False
            resppaginas = True if (muchaspaginas=="si") else False
        else:
            print(mal)
    bandera = True
    costo = 0
    while bandera:
        try:
            costo = int(input("Que tan costoso puede que ser su libro\n1. Barato\n2. Medio\n3. Caro\n"))
            if costo<1 or costo>3:
                raise Exception()
            bandera=False
        except:
            print(mal)

    
main()




