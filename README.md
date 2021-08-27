# TC1028 Proyecto


# Playlist

### contexto
El término en inglés “playlist” se refiere a una lista de reproducción en español. Normalmente, este término es utilizado para referirse a una serie o lista de canciones o videos que se reproducen sucesivamente. 

Fuente https://www.fundeu.es/recomendacion/playlist-lista-de-reproduccion/

En los últimos años, esta palabra es mayormente utilizada parar referirse a una lista de canciones y estas puedes hacerlas o encontrarlas en alguna plataforma de streaming como Spotify, Apple music, Amazon music, etcétera. 

Considero este tema interesante para mi proyecto puesto que mucha gente hace uso de las plataformas streaming en estos tiempos, entre ellas me encuentro yo. Además de que la música se me hace algo muy importante en la vida diaria, pues te puede poner feliz de una manera inexplicable y muy sencilla al escucharla. Finalmente, me parece una buena manera de que la gente amplíe sus gustos y conocimientos musicales de una manera sencilla y que pueda llamarles la atención, puesto que se les recomienda  de acuerdo a sus gustos y de una forma personalizada.

Este programa es un generador de playlists de 15 o 30 canciones, dependiendo de si elige 1 o dos géneros, basándose en el o los géneros que más le gusten al usuario. El programa corre en Python 3.7.4. Cuenta con una lista preelegida de canciones que el usuario no va a ver; el programa va a dar la opción de géneros que tiene y procederá a preguntar cuál desea elegir y luego si quiere agregar otro género, si es así, dará la opción de elegir y si no se irá directo a arrojar la lista de 15 canciones de dicho o dichos géneros. Una vez terminada, le pedirá saber si le gustó la playlist y si gusta repetir el programa para crear otra. 

### algoritmo

"""
listas pre seleccionada de canciones, dividida en género
"""
lista1("15 canciones de rock"
lista2("15 canciones de electrónica"
lista3("15 canciones de pop"
lista4("15 canciones de reggaeton"
lista5("15 canciones de rap"


E0: pedir el género que escucha (1-rock, 2-electrónica, 3-pop, 4-reggaetón, 5-rap)
	
  Si género==1
	
    EP(regresar lista)
	
  Si género==2
	  
    EP(regresar lista 2)
	
  Si género==3
	  
    EP(regresar lista 3)
	
  Si género==4
	  
    EP(regresar lista 4)
	
  Si género==5
	  
    EP(regresar lista 5)
	
  Si no
	  
    EP(regresar “aún no cuento con ese género”)

Preguntar si desea repetir el programa
  
  Si repsuesta==sí
	  
    EP(repetir)
	  
  Si respuesta==no
	  
    EF(TERMINAR)

