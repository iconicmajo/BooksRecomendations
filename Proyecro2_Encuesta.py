#Autores:María José Lemus 181202, André Rodriguez 18332, Javier Salazar 18764
#Proyecto 2 Estructuras de Datos
#Fecha: 24/05/2019
#Descripción: Sistema de recomendaciones de libros, ya sea por autor, numero de paginas, costo del libro, genero del libro

#Se importa el grafo desde neo4j
#Nota: Se necesita instalar neo4jrestclient para que se conecte a la base de datos
from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from numpy import *

#Conexión a la base de datos, usando el puerto, el usuario y la contraseña de la base de datos
db = GraphDatabase("http://localhost:7474", username="neo4j", password="1234")

#Aqui se ingresan los nodos y las etiquetas del grafo

##Categorias de la base de datos
literatura = db.labels.create("Literatura Universal")
Costos = db.labels.create("Costos")
Generos = db.labels.create("Generos")
No_Pags = db.labels.create("Numero de paginas")
Titulos = db.labels.create("Titulos")
Usuarios = db.labels.create("Usuarios")

#Generos
novela_Negra = db.nodes.create(name="Novela Negra")
dramatico = db.nodes.create(name="Dramatico")
terror = db.nodes.create(name="Terror")
prosa = db.nodes.create(name="Prosa")
ensayo = db.nodes.create(name="Ensayo")
narrativa = db.nodes.create(name="Narrativa")
novela = db.nodes.create(name="Novela")
ciencia_Ficcion = db.nodes.create(name="Ciencia Ficcion")
periodistico = db.nodes.create(name="Periodistico")
sagas = db.nodes.create(name="Sagas")
aventura = db.nodes.create(name="Aventura")
poesia = db.nodes.create(name="Poesia")

Generos.add(novela_Negra, dramatico, terror, prosa, ensayo, narrativa, novela, ciencia_Ficcion, periodistico, sagas, aventura, poesia)

#Costos y numero de paginas
costo_Bajo = db.nodes.create(name="Gratis PDF")
costo_Medio = db.nodes.create(name="0-150")
costo_Alto = db.nodes.create(name="150-300")
pags_0_a_250 = db.nodes.create(name="0 a 250")
pags_251_500 = db.nodes.create(name=" 251 - 500")
pags_500_mas = db.nodes.create(name=" 251 - 500")

Costos.add(costo_Bajo, costo_Medio, costo_Alto, pags_0_a_250, pags_500_mas,pags_251_500)

##Titulos de libros
bajo_la_misma_estrella = db.nodes.create(name="Bajo la Misma Estrella")
sinsajo = db.nodes.create(name="Sinsajo")
viaje_al_Corazon_del_Hambre = db.nodes.create(name="Viaje al Corazon del Hambre")
los_Juegos_del_Hambre = db.nodes.create(name="Los Juegos del Hambre")
el_Asesinato_de_Roger = db.nodes.create(name="El Asesinato de Roger Ackroyd")
la_Leyenda_de_Sleepy = db.nodes.create(name="La Leyenda de Sleepy")
un_Cadaver_en_la_Biblioteca = db.nodes.create(name="Un Cadaver en la Biblioteca")
fuan_no_Tane_Plus = db.nodes.create(name="Fuan no Tane Plus")
churras_y_Merinas = db.nodes.create(name="Churras y Merinas")
blanco = db.nodes.create(name="Blanco")
la_mente_Dibujada = db.nodes.create(name="La Mente Dibujada")
dormir_a_la_belle = db.nodes.create(name="Dormir a la Belle")
burla = db.nodes.create(name="Burla burlando.Las diversiones de los universitarios en el siglo XVI")
cuando_el_oro_aprieta = db.nodes.create(name="Cuando el Oro Aprieta")
animales_Heridos = db.nodes.create(name="Animales Heridos")
eire = db.nodes.create(name="Éire")
al_Tantear_la_Costa = db.nodes.create(name="Al tantear la costa")
vuelos_Rasantes = db.nodes.create(name="Vuelos rasantes")
objective_AHIAH = db.nodes.create(name="Objetive: AHIAH Summit - Objetivo: Cumbre AHIAH (Edición Bilingüe")
harry_Potter_y_la_Piedra = db.nodes.create(name="Harry Potter y la Piedra Filosofal")
yo_Robot = db.nodes.create(name="Yo Robot")
buscando_a_Alaska = db.nodes.create(name="Buscando a Alaska")
en_Llamas = db.nodes.create(name="En Llamas")
la_Sociedad_Inmortal = db.nodes.create(name="La Sociedad Inmortal (Hacia la Metamorfosis Humana)")
#*******************************************************************************************************************
el_asesinato_de_roger= db.nodes.create(name="El Asesinato de Roger Ackroyd", autor="Agatha Christie", genero="Novela Negra")
#///********************************************************************************************************************

Titulos.add(bajo_la_misma_estrella, sinsajo, viaje_al_Corazon_del_Hambre, los_Juegos_del_Hambre, el_Asesinato_de_Roger, la_Leyenda_de_Sleepy, un_Cadaver_en_la_Biblioteca, fuan_no_Tane_Plus, churras_y_Merinas, blanco, la_mente_Dibujada, dormir_a_la_belle, burla, cuando_el_oro_aprieta, animales_Heridos, eire, al_Tantear_la_Costa, vuelos_Rasantes, objective_AHIAH, harry_Potter_y_la_Piedra, yo_Robot, buscando_a_Alaska, en_Llamas, la_Sociedad_Inmortal)

##Usuarios
Javier_Salazar = db.nodes.create(name="Javier Salazar")
Andre_Rodriguez = db.nodes.create(name ="André Rodriguez")
Maria_Jose_Lemus = db.nodes.create(name ="María José Lemus")


Usuarios.add(Javier_Salazar, Andre_Rodriguez, Maria_Jose_Lemus)

#costo_Bajo = db.nodes.create(name="Gratis PDF")
#costo_Medio = db.nodes.create(name="0-150")
#costo_Alto = db.nodes.create(name="150-300")

#Relaciones entre libros y costo
bajo_la_misma_estrella.relationships.create("Cuesta", )
sinsajo.relationships.create()
viaje_al_Corazon_del_Hambre.relationships.create()
los_Juegos_del_Hambre.relationships.create()
el_Asesinato_de_Roger.relationships.create()
la_Leyenda_de_Sleepy.relationships.create()
un_Cadaver_en_la_Biblioteca.relationships.create()
fuan_no_Tane_Plus.relationships.create()
churras_y_Merinas.relationships.create()
blanco.relationships.create()
la_mente_Dibujada.relationships.create()
dormir_a_la_belle.relationships.create()
burla.relationships.create()
cuando_el_oro_aprieta.relationships.create()
animales_Heridos.relationships.create()
eire.relationships.create()
al_Tantear_la_Costa.relationships.create()
vuelos_Rasantes.relationships.create()
objective_AHIAH.relationships.create()
harry_Potter_y_la_Piedra.relationships.create()
yo_Robot.relationships.create()
buscando_a_Alaska.relationships.create()
en_Llamas.relationships.create()
la_Sociedad_Inmortal.relationships.create()

#Relaciones entre libros y generos
bajo_la_misma_estrella.relationships.create("Pertenece a: ", dramatico)
sinsajo.relationships.create("Pertenece a: ", ciencia_Ficcion)
viaje_al_Corazon_del_Hambre.relationships.create("Pertenece a: ", periodistico)
los_Juegos_del_Hambre.relationships.create("Pertenece a: ", ciencia_Ficcion)
el_Asesinato_de_Roger.relationships.create("Pertenece a: ", novela_Negra)
la_Leyenda_de_Sleepy.relationships.create("Pertenece a: ", terror)
un_Cadaver_en_la_Biblioteca.relationships.create("Pertenece a: ", novela_Negra)
fuan_no_Tane_Plus.relationships.create("Pertenece a: ", terror)
churras_y_Merinas.relationships.create("Pertenece a: ", periodistico)
blanco.relationships.create("Pertenece a: ", poesia )
la_mente_Dibujada.relationships.create("Pertenece a: ", poesia)
dormir_a_la_belle.relationships.create("Pertenece a: ", poesia)
burla.relationships.create("Pertenece a: ", ensayo)
cuando_el_oro_aprieta.relationships.create("Pertenece a: ", narrativa)
animales_Heridos.relationships.create("Pertenece a: ", poesia)
eire.relationships.create("El autor@ es: ", novela_Negra)
al_Tantear_la_Costa.relationships.create("Pertenece a: ", novela_Negra)
vuelos_Rasantes.relationships.create("Pertenece a: ", narrativa)
objective_AHIAH.relationships.create("Pertenece a: ", ensayo)
harry_Potter_y_la_Piedra.relationships.create("Pertenece a: ", ciencia_Ficcion)
yo_Robot.relationships.create("El autor@ es: ", ciencia_Ficcion)
buscando_a_Alaska.relationships.create("Pertenece a: ", novela)
en_Llamas.relationships.create("Pertenece a: ", ciencia_Ficcion)
la_Sociedad_Inmortal.relationships.create("Pertenece a: ", ensayo)

#Print para corroborar que todo funciona 
print("Si conecto a la base de datos")

#*************IGNORAR ESTO******************
#def recomendacion(usuario,genero, costo, paginas):
 #   libros ={}
  #  q = 'MATCH (n: Libros) RETURN n'
   # resultados = db.query(q, returns=(client.Node))
    #for i in results:
     #   libros[i[0]["name"]]=0
    #q='MATCH (n:Usuario)-[r:a]->(m:Usuario) WHERE U.name="'+nombre+'"RETURN n, type(r),m'
    
