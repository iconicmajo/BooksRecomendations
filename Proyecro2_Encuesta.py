#Autores:María José Lemus 181202, André Rodriguez, Javier Salazar 18764
#Proyecto 2 Estructuras de Datos
#Fecha: 24/05/2019
#Descripción: Sistema de recomendaciones de libros, ya sea por autor, numero de paginas, costo del libro, genero="" del libro
#El algoritmo de recomendacion fue tomado y editado de: https://github.com/andresum97/Proyecto2
#a conveniencia del programa

#Se importa el grafo desde neo4j
#Nota: Se necesita instalar neo4jrestclient para que se conecte a la base de datos
from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client

#Conexión a la base de datos, usando el puerto, el usuario y la contraseña de la base de datos
db = GraphDatabase("http://localhost:7474", username="neo4j", password="1234")

#Aqui se ingresan los nodos y las etiquetas del grafo
##Categorias de la base de datos
Generos = db.labels.create("Generos")
Titulos = db.labels.create("Titulos")
Usuarios = db.labels.create("Usuarios")
Encuesta_Pregunta = db.labels.create("Preguntas")
genders_Result = db.labels.create("Resultados")
Costos = db.labels.create("Costos")
No_Pags= db.labels.create("Paginas")
Universal= db.labels.create("Literatura")

#Nodo Universal
nodo_Universal = db.nodes.create(name="Literatura Universal")
Universal.add(nodo_Universal)


#genero=""s
#Manualmente se crean los nodos de los genero=""s de los libros
novela_Negra = db.nodes.create(name="Novela Negra")
romance = db.nodes.create(name="Romance")
filosofia= db.nodes.create(name="Filosofia")
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

#Los genero=""s se agregan a la base de datos
Generos.add(novela_Negra, dramatico, terror, prosa, ensayo, narrativa, novela, ciencia_Ficcion, periodistico, sagas, aventura, poesia, romance, filosofia)

#Costos y numero de paginas
#Manualmente se crean los nodos de los tipos de costos y numero de paginas
pags_0_a_250 = db.nodes.create(name="De 0 a 250 paginas")
pags_en_adelante = db.nodes.create(name="De 251 paginas en adelante")
costo_Bajo = db.nodes.create(name="Gratis PDF")
costo_Medio = db.nodes.create(name="0-150")
costo_Mayor = db.nodes.create(name="150-300")

#Se agregan los nodos a la base de datos
Costos.add(costo_Bajo, costo_Medio, costo_Mayor)
No_Pags.add(pags_0_a_250, pags_en_adelante)

##Titulos de libros
viaje_al_Centro_de_la_Tierra = db.nodes.create(titulo="Viaje al Centro de la Tierra", autor="Julio Verne", genero="Ciencia Ficcion")
la_Vuelta_al_Mundo_en_80_dias = db.nodes.create(titulo = "La Vuelta al Mundo en 80 Dias", autor="Julio Verne", genero="Ciencia Ficcion")
la_Isla_Misteriosa = db.nodes.create(titulo="La Isla Misteriosa", autor="Julio Verne", genero="Ciencia Ficcion")
la_Esfinge_de_los_Hielos = db.nodes.create(titulo="La Esfinge de los Hielos", autor="Julio Verne", genero="Ciencia Ficcion")
la_Casa_de_Vapor = db.nodes.create(titulo="La Casa de Vapor", autor="Julio Verne", genero="Ciencia Ficcion")
en_Busca_del_Tiempo_Perdido = db.nodes.create(titulo="En Busca del Tiempo Perdido", autor="Julio Verne", genero="Ciencia Ficcion")
viaje_al_fin_de_la_noche = db.nodes.create(titulo="Viaje al Fin de la Noche", autor="Louis Fernandin Celine", genero="Ciencia Ficcion")
diario_de_Anne_Frank = db.nodes.create(titulo="Diario de Anne Frank", autor="Anne Frank", genero="Novela")
ulises = db.nodes.create(titulo="Ulises", autor="James Joyce", genero="Ciencia Ficcion")
la_Metamorfosis = db.nodes.create(titulo="La Metamorfosis", autor="Kafka", genero="Ciencia Ficcion")
cien_Años_de_Soledad = db.nodes.create(titulo="Cien Años de Soledad", autor="Gabriel Garcia Marquez", genero="Novela, Ficcion")
lo_que_el_viento_se_llevo = db.nodes.create(titulo="Lo que el Viento se Llevo", autor="Margaret Mitchell", genero="Novela")
la_Montaña_Magica = db.nodes.create(titulo="La Montaña Magica", autor="Thomas Mann", genero="Ciencia Ficcion")
el_Silencio_del_Mar = db.nodes.create(titulo="El Silencio del Mar", autor="Jean Bruller", genero="Dramatico")
la_Vida_Instrucciones_de_Uso = db.nodes.create(titulo="La Vida Instrucciones de Uso", autor="Georger Perec", genero="Ciencia Ficcion")
el_Sabueso_de_los_Bakerville = db.nodes.create(titulo="El Sabueso de los Bakerville", autor="Arthur Conan Doyle", genero="Ciencia Ficcion")
seis_Personajes_en_Busca_de_Autor = db.nodes.create(titulo="Seis Personajes en Busca de Autor", autor="Lougi Pirandellor", genero="Filosofia")
orgullo_y_Prejuicio = db.nodes.create(titulo="Orgullo y Prejuicio", autor="Jane Austen", genero="Romance")
la_Guerra_de_los_Mundos = db.nodes.create(titulo="La Guerra de los Mundos", autor="H.G. Wells", genero="Ciencia Ficcion")
el_Señor_de_los_Anillos = db.nodes.create(titulo="El Señor de los Anillos", autor="J.R.R Tolkien", genero="Ciencia Ficcion")
bajo_la_misma_estrella = db.nodes.create(titulo="Bajo la Misma Estrella", autor="Jonh Green", genero="Dramatico")
sinsajo = db.nodes.create(titulo="Sinsajo", autor="Suzann Collings", genero="Ciencia Ficcion")
viaje_al_Corazon_del_Hambre = db.nodes.create(titulo="Viaje al Corazon del Hambre", autor="", genero="Periodistico")
los_Juegos_del_Hambre = db.nodes.create(titulo="Los Juegos del Hambre", autor="", genero="Ciencia Ficcion")
el_Asesinato_de_Roger = db.nodes.create(titulo="El Asesinato de Roger Ackroyd", autor="", genero="Novela Negra")
la_Leyenda_de_Sleepy = db.nodes.create(titulo="La Leyenda de Sleepy", autor="", genero="Terror")
un_Cadaver_en_la_Biblioteca = db.nodes.create(titulo="Un Cadaver en la Biblioteca", autor="", genero="Novela Negra")
fuan_no_Tane_Plus = db.nodes.create(titulo="Fuan no Tane Plus", autor="", genero="Terror")
churras_y_Merinas = db.nodes.create(titulo="Churras y Merinas", autor="", genero="Periodistico")
blanco = db.nodes.create(titulo="Blanco", autor="", genero="Poesia")
la_mente_Dibujada = db.nodes.create(titulo="La Mente Dibujada", autor="", genero="Poesia")
dormir_a_la_belle = db.nodes.create(titulo="Dormir a la Belle", autor="", genero="Poesia")
burla = db.nodes.create(titulo="Burla burlando.Las diversiones de los universitarios en el siglo XVI", autor="", genero="Ensayo")
cuando_el_oro_aprieta = db.nodes.create(titulo="Cuando el Oro Aprieta", autor="", genero="Narrativa")
animales_Heridos = db.nodes.create(titulo="Animales Heridos", autor="", genero="Poesia")
eire = db.nodes.create(titulo="Éire", autor="", genero="Novela Negra")
al_Tantear_la_Costa = db.nodes.create(titulo="Al tantear la costa", autor="", genero="Novela Negra")
vuelos_Rasantes = db.nodes.create(titulo="Vuelos rasantes", autor="", genero="Narrativa")
objective_AHIAH = db.nodes.create(titulo="Objetive: AHIAH Summit - Objetivo: Cumbre AHIAH (Edición Bilingüe", autor="", genero="Ensayo")
harry_Potter_y_la_Piedra = db.nodes.create(titulo="Harry Potter y la Piedra Filosofal", autor="", genero="Ciencia Ficcion")
yo_Robot = db.nodes.create(titulo="Yo Robot", autor="", genero="Ciencia Ficcion")
buscando_a_Alaska = db.nodes.create(titulo="Buscando a Alaska", autor="", genero="Novela")
en_Llamas = db.nodes.create(titulo="En Llamas", autor="", genero="Ciencia Ficcion")
la_Sociedad_Inmortal = db.nodes.create(titulo="La Sociedad Inmortal (Hacia la Metamorfosis Humana)", autor="", genero="Ensayo")
Titulos.add(viaje_al_Centro_de_la_Tierra,la_Vuelta_al_Mundo_en_80_dias,la_Isla_Misteriosa,la_Esfinge_de_los_Hielos,la_Casa_de_Vapor,en_Busca_del_Tiempo_Perdido,viaje_al_fin_de_la_noche ,diario_de_Anne_Frank,ulises,la_Metamorfosis,cien_Años_de_Soledad,lo_que_el_viento_se_llevo, la_Montaña_Magica,el_Silencio_del_Mar,la_Vida_Instrucciones_de_Uso,el_Sabueso_de_los_Bakerville,seis_Personajes_en_Busca_de_Autor,orgullo_y_Prejuicio,la_Guerra_de_los_Mundos,el_Señor_de_los_Anillos, bajo_la_misma_estrella, sinsajo, viaje_al_Corazon_del_Hambre, los_Juegos_del_Hambre, el_Asesinato_de_Roger, la_Leyenda_de_Sleepy, un_Cadaver_en_la_Biblioteca, fuan_no_Tane_Plus, churras_y_Merinas, blanco, la_mente_Dibujada, dormir_a_la_belle, burla, cuando_el_oro_aprieta, animales_Heridos, eire, al_Tantear_la_Costa, vuelos_Rasantes, objective_AHIAH, harry_Potter_y_la_Piedra, yo_Robot, buscando_a_Alaska, en_Llamas, la_Sociedad_Inmortal)

#Relaciones de los generos con el genero libro literario universal
romance.relationships.create("Es perteneciente a la ", nodo_Universal)
filosofia.relationships.create("Es perteneciente a la ", nodo_Universal)
novela_Negra.relationships.create("Es perteneciente a la ", nodo_Universal)
dramatico.relationships.create("Es perteneciente a la ", nodo_Universal)
terror.relationships.create("Es perteneciente a la ", nodo_Universal)
prosa.relationships.create("Es perteneciente a la ", nodo_Universal)
ensayo.relationships.create("Es perteneciente a la ", nodo_Universal)
narrativa.relationships.create("Es perteneciente a la ", nodo_Universal)
novela.relationships.create("Es perteneciente a la ", nodo_Universal)
ciencia_Ficcion.relationships.create("Es perteneciente a la ", nodo_Universal)
periodistico.relationships.create("Es perteneciente a la ", nodo_Universal)
sagas.relationships.create("Es perteneciente a la ", nodo_Universal)
aventura.relationships.create("Es perteneciente a la ", nodo_Universal)
poesia.relationships.create("Es perteneciente a la ", nodo_Universal)

#Relaciones de libros con numero de paginas
viaje_al_Centro_de_la_Tierra.relationships.create("La cantidad de paginas es: ", pags_en_adelante)
la_Vuelta_al_Mundo_en_80_dias.relationships.create("La cantidad de paginas es: ", pags_0_a_250)
la_Isla_Misteriosa.relationships.create("La cantidad de paginas es: ", pags_en_adelante)
la_Esfinge_de_los_Hielos.relationships.create("La cantidad de paginas es: ", pags_0_a_250)
la_Casa_de_Vapor.relationships.create("La cantidad de paginas es: ", pags_en_adelante)
en_Busca_del_Tiempo_Perdido.relationships.create("La cantidad de paginas es: ", pags_0_a_250)
viaje_al_fin_de_la_noche.relationships.create("La cantidad de paginas es: ", pags_en_adelante)
diario_de_Anne_Frank.relationships.create("La cantidad de paginas es: ", pags_0_a_250)
ulises.relationships.create("La cantidad de paginas es: ", pags_en_adelante)
la_Metamorfosis.relationships.create("La cantidad de paginas es: ", pags_0_a_250)
cien_Años_de_Soledad.relationships.create("La cantidad de paginas es: ", pags_0_a_250)
lo_que_el_viento_se_llevo.relationships.create("La cantidad de paginas es: ", pags_en_adelante)
la_Montaña_Magica.relationships.create("La cantidad de paginas es: ", pags_0_a_250)
el_Silencio_del_Mar.relationships.create("La cantidad de paginas es: ", pags_en_adelante)
la_Vida_Instrucciones_de_Uso.relationships.create("La cantidad de paginas es: ", pags_0_a_250)
el_Sabueso_de_los_Bakerville.relationships.create("La cantidad de paginas es: ", pags_0_a_250)
seis_Personajes_en_Busca_de_Autor.relationships.create("La cantidad de paginas es: ", pags_en_adelante)
orgullo_y_Prejuicio.relationships.create("La cantidad de paginas es: ", pags_0_a_250)
la_Guerra_de_los_Mundos.relationships.create("La cantidad de paginas es: ", pags_en_adelante)
el_Señor_de_los_Anillos.relationships.create("La cantidad de paginas es: ", pags_0_a_250)

bajo_la_misma_estrella.relationships.create("La cantidad de paginas es: ", pags_en_adelante)
sinsajo.relationships.create("La cantidad de paginas es: ", pags_0_a_250)
viaje_al_Corazon_del_Hambre.relationships.create("La cantidad de paginas es: ", pags_0_a_250)
los_Juegos_del_Hambre.relationships.create("La cantidad de paginas es: ", pags_en_adelante)
el_Asesinato_de_Roger.relationships.create("La cantidad de paginas es: ", pags_0_a_250)
la_Leyenda_de_Sleepy.relationships.create("La cantidad de paginas es: ", pags_en_adelante)
un_Cadaver_en_la_Biblioteca.relationships.create("La cantidad de paginas es: ", pags_en_adelante)
fuan_no_Tane_Plus.relationships.create("La cantidad de paginas es: ", pags_0_a_250)
churras_y_Merinas.relationships.create("La cantidad de paginas es: ", pags_en_adelante) 
blanco.relationships.create("La cantidad de paginas es: ",pags_0_a_250)
la_mente_Dibujada.relationships.create("La cantidad de paginas es: ", pags_0_a_250)
dormir_a_la_belle.relationships.create("La cantidad de paginas es: ", pags_en_adelante)
burla.relationships.create("La cantidad de paginas es: ", pags_0_a_250)
cuando_el_oro_aprieta.relationships.create("La cantidad de paginas es: ", pags_0_a_250)
animales_Heridos.relationships.create("La cantidad de paginas es: ", pags_en_adelante)
eire.relationships.create("La cantidad de paginas es: ", pags_0_a_250)
al_Tantear_la_Costa.relationships.create("La cantidad de paginas es: ", pags_0_a_250)
vuelos_Rasantes.relationships.create("La cantidad de paginas es: ", pags_0_a_250)
objective_AHIAH.relationships.create("La cantidad de paginas es: ", pags_en_adelante)
harry_Potter_y_la_Piedra.relationships.create("La cantidad de paginas es: ", pags_0_a_250)
yo_Robot.relationships.create("La cantidad de paginas es: ", pags_en_adelante)
buscando_a_Alaska.relationships.create("La cantidad de paginas es: ", pags_0_a_250)
en_Llamas.relationships.create("La cantidad de paginas es: ", pags_0_a_250)
la_Sociedad_Inmortal.relationships.create("La cantidad de paginas es: ", pags_en_adelante)

#Relaciones entre libros y generos
viaje_al_Centro_de_la_Tierra.relationships.create("Pertenece a: ", ciencia_Ficcion)
la_Vuelta_al_Mundo_en_80_dias.relationships.create("Pertenece a: ", ciencia_Ficcion)
la_Isla_Misteriosa.relationships.create("Pertenece a: ", ciencia_Ficcion)
la_Esfinge_de_los_Hielos.relationships.create("Pertenece a: ", ciencia_Ficcion)
la_Casa_de_Vapor.relationships.create("Pertenece a: ", ciencia_Ficcion)
en_Busca_del_Tiempo_Perdido.relationships.create("Pertenece a: ", ciencia_Ficcion)
viaje_al_fin_de_la_noche.relationships.create("Pertenece a: ", ciencia_Ficcion)
diario_de_Anne_Frank.relationships.create("Pertenece a: ", novela)
ulises.relationships.create("Pertenece a: ", ciencia_Ficcion)
la_Metamorfosis.relationships.create("Pertenece a: ", ciencia_Ficcion)
cien_Años_de_Soledad.relationships.create("Pertenece a: ", ciencia_Ficcion)
lo_que_el_viento_se_llevo.relationships.create("Pertenece a: ",novela)
la_Montaña_Magica.relationships.create("Pertenece a: ", ciencia_Ficcion)
el_Silencio_del_Mar.relationships.create("Pertenece a: ", dramatico)
la_Vida_Instrucciones_de_Uso.relationships.create("Pertenece a: ", ciencia_Ficcion)
el_Sabueso_de_los_Bakerville.relationships.create("Pertenece a: ", ciencia_Ficcion)
seis_Personajes_en_Busca_de_Autor.relationships.create("Pertenece a: ", filosofia)
orgullo_y_Prejuicio.relationships.create("Pertenece a: ", romance)
la_Guerra_de_los_Mundos.relationships.create("Pertenece a: ", ciencia_Ficcion)
el_Señor_de_los_Anillos.relationships.create("Pertenece a: ", ciencia_Ficcion)
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

#Relaciones de libros con costos
viaje_al_Centro_de_la_Tierra.relationships.create("El precio del libro es: ", costo_Mayor)
la_Vuelta_al_Mundo_en_80_dias.relationships.create("El precio del libro es: ", costo_Mayor)
la_Isla_Misteriosa.relationships.create("El precio del libro es: ", costo_Medio)
la_Esfinge_de_los_Hielos.relationships.create("El precio del libro es: ", costo_Mayor)
la_Casa_de_Vapor.relationships.create("El precio del libro es: ", costo_Bajo)
en_Busca_del_Tiempo_Perdido.relationships.create("El precio del libro es: ", costo_Medio)
viaje_al_fin_de_la_noche.relationships.create("El precio del libro es: ", costo_Mayor)
diario_de_Anne_Frank.relationships.create("El precio del libro es: ", costo_Medio)
ulises.relationships.create("El precio del libro es: ", costo_Mayor)
la_Metamorfosis.relationships.create("El precio del libro es: ", costo_Medio)
cien_Años_de_Soledad.relationships.create("El precio del libro es: ", costo_Mayor)
lo_que_el_viento_se_llevo.relationships.create("El precio del libro es: ", costo_Bajo)
la_Montaña_Magica.relationships.create("El precio del libro es: ", costo_Mayor)
el_Silencio_del_Mar.relationships.create("El precio del libro es: ", costo_Mayor)
la_Vida_Instrucciones_de_Uso.relationships.create("El precio del libro es: ", costo_Bajo)
el_Sabueso_de_los_Bakerville.relationships.create("El precio del libro es: ", costo_Mayor)
seis_Personajes_en_Busca_de_Autor.relationships.create("El precio del libro es: ", costo_Bajo)
orgullo_y_Prejuicio.relationships.create("El precio del libro es: ", costo_Mayor)
la_Guerra_de_los_Mundos.relationships.create("El precio del libro es: ", costo_Medio)
el_Señor_de_los_Anillos.relationships.create("El precio del libro es: ", costo_Bajo)
bajo_la_misma_estrella.relationships.create("El precio del libro es: ", costo_Mayor)
sinsajo.relationships.create("Pertenece a: ", costo_Mayor)
viaje_al_Corazon_del_Hambre.relationships.create("El precio del libro es: ", costo_Medio)
los_Juegos_del_Hambre.relationships.create("El precio del libro es: ", costo_Mayor)
el_Asesinato_de_Roger.relationships.create("El precio del libro es: ", costo_Mayor)
la_Leyenda_de_Sleepy.relationships.create("El precio del libro es: ", costo_Medio)
un_Cadaver_en_la_Biblioteca.relationships.create("El precio del libro es: ", costo_Mayor)
fuan_no_Tane_Plus.relationships.create("El precio del libro es: ", costo_Bajo)
churras_y_Merinas.relationships.create("El precio del libro es: ", costo_Medio) 
blanco.relationships.create("El precio del libro es: ", costo_Bajo)
la_mente_Dibujada.relationships.create("El precio del libro es: ", costo_Bajo)
dormir_a_la_belle.relationships.create("El precio del libro es: ", costo_Medio)
burla.relationships.create("El precio del libro es: ", costo_Bajo)
cuando_el_oro_aprieta.relationships.create("El precio del libro es: ", costo_Bajo)
animales_Heridos.relationships.create("El precio del libro es: ", costo_Medio)
eire.relationships.create("El precio del libro es: ", costo_Bajo)
al_Tantear_la_Costa.relationships.create("El precio del libro es: ", costo_Medio)
vuelos_Rasantes.relationships.create("El precio del libro es: ", costo_Bajo)
objective_AHIAH.relationships.create("El precio del libro es: ", costo_Mayor)
harry_Potter_y_la_Piedra.relationships.create("El precio del libro es: ", costo_Mayor)
yo_Robot.relationships.create("El precio del libro es: ", costo_Mayor)
buscando_a_Alaska.relationships.create("El precio del libro es: ",costo_Medio )
en_Llamas.relationships.create("El precio del libro es: ", costo_Bajo)
la_Sociedad_Inmortal.relationships.create("El precio del libro es: ", costo_Medio)

##Usuarios
Javier_Salazar = db.nodes.create(name="Javier Salazar", nivel_educativo="Licenciatura", genero="Masculino")
Andre_Rodriguez = db.nodes.create(name ="André Rodriguez", nivel_educativo="Licenciatura", genero="Masculino")
Maria_Jose_Lemus = db.nodes.create(name ="María José Lemus", nivel_educativo="Licenciatura", genero="Femenino")
Eynar_Rodriguez = db.nodes.create(name ="Eynar Rodríguez", nivel_educativo="Licenciatura", genero="Femenino")
Damian_Rodriguez = db.nodes.create(name ="Damian Rodriguez", nivel_educativo="Bachillerato", genero="Masculino")
Sabrina_Monroy = db.nodes.create(name ="Sabrina Monroy", nivel_educativo="Licenciatura", genero="Femenino")
Lilian_Lissethe_Lemus = db.nodes.create(name="Lilian Lissethe Lemus", nivel_educativo="Licenciatura", genero="Femenino")
Mirka_Monzon = db.nodes.create(name="Mirka Monzón", nivel_educativo="Licenciatura", genero="Femenino")
Renato_Estrada = db.nodes.create(name="Renato Estrada", nivel_educativo="Licenciatura", genero="Masculino")
Francisco_Salazar = db.nodes.create(name="Francisco Salazar", nivel_educativo="Licenciatura", genero="Masculino")

Usuarios.add(Javier_Salazar, Andre_Rodriguez, Maria_Jose_Lemus, Eynar_Rodriguez, Damian_Rodriguez, Sabrina_Monroy, Lilian_Lissethe_Lemus, Mirka_Monzon, Renato_Estrada, Francisco_Salazar)

#Print para corroborar que todo funciona 
print("Si conecto a la base de datos")
#*********************************************Desarrollo del algoritmo de recomendacion********************************


#**************POESIA***************
def  hacerrecomendacion(respaginas, costo2):
    #************************Filtración por Genero, Costo y paginas
    x = True 
    while x:  #Para que el usuario pueda elegir un ambiente y si se equivoca vuelve a preguntar
        print("\nLos libros que recomendamos de Poesia: \n")
        #q='MATCH (:Generos { name: "Poesia" })<--(u:Titulos) MATCH (:Costos {name:"'+costo2+'"})--(u:Titulos) MATCH (:Paginas{name:"'+respaginas+'"})--(u:Titulos) RETURN u'
        #q='MATCH (:Generos { name: "Poesia" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) MATCH (:Paginas{name:"De 0 a 250 paginas"})--(u:Titulos) RETURN u'
        #q = 'MATCH (u: Titulos{genero:"Poesia"}) RETURN u'
        #q = 'MATCH (:Generos { name: "Poesia" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) RETURN u'
        results = db.query(q,returns=(client.Node,str,client.Node))
        #Se agregan todos los ambientes
        for i in results:
            print("-"+"%s"%(i[0]["titulo"]))
    x = True
    
#***************Ciencia Ficcion
def  cienciaf(respaginas, costo2):
    #************************Filtración por Genero
    x = True 
    while x:  #Para que el usuario pueda elegir un ambiente y si se equivoca vuelve a preguntar
        print("\nLos libros que recomendamos de Ciencia Ficcion: \n")
        #q='MATCH (:Generos { name: "Ciencia Ficcion" })<--(u:Titulos) MATCH (:Costos {name:"'+costo2+'"})--(u:Titulos) MATCH (:Paginas{name:"'+respaginas+'"})--(u:Titulos) RETURN u'
        #q='MATCH (:Generos { name: "Ciencia Ficcion" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) MATCH (:Paginas{name:"De 0 a 250 paginas"})--(u:Titulos) RETURN u'
        #q = 'MATCH (u: Titulos{genero:"Ciencia Ficcion"}) RETURN u'
        #q = 'MATCH (:Generos { name: "Ciencia Ficcion" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) RETURN u'
        results = db.query(q,returns=(client.Node,str,client.Node))
        #Se agregan todos los ambientes
        for i in results:
            print("-"+"%s"%(i[0]["titulo"]))
    x = True
def  romance(respaginas, costo2):
    #************************Filtración por Genero
    x = True 
    while x:  #Para que el usuario pueda elegir un ambiente y si se equivoca vuelve a preguntar
        print("\nLos libros que recomendamos de Romance: \n")
        #q='MATCH (:Generos { name: "Romance" })<--(u:Titulos) MATCH (:Costos {name:"'+costo2+'"})--(u:Titulos) MATCH (:Paginas{name:"'+respaginas+'"})--(u:Titulos) RETURN u'
        #q='MATCH (:Generos { name: "Romance" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) MATCH (:Paginas{name:"De 0 a 250 paginas"})--(u:Titulos) RETURN u'
        #q = 'MATCH (u: Titulos{genero:"Romance"}) RETURN u'
        #q = 'MATCH (:Generos { name: "Romance" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) RETURN u'
        results = db.query(q,returns=(client.Node,str,client.Node))
        #Se agregan todos los ambientes
        for i in results:
            print("-"+"%s"%(i[0]["titulo"]))
    x = True
def  filo(respaginas, costo2):
    #************************Filtración por Genero
    x = True 
    while x:  #Para que el usuario pueda elegir un ambiente y si se equivoca vuelve a preguntar
        print("\nLos libros que recomendamos de Filosofia: \n")
        #q='MATCH (:Generos { name: "Filosofia" })<--(u:Titulos) MATCH (:Costos {name:"'+costo2+'"})--(u:Titulos) MATCH (:Paginas{name:"'+respaginas+'"})--(u:Titulos) RETURN u'
        #q='MATCH (:Generos { name: "Filosofia" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) MATCH (:Paginas{name:"De 0 a 250 paginas"})--(u:Titulos) RETURN u'
        #q = 'MATCH (u: Titulos{genero:"Filosofia"}) RETURN u'
        #q = 'MATCH (:Generos { name: "Filosofia" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) RETURN u'
        results = db.query(q,returns=(client.Node,str,client.Node))
        #Se agregan todos los ambientes
        for i in results:
            print("-"+"%s"%(i[0]["titulo"]))
    x = True
def  nov_negra(respaginas, costo2):
    #************************Filtración por Genero
    x = True 
    while x:  #Para que el usuario pueda elegir un ambiente y si se equivoca vuelve a preguntar
        print("\nLos libros que recomendamos de Novela Negra: \n")
        #q='MATCH (:Generos { name: "Novela Negra" })<--(u:Titulos) MATCH (:Costos {name:"'+costo2+'"})--(u:Titulos) MATCH (:Paginas{name:"'+respaginas+'"})--(u:Titulos) RETURN u'
        #q='MATCH (:Generos { name: "Novela Negra" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) MATCH (:Paginas{name:"De 0 a 250 paginas"})--(u:Titulos) RETURN u'
        #q = 'MATCH (u: Titulos{genero:"Novela Negra"}) RETURN u'
        #q = 'MATCH (:Generos { name: "Novela Negra" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) RETURN u'
        results = db.query(q,returns=(client.Node,str,client.Node))
        #Se agregan todos los ambientes
        for i in results:
            print("-"+"%s"%(i[0]["titulo"]))
    x = True
def  drama(respaginas, costo2):
    #************************Filtración por Genero
    x = True 
    while x:  #Para que el usuario pueda elegir un ambiente y si se equivoca vuelve a preguntar
        print("\nLos libros que recomendamos de Dramatico: \n")
        #q='MATCH (:Generos { name: "Dramatico" })<--(u:Titulos) MATCH (:Costos {name:"'+costo2+'"})--(u:Titulos) MATCH (:Paginas{name:"'+respaginas+'"})--(u:Titulos) RETURN u'
        #q='MATCH (:Generos { name: "Dramatico" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) MATCH (:Paginas{name:"De 0 a 250 paginas"})--(u:Titulos) RETURN u'
        #q = 'MATCH (u: Titulos{genero:"Dramatico"}) RETURN u'
        #q = 'MATCH (:Generos { name: "Dramatico" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) RETURN u'
        results = db.query(q,returns=(client.Node,str,client.Node))
        #Se agregan todos los ambientes
        for i in results:
            print("-"+"%s"%(i[0]["titulo"]))
    x = True
def  Terror(respaginas, costo2):
    #************************Filtración por Genero
    x = True 
    while x:  #Para que el usuario pueda elegir un ambiente y si se equivoca vuelve a preguntar
        print("\nLos libros que recomendamos de Terror: \n")
        #q='MATCH (:Generos { name: "Terror" })<--(u:Titulos) MATCH (:Costos {name:"'+costo2+'"})--(u:Titulos) MATCH (:Paginas{name:"'+respaginas+'"})--(u:Titulos) RETURN u'
        #q='MATCH (:Generos { name: "Terror" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) MATCH (:Paginas{name:"De 0 a 250 paginas"})--(u:Titulos) RETURN u'
        #q = 'MATCH (u: Titulos{genero:"Terror"}) RETURN u'
        #q = 'MATCH (:Generos { name: "Terror" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) RETURN u'
        results = db.query(q,returns=(client.Node,str,client.Node))
        #Se agregan todos los ambientes
        for i in results:
            print("-"+"%s"%(i[0]["titulo"]))
    x = True

def  prosa(respaginas, costo2):
    #************************Filtración por Genero
    x = True 
    while x:  #Para que el usuario pueda elegir un ambiente y si se equivoca vuelve a preguntar
        print("\nLos libros que recomendamos de Prosa: \n")
        #q='MATCH (:Generos { name: "Prosa" })<--(u:Titulos) MATCH (:Costos {name:"'+costo2+'"})--(u:Titulos) MATCH (:Paginas{name:"'+respaginas+'"})--(u:Titulos) RETURN u'
        #q='MATCH (:Generos { name: "Prosa" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) MATCH (:Paginas{name:"De 0 a 250 paginas"})--(u:Titulos) RETURN u'
        #q = 'MATCH (u: Titulos{genero:"Prosa"}) RETURN u'
        #q = 'MATCH (:Generos { name: "Prosa" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) RETURN u'
        results = db.query(q,returns=(client.Node,str,client.Node))
        #Se agregan todos los ambientes
        for i in results:
            print("-"+"%s"%(i[0]["titulo"]))
    x = True

def  ensayo(respaginas, costo2):
    #************************Filtración por Genero
    x = True 
    while x:  #Para que el usuario pueda elegir un ambiente y si se equivoca vuelve a preguntar
        print("\nLos libros que recomendamos de Ensayo: \n")
        #q='MATCH (:Generos { name: "Ensayo" })<--(u:Titulos) MATCH (:Costos {name:"'+costo2+'"})--(u:Titulos) MATCH (:Paginas{name:"'+respaginas+'"})--(u:Titulos) RETURN u'
        #q='MATCH (:Generos { name: "Ensayo" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) MATCH (:Paginas{name:"De 0 a 250 paginas"})--(u:Titulos) RETURN u'
        #q = 'MATCH (u: Titulos{genero:"Ensayo"}) RETURN u'
        #q = 'MATCH (:Generos { name: "Ensayo" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) RETURN u'
        results = db.query(q,returns=(client.Node,str,client.Node))
        #Se agregan todos los ambientes
        for i in results:
            print("-"+"%s"%(i[0]["titulo"]))
    x = True
def  narrativa(respaginas, costo2):
    #************************Filtración por Genero
    x = True 
    while x:  #Para que el usuario pueda elegir un ambiente y si se equivoca vuelve a preguntar
        print("\nLos libros que recomendamos de Narrativa: \n")
        #q='MATCH (:Generos { name: "Narrativa" })<--(u:Titulos) MATCH (:Costos {name:"'+costo2+'"})--(u:Titulos) MATCH (:Paginas{name:"'+respaginas+'"})--(u:Titulos) RETURN u'
        #q='MATCH (:Generos { name: "Narrativa" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) MATCH (:Paginas{name:"De 0 a 250 paginas"})--(u:Titulos) RETURN u'
        #q = 'MATCH (u: Titulos{genero:"Narrativa"}) RETURN u'
        #q = 'MATCH (:Generos { name: "Narrativa" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) RETURN u'
        results = db.query(q,returns=(client.Node,str,client.Node))
        #Se agregan todos los ambientes
        for i in results:
            print("-"+"%s"%(i[0]["titulo"]))
    x = True
def  novela(respaginas, costo2):
    #************************Filtración por Genero
    x = True 
    while x:  #Para que el usuario pueda elegir un ambiente y si se equivoca vuelve a preguntar
        print("\nLos libros que recomendamos de Novela: \n")
        #q='MATCH (:Generos { name: "Novela" })<--(u:Titulos) MATCH (:Costos {name:"'+costo2+'"})--(u:Titulos) MATCH (:Paginas{name:"'+respaginas+'"})--(u:Titulos) RETURN u'
        #q='MATCH (:Generos { name: "Novela" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) MATCH (:Paginas{name:"De 0 a 250 paginas"})--(u:Titulos) RETURN u'
        #q = 'MATCH (u: Titulos{genero:"Novela"}) RETURN u'
        #q = 'MATCH (:Generos { name: "Novela" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) RETURN u'
        results = db.query(q,returns=(client.Node,str,client.Node))
        #Se agregan todos los ambientes
        for i in results:
            print("-"+"%s"%(i[0]["titulo"]))
    x = True
def  perio(respaginas, costo2):
    #************************Filtración por Genero
    x = True 
    while x:  #Para que el usuario pueda elegir un ambiente y si se equivoca vuelve a preguntar
        print("\nLos libros que recomendamos de Periodisitico: \n")
        #q='MATCH (:Generos { name: "Periodisitico" })<--(u:Titulos) MATCH (:Costos {name:"'+costo2+'"})--(u:Titulos) MATCH (:Paginas{name:"'+respaginas+'"})--(u:Titulos) RETURN u'
        #q='MATCH (:Generos { name: "Periodisitico" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) MATCH (:Paginas{name:"De 0 a 250 paginas"})--(u:Titulos) RETURN u'
        #q = 'MATCH (u: Titulos{genero:"Periodisitico"}) RETURN u'
        #q = 'MATCH (:Generos { name: "Periodisitico" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) RETURN u'
        results = db.query(q,returns=(client.Node,str,client.Node))
        #Se agregan todos los ambientes
        for i in results:
            print("-"+"%s"%(i[0]["titulo"]))
    x = True
def  sagas(respaginas, costo2):
    #************************Filtración por Genero
    x = True 
    while x:  #Para que el usuario pueda elegir un ambiente y si se equivoca vuelve a preguntar
        print("\nLos libros que recomendamos de Sagas: \n")
        #q='MATCH (:Generos { name: "Sagas" })<--(u:Titulos) MATCH (:Costos {name:"'+costo2+'"})--(u:Titulos) MATCH (:Paginas{name:"'+respaginas+'"})--(u:Titulos) RETURN u'
        #q='MATCH (:Generos { name: "Sagas" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) MATCH (:Paginas{name:"De 0 a 250 paginas"})--(u:Titulos) RETURN u'
        #q = 'MATCH (u: Titulos{genero:"Sagas"}) RETURN u'
        #q = 'MATCH (:Generos { name: "Sagas" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) RETURN u'
        results = db.query(q,returns=(client.Node,str,client.Node))
        #Se agregan todos los ambientes
        for i in results:
            print("-"+"%s"%(i[0]["titulo"]))
    x = True
def  aventura(respaginas, costo2):
    #************************Filtración por Genero
    x = True 
    while x:  #Para que el usuario pueda elegir un ambiente y si se equivoca vuelve a preguntar
        print("\nLos libros que recomendamos de Aventura: \n")
        #q='MATCH (:Generos { name: "Aventura" })<--(u:Titulos) MATCH (:Costos {name:"'+costo2+'"})--(u:Titulos) MATCH (:Paginas{name:"'+respaginas+'"})--(u:Titulos) RETURN u'
        #q='MATCH (:Generos { name: "Aventura" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) MATCH (:Paginas{name:"De 0 a 250 paginas"})--(u:Titulos) RETURN u'
        #q = 'MATCH (u: Titulos{genero:"Aventura"}) RETURN u'
        #q = 'MATCH (:Generos { name: "Aventura" })<--(u:Titulos) MATCH (:Costos {name:"Gratis PDF"})--(u:Titulos) RETURN u'
        results = db.query(q,returns=(client.Node,str,client.Node))
        #Se agregan todos los ambientes
        for i in results:
            print("-"+"%s"%(i[0]["titulo"]))
    x = True
