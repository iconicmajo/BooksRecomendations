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
db = GraphDatabase("http://localhost:7474", username="neo4j", password="1234")

generos = ["Novela Negra", "Dramatico", "Terror", "Prosa", "Ensayo", "Narrativa", "Novela",
           "Ciencia Ficcion", "Periodistico", "Sagas", "Aventura", "Poesia"]
def hacerrecomendacin(respaginas, costo):
    print("hola si entro")
    libros = {}
    for i in generos:
        mquery = 'MATCH (g:Generos)-[r:a]->(t:Titulos) WHERE g.name="'+i+'"RETURN g, type(r), t'
        res1 = db.query(mquery, returns=(client.Node, str, client.Node))
        print("-"+"%s"%(i[0]["name"]))
        #libros[i[0][i]]=0
        print("hola si entrox2")
        for j in res1:
            mquery = 'MATCH (g:No_Pags)-[r:a]->(t:Titulos) WHERE t.name="'+j[2]["name"]+'"RETURN g, type(r), t'
            res2 = db.query(mquery, returns=(client.Node, str, client.Node))
            print("hola si entrox3")
            for k in res2:
                mquery2 = 'MATCH (g:Costo)-[r:a]->(t:Titulos) WHERE g.name="'+j[2]["name"]+'"RETURN g, type(r), t'
                res3 = db.query(mquery2, returns=(client.Node, str, client.Node))
                print("hola si entrox4")
                for l in  res3:
                    if k[0]["name"] == respaginas and l[0]["name"] == costo:
                        libros[l[2]["name"]]= libros[l[2]["name"]]+5
    for key, value in libros:
        print("- %s" %key)
        print("hola si entrox5")




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
    print("3. Eliminar")
    print("4. Salir")
    while op != 4:
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
            print("3. Eliminar")
            print("4. Salir")
            
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
                muchaspaginas = input("Que tantas paginas le importa que su libro tenga?\n1. 0 - 250 pags\n2. 251 -en adelante pags").lower().strip()
                if muchaspaginas == "1" or muchaspaginas == "2" or muchaspaginas == "3":
                    bandera = False
                    #opciones de respuestas
                    resppaginas = "De 0 a 250 paginas" if (muchaspaginas == "1") else "De 251 en adelante" if (muchaspaginas == "2") else "500+"
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
                    costo2 = "Gratis pdf" if costo == 1 else "0-150" if costo == 2 else "150-300"
                except:
                    print(mal)
            #Hace una llamada a la función en Proyecto2_Encuesta
            #En este determina la recomendacion
            #hacerrecomendacion(respaginas, costo2)
            hacerrecomendacion(respaginas, costo2)
            #buscar()
        if op==3:
            #Elimina un usuario ingresado 
            print("************************************")
            print("         Eliminar Usuarios" )
            print("************************************")
            nombre = input("ingrese su nombre: ")
            #Aqui se conecta con la db para poder eliminar
            #Encontrar el nombre de usuario
            #user = db.nodes.create(name=nombre,age=edad,gen=genero,ed= eduacion)
            #Eliminar
            #Usuarios.add(user)
            print("**********************************")
            print("     Bienvenido a de Bookstore")
            print("**********************************")
            print("1. Nuevo usuario")
            print("2. Ver Recomendaciones")
            print("3. Eliminar")
            print("4. Salir")
            
    else:
        print("Gracias por su prefencia. Disfrute su lectura")
        
main()
