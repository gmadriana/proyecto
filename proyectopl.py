"""
proyecto python
generador de playlist
el programa crea una playlist de 15 canciones o más
de acuerdo con el o los géneros que más le guste
escuchar a quien decida correrlo.
"""
#funciones

def otro():
    """
    (uso de funciones)
    determina si se debe repetir el programa o no
    """
    otro="si"
def genero():
    """
    (uso de funciones)
    determina el genero que el usuario desea escuchar en su nueva playlist
    """
    genero=int(input())
#listas

def lista1():
    """
    (archivo de texto)
    abre la playlist dependiendo del género elegido
    """
    lista1=open("rock.txt",'r')
def lista2():
    """
    (archivo de texto)
    abre la playlist dependiendo del género elegido
    """
    lista2=open("electronica.txt",'r')
def lista3():
    """
    (archivo de texto)
    abre la playlist dependiendo del género elegido
    """
    lista3=open("pop.txt",'r')
def lista4():
    """
    (archivo de texto)
    abre la playlist dependiendo del género elegido
    """
    lista4=open("reggaeton.txt",'r')
def lista5():
    """
    (archivo de texto)
    abre la playlist dependiendo del género elegido
    """
    lista5=open("rap.txt",'r')

#programa

lista1=open("rock.txt",'r')
lista2=open("electronica.txt",'r')
lista3=open("pop.txt",'r')
lista4=open("reggaeton.txt",'r')
lista5=open("rap.txt",'r')

otro="si"
while otro=="si":
    genero=int(input("¡hola! ¿qué genero musical prefieres: 1-rock, 2-electrónica, 3-pop, 4-reggaton o 5-rap? (teclea el numero)"))
    if genero==1:
        print("tu playlist es:",lista1.read())
    if genero==2:
        print("tu playlist es:",lista2.read())
    if genero==3:
        print("tu playlist es:",lista3.read())
    if genero==4:
        print("tu playlist es:",lista4.read())
    if genero==5:
        print("tu playlist es:",lista5.read())
    otro=input("qieres otra playlist (si,no)?")
else:
    if otro=="no":
        print("espero te haya gustado tu playlist:)")
