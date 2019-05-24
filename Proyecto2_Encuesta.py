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
Autores = db.labels.create("Autores")
Costos = db.labels.create("Costos")
Generos = db.labels.create("Generos")
No_Pags = db.labels.create("Numero de paginas")
Titulos = db.labels.create("Titulos")
Usuarios = db.labels.create("Usuarios")

#Autores
jonh_Green = db.nodes.create(name="Jonh Green")
suzann_Collings = db.nodes.create(name="Suzann Collings")
xavier_Aldekoa = db.nodes.create(name="Xavier Aldekoa")
agatha_Christie = db.nodes.create(name="Agatha Christie")
suzanne_Collins = db.nodes.create(name="Suzanne Collins")
washington_Irving = db.nodes.create(name="Washington Irving")
desconocido = db.nodes.create(name="Desconocido")
masaaki_Nakayama = db.nodes.create(name="Masaaki Nakayama")
roman_Alvarez = db.nodes.create(name="Roman Alvarez")
carlota_Josefina_Berard = db.nodes.create(name="Carlota Josefina Berard")
grace_Klimt_y_Salvawitts = db.nodes.create(name="Grace Klimt y Salvawitts")
aitana_Monzon = db.nodes.create(name="Aitana Monzon")
alberto_Del_Campo_Tejedor = db.nodes.create(name="Alberto del Campo Tejedor")
bjorn_Blanca_Van_Goch = db.nodes.create(name="Björn Blanca van Goch")
luis_Alemañ = db.nodes.create(name="Luis Alemañ")
salva_Alemany = db.nodes.create(name="Salva Alemany")
juan_Jose_Fernandez_Morales = db.nodes.create(name="Juan Jose Fernandez")
luis_Amezaga = db.nodes.create(name="Luis Amezaga")
julio_Fraile = db.nodes.create(name="Julio Fraile")
jk_Rowllin = db.nodes.create(name="J.K Rowllin")
isaac_Asimov = db.nodes.create(name="Isaac Asimov")
francisco_Alamar = db.nodes.create(name="Francisco Alamar")

Autores.add(jonh_Green, suzann_Collings, xavier_Aldekoa, agatha_Christie, suzanne_Collins, washington_Irving, desconocido, masaaki_Nakayama, roman_Alvarez, carlota_Josefina_Berard, grace_Klimt_y_Salvawitts, aitana_Monzon, alberto_Del_Campo_Tejedor, bjorn_Blanca_Van_Goch, luis_Alemañ, salva_Alemany, juan_Jose_Fernandez_Morales, luis_Amezaga, julio_Fraile, jk_Rowllin, isaac_Asimov, francisco_Alamar)

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
costo_Bajo = db.nodes.create(name="Bajo Costo")
costo_Medio = db.nodes.create(name="Costo Medio")
costo_Alto = db.nodes.create(name="Costo Alto")
pags_0_a_250 = db.nodes.create(name="De 0 a 250 paginas")
pags_en_adelante = db.nodes.create(name="De 251 paginas en adelante")

Costos.add(costo_Bajo, costo_Medio, costo_Alto, pags_0_a_250, pags_en_adelante)

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

Titulos.add(bajo_la_misma_estrella, sinsajo, viaje_al_Corazon_del_Hambre, los_Juegos_del_Hambre, el_Asesinato_de_Roger, la_Leyenda_de_Sleepy, un_Cadaver_en_la_Biblioteca, fuan_no_Tane_Plus, churras_y_Merinas, blanco, la_mente_Dibujada, dormir_a_la_belle, burla, cuando_el_oro_aprieta, animales_Heridos, eire, al_Tantear_la_Costa, vuelos_Rasantes, objective_AHIAH, harry_Potter_y_la_Piedra, yo_Robot, buscando_a_Alaska, en_Llamas, la_Sociedad_Inmortal)

##Usuarios
Javier_Salazar = db.nodes.create(name="Javier Salazar")
Andre_Rodriguez = db.nodes.create(name ="André Rodriguez")
Maria_Jose_Lemus = db.nodes.create(name ="María José Lemus")
Eynar_Rodriguez = db.nodes.create(name ="Eynar Rodríguez")
Damian_Rodriguez = db.nodes.create(name ="Damian Rodriguez")
Sabrina_Monroy = db.nodes.create(name ="Sabrina Monroy")
Lilian_Lissethe_Lemus = db.nodes.create(name="Lilian Lissethe Lemus")
Mirka_Monzon = db.nodes.create(name="Mirka Monzón")
Renato_Estrada = db.nodes.create(name="Renato Estrada")
Francisco_Salazar = db.nodes.create(name="Francisco Salazar")

Usuarios.add(Javier_Salazar, Andre_Rodriguez, Maria_Jose_Lemus, Eynar_Rodriguez, Damian_Rodriguez, Sabrina_Monroy, Lilian_Lissethe_Lemus, Mirka_Monzon, Renato_Estrada, Francisco_Salazar)

#Relaciones entre libros y autores
bajo_la_misma_estrella.relationships.create("El autor@ es:", jonh_Green)
sinsajo.relationships.create("El autor@ es:", suzann_Collings)
viaje_al_Corazon_del_Hambre.relationships.create("El autor@ es: ", xavier_Aldekoa)
los_Juegos_del_Hambre.relationships.create("El autor@ es: ", suzanne_Collins)
el_Asesinato_de_Roger.relationships.create("El autor@ es: ", agatha_Christie)
la_Leyenda_de_Sleepy.relationships.create("El autor@ es: ", washington_Irving)
un_Cadaver_en_la_Biblioteca.relationships.create("El autor@ es: ", desconocido)
fuan_no_Tane_Plus.relationships.create("El autor@ es: ", masaaki_Nakayama)
churras_y_Merinas.relationships.create("El autor@ es: ", roman_Alvarez)
blanco.relationships.create("El autor@ es: ", carlota_Josefina_Berard)
la_mente_Dibujada.relationships.create("El autor@ es: ", grace_Klimt_y_Salvawitts)
dormir_a_la_belle.relationships.create("El autor@ es: ", aitana_Monzon)
burla.relationships.create("El autor@ es: ", alberto_Del_Campo_Tejedor)
cuando_el_oro_aprieta.relationships.create("El autor@ es: ", bjorn_Blanca_Van_Goch)
animales_Heridos.relationships.create("El autor@ es: ", luis_Alemañ)
eire.relationships.create("El autor@ es: ", salva_Alemany)
al_Tantear_la_Costa.relationships.create("El autor@ es: ", juan_Jose_Fernandez_Morales)
vuelos_Rasantes.relationships.create("El autor@ es: ", luis_Amezaga)
objective_AHIAH.relationships.create("El autor@ es: ", julio_Fraile)
harry_Potter_y_la_Piedra.relationships.create("El autor@ es: ", jk_Rowllin)
yo_Robot.relationships.create("El autor@ es: ", isaac_Asimov)
buscando_a_Alaska.relationships.create("El autor@ es: ", jonh_Green)
en_Llamas.relationships.create("El autor@ es: ", suzanne_Collins)
la_Sociedad_Inmortal.relationships.create("El autor@ es: ", francisco_Alamar)

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

