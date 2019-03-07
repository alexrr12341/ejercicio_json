def listar_juegos(doc,compania):
	listaG=[]
	for comp in doc["compañias"]["compañia"]:
		if comp["name"]==compania:
			print("Compañia detectada.")
			input("Presione Enter para continuar.")
			for consolas in comp["consola"]:
				if type(consolas["games"]["game"])==list:
					for juegos in consolas["games"]["game"]:
						listaG.append(juegos["_name"])
				else:
					listaG.append(consolas["games"]["game"]["_name"])
	return listaG
def contar_juegos(doc,consola):
	listaG=[]
	contador=0
	for comp in doc["compañias"]["compañia"]:
		for consolas in comp["consola"]:
			if consolas["listname"]==consola:
				print("Consola detectada")
				input("Presione Enter para continuar.")
				if type(consolas["games"]["game"])==list:
					for juegos in consolas["games"]["game"]:
						listaG.append(juegos["_name"]) 
				else:
					listaG.append(consolas["games"]["game"]["_name"])
	for juegos in listaG:
		contador+=1
	return contador
def generos_consola(doc,consola):
	listaG=[]
	listaJ=[]
	for comp in doc["compañias"]["compañia"]:
		for consolas in comp["consola"]:
			if consolas["listname"]==consola:
				print("Consola detectada")
				input("Presione Enter para continuar.")
				if type(consolas["games"]["game"])==list:
					for juegos in consolas["games"]["game"]:
						listaG.append(juegos["genre"])
						listaJ.append(juegos["_name"])
				else:
					listaG.append(consolas["games"]["game"]["genre"])
					listaJ.append(consolas["games"]["game"]["_name"])
	return zip(listaG,listaJ)

def juego_compañia(doc,juego):
	for comp in doc["compañias"]["compañia"]:
		for consolas in comp["consola"]:
			for juegos in consolas["games"]["game"]:
				if juegos["_name"]==juego:
					print("Juego detectado")
					input("Presione Enter para continuar.")
					return comp["name"]

def caracteristicas_juego(doc,juego):
	for comp in doc["compañias"]["compañia"]:
		for consolas in comp["consola"]:
			for juegos in consolas["games"]["game"]:
				if juegos["_name"]==juego:
					print("Juego detectado")
					input("Presione Enter para continuar.")
					lista=[consolas["listname"],comp["name"],juegos["description"],juegos["cloneof"],juegos["crc"],juegos["manufacturer"],juegos["year"],juegos["genre"],juegos["rating"],juegos["enabled"]]
	return lista
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
    	compania=str(input("Dime una compañia. "))
    	#Ejemplos Sony,Nintendo,Sega
    	for juegos in listar_juegos(doc,compania):
    		print(juegos)
    elif opcion==2:
    	consola=str(input("Dime el nombre de la consola. "))
    #Ejemplos Nintendo 64,Nintendo Game Boy Advance,Sega Classics,Sega Genesis,Sony PlayStation,Sony PlayStation 2
    	if contar_juegos(doc,consola)==0:
    		print("Esa consola no tiene juegos.")
    	else:
    		print("Hay",contar_juegos(doc,consola),"juegos en esta consola.")
    elif opcion==3:
    	consola=str(input("Dime el nombre de la consola. "))
    	for generos in generos_consola(doc,consola):
    		print(generos[1]," Genero-->",generos[0])
        #Ejemplos Nintendo 64,Nintendo Game Boy Advance,Sega Classics,Sega Genesis,Sony PlayStation,Sony PlayStation 2
    elif opcion==4:
    	juego=str(input("Dime el nombre del juego. "))
    	if juego_compañia(doc,juego)==None:
    		print("Ese juego no tiene compañia.")
    	else:
    		print("Su compañia es",juego_compañia(doc,juego))
        #Ejemplos 007 - GoldenEye (USA),V.I.P. (USA),WWF No Mercy (USA) (Rev A),Majesco's Rec Room Challenge (USA),Duke Nukem - Time to Kill (USA),Caesars Palace (USA),Burning Force (USA)
    elif opcion==5:
    	#Ejemplos ,V.I.P. (USA),WWF No Mercy (USA) (Rev A),Majesco's Rec Room Challenge (USA),Duke Nukem - Time to Kill (USA),Caesars Palace (USA),Burning Force (USA)
    	juego=str(input("Dime el nombre del juego. "))
    	try:
    		lista=caracteristicas_juego(doc,juego)
    	except:
    		print("Ese juego no tiene caracteristicas.")
    	else:
    		print("Su compañia es",lista[1])
    		print("Su consola es",lista[0])
    		print("Caracteristicas:")
    		print("Descripcion-->",lista[2])
    		print("Copia de -->",lista[3])
    		print("crc -->",lista[4])
    		print("Fabricante -->",lista[5])
    		print("Año de Salida -->",lista[6])
    		print("Genero -->",lista[7])
    		print("PEGI -->",lista[8])
    		print("Lanzado -->",lista[9])
    elif opcion==0:
        print("Fin del programa.")
