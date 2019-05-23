from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from numpy import *


#Conexión a la base de datos, usando el puerto, el usuario y la contraseña de la base de datos
#db = GraphDatabase("http://localhost:7474", username="neo4j", password="1234")

def main():
    print("Bienvenido BookRec\nProcederemos a Realizarle una serie de preguntas con las cuales podemos determinar los libros mas "
          "de ahuevo para usted.\nAntes de inciar la encuesta tomaremos unos datos de usted. Los datos no seran compartidos a"
          " terceros.")
    numero = input("¿Cuál es tu nombre? ")
    edad = input("¿Qué edad tiene actualmente? ")
    genero = input("¿Con qué genero se identifica? ")
    niveleducativo= input("¿Cual es su nivel educativo?\na. Bachillerato\nb. Licenciatura\nc. Posgrado")

main()