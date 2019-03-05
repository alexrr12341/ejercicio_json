def listar_juegos(doc):
	compañia=str(input("Dime una compañia. "))
	listaG=[]
	indicador=False
	for comp in doc["compañias"]["compañia"]:
		if comp["name"]==compañia:
			print("Compañia detectada.")
			input("Presione enter para continuar.")
			indicador=True
			for consolas in comp["consola"]:
				if type(consolas["games"]["game"])==list:
					for juegos in consolas["games"]["game"]:
						listaG.append(juegos["_name"])
				else:
					listaG.append(consolas["games"]["game"]["_name"])
	return listaG
	if not indicador:
		print("Esa compañia no esta en nuestra base de datos.")

########################
import json
import codecs
doc=json.load(codecs.open('CompañiasConsolas.json', 'r', 'utf-8-sig'))
opciones='''1.Listar nombre de juego
2.Contar Juegos de consola
3.Generos de una consola
4.Compañias de Juegos
5.Caracteristicas Juegos
0.Salir'''
opcion=int
while opcion!=0:
    print(opciones)
    opcion=int(input("Dime la opción. "))
    if opcion==1:
       for juegos in listar_juegos(doc):
       		print(juegos)
    elif opcion==2:
        print("adios")
    elif opcion==3:
        print("buenas")
        #Ejemplo Darius,Ziggs,Anivia
    elif opcion==4:
        print("ejercicio4")
        #Ejemplo Spinning Axe,Courage,Quickdraw
    elif opcion==5:
        print("ejercicio5")
    elif opcion==0:
        print("Fin del programa.")
