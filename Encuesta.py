from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from numpy import *
from Proyecto2_Encuesta import *

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

def hacerrecomendacion(respaginas, costo):
    libros = {}
    for i in generos:
        mquery = 'MATCH (g:Generos)-[r:a]->(t:Titulos) WHERE g.name="'+i+'"RETURN g, type(r), t'
        res1 = db.query(mquery, returns=(client.Node, str, client.Node))
        for j in res1:
            mquery = 'MATCH (g:No_Pags)-[r:a]->(t:Titulos) WHERE t.name="'+j[2]["name"]+'"RETURN g, type(r), t'
            res2 = db.query(mquery, returns=(client.Node, str, client.Node))
            for k in res2:
                mquery2 = 'MATCH (g:Costo)-[r:a]->(t:Titulos) WHERE g.name="'+j[2]["name"]+'"RETURN g, type(r), t'
                res3 = db.query(mquery2, returns=(client.Node, str, client.Node))
                for l in  res3:
                    if k[0]["name"] == respaginas and l[0]["name"] == costo:
                        libros[l[2]["name"]]= libros[l[2]["name"]]+5
    for key, value in libros:
        print("- %s" %key)



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
    age = op = 0
    print("**********************************")
    print("     Bienvenido a de Bookstore")
    print("**********************************")
    print("1. Nuevo usuario")
    print("2. Ver Recomendaciones")
    print("3. Relacionar usuarios")
    print("4. Salir")
    op = input(" ")
    while op != 4:
        while not op.isdigit():
            op = input("Ingese una opción valida: ")
        op = int(op)
    if op ==1:
        print ("")
        print("************************************")
        print("             Nuevo usuario")
        print("************************************")
        nombre = input("ingrese su nombre: ")
        edad = input("ingrese su edad: ")
        genero = input("ingrese su genero: ")
        eduacion = input("ingrese su nivel educativo: ")
        user = db.nodes.create(name=nombre,age=edad,gen=genero,ed= eduacion)
        Usuarios.add(user)
        print("listo")
    if op ==2:
        print("************************************")
        print("       Ver Recomendaciones" )
        print("************************************")
        preguntas = ["Te gusta leer", "Te gusta el romance",
                     "Te gusta la poesia", "Te gusta la ciencia ficción",
                     "Te gustan las historias de terror",
                     "Te gustan las historias policiacas", "Te gustan las sagas",
                     "Te gusta la aventura"]
        respuestas = [["Ensayo", "Periodistico"], ["Dramatico", "Narrativa"], ["Poesia", "Prosa"], ["Ciencia Ficcion"],
                      ["Terror"], ["Novela Negra"], ["Sagas"], ["Sagas"]]
        for x in range(0, 8):
            Preguntar(preguntas[x], respuestas[x])
        bandera = True
        respaginas = ""
        while bandera:
            muchaspaginas = input("Que tantas paginas le importa que su libro tenga?\n1. 0 - 250 pags\n2. 251 - 500 pags\n3. 500 en adelante\n").lower().strip()
            if muchaspaginas == "1" or muchaspaginas == "2" or muchaspaginas == "3":
                bandera = False
                resppaginas = "0-250" if (muchaspaginas == "1") else "251-500" if (muchaspaginas == "2") else "500+"
            else:
                print(mal)
        bandera = True
        costo = 0
        while bandera:
            try:
                costo = int(input("Que tan costoso puede que ser su libro\n1. Barato\n2. Medio\n3. Caro\n"))
                if costo < 1 or costo > 3:
                    raise Exception()
                bandera = False
                costo2 = "Gratis pdf" if costo == 1 else "Q 0-150" if costo == 2 else "Q 150-300"
            except:
                print(mal)
        hacerrecomendacion(respaginas, costo2)
    if op==3:
        print("Majito aqui falta")






main()




