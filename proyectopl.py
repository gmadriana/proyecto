"""
proyecto python
generador de playlist
el programa crea una playlist de 15 canciones de
acuerdo con el o los géneros que más le guste
escuchar al usuario, además de que se puede repetir
las veces que este lo desee.
"""

#funciones

def genero():
    """
    (uso de funciones)
    recibe: rock (texto), electronica (texto), pop (texto), reggaeton (texto),
    rap (texto)
    determina el genero que el usuario desea escuchar en su nueva playlist
    devuelve: el nombre del género para la realización de la playlist
    """
    genero=input("¡hola! ¿qué genero musical prefieres: rock, electronica, pop, reggaton o rap?")
    return genero
def obten_playlist(playlists, genero_elegido):
    """
    (uso de funciones/matrices)
    recibe: playlists (matriz con las canciones de todas las playlists),
    genero_elegido (el género obtenido con la función "genero()")
    elige la playlist dependiendo del género ingresado
    devuelve: la playlist que había sido creada para el género elegido
    """
    genero_playlist=[]
    genero_playlist.append(genero_elegido)
    locacion=-1
    playlist_final=[]

    for i in range(len(playlists)):
        if playlists[i][0]==genero_playlist[0]:
            locacion=i
    if locacion==-1:
        print("aún no tenemos ese género")
    else:
        for i in range(len(playlists[locacion])-1):
            playlist_final.append(playlists[locacion][i+1])
        print(playlist_final, '\n')
    
#programa

otro="si"
while otro=="si":
    genero_elegido=genero()
    playlists=[["rock", "1. crying lightning - arctic monkeys", "2. mr. brightside - the killers", "3. afuera - caifanes", "4. cama - serbia", "5. juicebox - the strokes", "6. take me out - franz ferdinand", "7. madrugada - enjambre", "8. dias de fuego - odisseo", "9. spare me the details - the offspring", "10. sismo - division minuscula", "11. if you wanna - the vaccines", "12. mardy bum - arctic monkeys", "13. reptilia - the strokes", "14. do me a favour - arctic mokeys", "15. aqui no es asi - caifanes"],
               ["electronica", "1. the nights - avicci", "2. firestone - kygo", "3. beautiful now - zedd", "4. middle - dj snake", "5. feel so close - calvin harris", "6. you make me - avicci", "7. titanium - david guetta", "8. love tonight - shouse", "9. baiana - bakermat", "10. one kiss - calvin harris", "11. the wall - alok", "12. piece of your heart - meduza", "13. wow - tiesto", "14. without you - david ghetta", "15. out of my mind - klaas"],
               ["pop", "1. i kissed a girl - katy perry", "2. you belong with me - taylor swift", "3. good 4 u - olivia rodrigo", "4. heather - conan gray", "5. golden - harry styles", "6. blinding lights - the weekend", "7. shallow - lady gaga", "8. circles - post malone", "9. shape of you - ed sheeran", "10. chandelier - sia", "11. the scientist - coldplay", "12. the one that got away - katy perry", "13. wildest dreams - taylor swift", "14. idgaf - dua lipa", "15. ciega, sordomuda - shakira"],
               ["reggaeton", "1. nena maldicion - paulo londra", "2. la pregunta - j alvarez", "3. no me conoce - bad bunny", "4. te mudaste - bad bunny", "5. besos mojados - wisin y yandel", "6. dembow - danny ocean", "7. perreo en la luna - rich music ltd", "8. hola remix - dalex", "9. hookah & sheridan s - tommy boysen", "10. la player - zion & lennox", "11. la santa - bad bunny", "12. monaco - lagos", "13. yonaguni - bad bunny", "14. toda remix - alex rose", "15. una vez - bad bunny"],
               ["rap", "1. nunca te pude alcanzar - gera mx", "2. bombos y tarolas - cartel de santa", "3. se me olvidó - gera mx", "4. canela-nanpa basico", "5. buenos genes - rels b", "6. conmigo siempre - sabino", "7. tu - sabino", "8. rap god - eminem", "9. candy shop - 50 cent", "10. in da club - 50 cent", "11. solo por vos - trueno", "12. nuevequince - sabino", "13. te ire a buscar - santa fe klan", "14. huracan - gera mx", "15. yo no me quiero morir - charles ans"]]

    obten_playlist(playlists, genero_elegido)
    otro=input("¿quieres otra playlist (si,no)?")
    
else:
    if otro=="no":
        print("espero te haya gustado tu playlist (:")


