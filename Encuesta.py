from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from numpy import *


#Conexión a la base de datos, usando el puerto, el usuario y la contraseña de la base de datos
#db = GraphDatabase("http://localhost:7474", username="neo4j", password="1234")

def main():
    mal = "Ingrese un valor correcto"
    print("Bienvenido BookRec\nProcederemos a Realizarle una serie de preguntas con las cuales podemos determinar los libros mas "
          "de ahuevo para usted.\nAntes de inciar la encuesta tomaremos unos datos de usted. Los datos no seran compartidos a"
          " terceros.")
    banderaedad = False
    nombre = genero = niveleducativo = ""
    edad = 0
    while (nombre.strip()==""):
        nombre = input("¿Cuál es tu nombre? ").strip()
        if(nombre == ""):
            print(mal)
    while (banderaedad):
        try:
            edad = int(input("¿Qué edad tiene actualmente? "))
            banderaedad=False
        except:
            print(mal)
    while (genero.strip()==""):
        genero = input("¿Con qué genero se identifica? ").strip()
        if(genero == ""):
            print(mal)
    while (niveleducativo.strip() == "" or (niveleducativo !="a" and niveleducativo!="b" and niveleducativo!="c")):
        niveleducativo= input("¿Cual es su nivel educativo?\na. Bachillerato\nb. Licenciatura\nc. Posgrado").lower()
        if(niveleducativo =="" or (niveleducativo !="a" and niveleducativo!="b" and niveleducativo!="c")):
            print(mal)
main()