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

#Aqui se ingresan los nodos y las etiquetas del grafo
##Categorias de la base de datos

#Autores
jonh_Green = db.labels.create("Jonh Green")
suzann_Collings = db.labels.create("Suzann Collings")
xavier_Aldekoa = db.labels.create("Xavier Aldekoa")
agatha_Christie = db.labels.create("Agatha Christie")
suzanne_Collins = db.labels.create("Suzanne Collins")
washington_Irving = db.labels.create("Washington Irving")
desconocido = db.labels.create(" ")
masaaki_Nakayama = db.labels.create("Masaaki Nakayama")
roman_Alvarez = db.labels.create("Roman Alvarez")
carlota_Josefina_Berard = db.labels.create("Carlota Josefina Berard")
grace_Klimt_y_Salvawitts = db.labels.create("Grace Klimt y Salvawitts")
aitana_Monzon = db.labels.create("Aitana Monzon")
alberto_Del_Campo_Tejedor = db.labels.create("Alberto del Campo Tejedor")
bjorn_Blanca_Van_Goch = db.labels.create("Björn Blanca van Goch")
luis_Alemañ = db.labels.create("Luis Alemañ")
salva_Alemany = db.labels.create("Salva Alemany")
juan_Jose_Fernandez_Morales = db.labels.create("Juan Jose Fernandez")
luis_Amezaga = db.labels.create("Luis Amezaga")
julio_Fraile = db.labels.create("Julio Fraile")
jk_Rowllin = db.labels.create("J.K Rowllin")
isaac_Asimov = db.labels.create("Isaac Asimov")
francisco_Alamar = db.labels.create("Francisco Alamar")

#Generos
novela_Negra = db.labels.create("Novela Negra")
dramatico = db.labels.create("Dramatico")
terror = db.labels.create("Terror")
prosa = db.labels.create("Prosa")
ensayo = db.labels.create("Ensayo")
narrativa = db.labels.create("Narrativa")
novela = db.labels.create("Novela")
ciencia_Ficcion = db.labels.create("Ciencia Ficcion")
periodistico = db.labels.create("Periodistico")
sagas = db.labels.create("Sagas")
aventura = db.labels.create("Aventura")

#Costos y numero de paginas
costo_Bajo = db.labels.create("Bajo Costo")
costo_Medio = db.labels.create("Costo Medio")
costo_Alto = db.labels.create("Costo Alto")
pags_0_a_250 = db.labels.create("De 0 a 250 paginas")
pags_en_adelante = db.labels.create("De 251 paginas en adelante")
usuario = db.labels.create("Usuario")

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
animales_heridos = db.nodes.create(name="Animales Heridos")

##Usuarios
Javier_Salazar = db.nodes.create(name="Javier Salazar")
Andre_Rodriguez = db.nodes.create(name ="André Rodriguez")
Maria_Jose_Lemus = db.nodes.create(name ="María José Lemus")
usuario.add(Javier_Salazar, Andre_Rodriguez, Maria_Jose_Lemus)

#Print para corroborar que todo funciona 
print("Si conecto a la base de datos")

