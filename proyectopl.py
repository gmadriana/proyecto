"""
proyecto python
generador de playlist
el programa crea una playlist de 15 canciones o más
de acuerdo con el o los géneros que más le guste
escuchar a quien decida correrlo.
"""

#listas

lista1=("crying lightning-arctic monkeys, mr. brightside-the killers, afuera-caifanes, cama-serbia, juicebox-the strokes, take me out-franz ferdinand, madrugada-enjambre, dias de fuego-odisseo, spare me the details-the offspring, sismo-division minuscula, if you wanna-the vaccines, mardy bum-arctic monkeys, reptilia-the strokes, do me a favour-arctic mokeys, aqui no es asi-caifanes")
lista2=("the nights-avicci, firestone-kygo, beautiful now-zedd, middle-dj snake, feel so close-calvin harris, you make me-avicci, titanium-david guetta, love tonight-shouse, baiana-bakermat, one kiss-calvin harris, the wall-alok, piece of your heart-meduza, wow-tiesto, without you-david ghetta, out of my mind-klaas")
lista3=("i kissed a girl-katy perry, you belong with me-taylor swift, good 4 u- olivia rodrigo, heather-conan gray, golden-harry styles, blinding lights-the weekend, shallow-lady gaga, circles-post malone, shape of you-ed sheeran, chandelier-sia, the scientist-coldplay, the one that got away-katy perry, wildest dreams-taylor swift, idgaf-dua lipa, ciega, sordomuda-shakira")
lista4=("nena maldicion-paulo londra, la pregunta-j alvarez, no me conoce-bad bunny, te mudaste-bad bunny, besos mojados-wisin y yandel, dembow-danny ocean, perreo en la luna-rich music ltd, hola remix-dalex, hookah & sheridan s-tommy boysen, la player-zion & lennox, la santa-bad bunny, monaco-lagos, yonaguni-bad bunny, toda remix-alex rose, una vez-bad bunny")
lista5=("nunca te pude alcanzar-gera mx, bombos y tarolas-cartel de santa, se me olvidó-gera mx, canela-nanpa basico,  buenos genes-rels b, conmigo siempre-sabino, tu-sabino, rap god-eminem, candy shop-50 cent, in da club-50 cent, solo por vos-trueno, nuevequince-sabino, te ire a buscar-santa fe klan, huracan-gera mx, yo no me quiero morir-charles ans")

# inicio

genero=int(input("¡hola! ¿qué genero musical prefieres: 1-rock, 2-electrónica, 3-pop, 4-reggaton o 5-rap? (teclea el numero)"))
if genero==1:
    print("tu playlist es:",lista1)
if genero==2:
    print("tu playlist es:",lista2)
if genero==3:
    print("tu playlist es:",lista3)
if genero==4:
    print("tu playlist es:",lista4)
if genero==5:
    print("tu playlist es:",lista5)
