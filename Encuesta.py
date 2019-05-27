from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from numpy import *
from Proyecro2_Encuesta import *

#Autores:María José Lemus 181202, André Rodriguez, Javier Salazar 18764
#Proyecto 2 Estructuras de Datos
#Fecha: 24/05/2019
#Descripción: Sistema de recomendaciones de libros, ya sea por autor, numero de paginas, costo del libro, genero del libro
#Descripción: Sistema de recomendaciones de libros, ya sea por autor, numero de paginas, costo del libro, genero="" del libro
#El algoritmo de recomendacion fue tomado y editado de: https://github.com/andresum97/Proyecto2

#Se importa el grafo desde neo4j
#Nota: Se necesita instalar neo4jrestclient para que se conecte a la base de datos

#Conexión a la base de datos, usando el puerto, el usuario y la contraseña de la base de datos
db = GraphDatabase("http://localhost:11002", username="neo4j", password="1234")

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


def main():
    mal = "Ingrese un valor correcto"
    print(
        "Bienvenido BookRec\nProcederemos a Realizarle una serie de preguntas con las cuales podemos determinar los "
        "libros mas ahuevo para usted.\nAntes de inciar la encuesta tomaremos unos datos de usted. Los datos no seran "
        "compartidos a terceros.")
    name=gender=grade =""
    age =0
    op = 0
    
    print("**********************************")
    print("     Bienvenido a de Bookstore")
    print("**********************************")
    print("1. Nuevo usuario")
    print("2. Ver Recomendaciones")
    print("3. Salir")
    while op != 3:
        op = input(" ")
        while not op.isdigit():
            op = input("Ingese una opción valida: ")
        op = int(op)
        if op ==1:
            print ("")
            print("************************************")
            print("             Nuevo usuario")
            print("************************************")
            #Solicitud de informacion
            nombre = input("ingrese su nombre: ")
            edad = input("ingrese su edad: ")
            genero = input("ingrese su genero: ")
            eduacion = input("ingrese su nivel educativo: ")
            #Ingreso del usuario a la base de datos
            user = db.nodes.create(name=nombre,age=edad,gen=genero,ed= eduacion)
            Usuarios.add(user)
            print("Usuario agregado")
            print()
            print("**********************************")
            print("     Bienvenido a de Bookstore")
            print("**********************************")
            print("1. Nuevo usuario")
            print("2. Ver Recomendaciones")
            print("3. Salir")
            
        if op ==2:
            #Recomendación por intereses
            print("************************************")
            print("       Ver Recomendaciones" )
            print("************************************")
            #Area de preguntas para determinar generos
            preguntas = ["Te gusta leer", "Te gusta el romance",
                         "Te gusta la poesia", "Te gusta la ciencia ficción",
                         "Te gustan las historias de terror",
                         "Te gustan las historias policiacas", "Te gustan las sagas",
                         "Te gusta la aventura"]
            #En este arreglo se van filtrando cada respuesta
            #los generos restantes son los de interes del usuario
            respuestas = [["Ensayo", "Periodistico"], ["Dramatico", "Narrativa"], ["Poesia", "Prosa"], ["Ciencia Ficcion"],
                          ["Terror"], ["Novela Negra"], ["Sagas"], ["Sagas"]]
            for x in range(0, 8):
                Preguntar(preguntas[x], respuestas[x])
            bandera = True
            respaginas = ""
            #Otro de los filtros a tomar en cuenta para recomentar
            #numero de paginas y costo del mismo 
            while bandera:
                muchaspaginas = input("Que tantas paginas le importa que su libro tenga?\n1. 0 - 250 pags\n2. 251 -en adelante pags\n").lower().strip()
                if muchaspaginas == "1" or muchaspaginas == "2":
                    bandera = False
                    #opciones de respuestas
                    respaginas = "De 0 a 250 paginas" if (muchaspaginas == "1") else "De 251 paginas en adelante" 
                else:
                    print(mal)
            bandera = True
            costo = 0
            while bandera:
                try:
                    #pregunta el costo dispuesto a pagar
                    costo = int(input("Que tan costoso puede que ser su libro\n1. Barato\n2. Medio\n3. Caro\n"))
                    if costo < 1 or costo > 3:
                        raise Exception()
                    bandera = False
                    costo2 = "Gratis PDF" if costo == 1 else "0-150" if costo == 2 else "150-300"
                except:
                    print(mal)
            #Hace una llamada a la función en Proyecto2_Encuesta
            #En este determina la recomendacion
            print("Los libros que recomendamos son: ")
            for e in generos:
                hacerrecomendacion(e,respaginas, costo2)
            print("**********************************")
            print("     Bienvenido a de Bookstore")
            print("**********************************")
            print("1. Nuevo usuario")
            print("2. Ver Recomendaciones")
            print("3. Salir")
            
    else:
        print("Gracias por su prefencia. Disfrute su lectura")
        
main()
