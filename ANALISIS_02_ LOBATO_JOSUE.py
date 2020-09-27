#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 17:48:11 2020

@author: josue
"""
import csv

def escribir_csv(lista_datos,nombre_archivo,numero_filas):
    with open(str(nombre_archivo) +".csv","w") as archivo_csv:
        escritor = csv.writer(archivo_csv)
        escritor.writerows(lista_datos[:numero_filas])

def imprimir_10(lista):
    print()
    for i in range(10):
        print(lista[i][0],"-->",lista[i][1])
    print()
    
def imprimir2(lista):
    print()
    for i in [0,1,2]:
        print(lista[i][0])
        print("Cantidad de uso: ",lista[i][1])
        print("Valor: ",lista[i][2])
    print()
        
def conteo(direccion):
    contador = 0
    valor = 0
    rutas_contadas = []
    conteo_rutas = []
    
    for ruta in lista_datos:
        #filtro de exportacion o importacion
        if ruta[1] == direccion:
            ruta_actual = [ruta[2],ruta[3]]
            #filtro de rutas ya contadas
            if ruta_actual not in rutas_contadas:
                #volvemos a iterar sobre la lista, para las coincidencias
                for movimiento in lista_datos:
                    if movimiento[1]==direccion:
                        if ruta_actual == [movimiento[2],movimiento[3]]:
                            contador += 1
                            valor += int(movimiento[9])
                rutas_contadas.append(ruta_actual)
                conteo_rutas.append([ruta[2],ruta[3],contador,valor])
                contador = 0
                valor = 0
    conteo_rutas.sort(reverse = True,key = lambda x:x[2])
    return conteo_rutas


def contador_transporte(direccion):
    contador = 0
    valor = 0
    transporte_contados = []
    conteo_transporte = []
    
    for ruta in lista_datos:
            #filtro de exportacion o importacion
            if ruta[1] == direccion:
                transporte_actual = [ruta[7]]
                #filtro de transporte ya contado
                if transporte_actual not in transporte_contados:
                    #volvemos a iterar sobre la lista, para las coincidencias
                    for movimiento in lista_datos:
                        if movimiento[1]==direccion:
                            if transporte_actual == [movimiento[7]]:
                                contador += 1
                                valor += int(movimiento[9])
                    transporte_contados.append(transporte_actual)
                    conteo_transporte.append([ruta[7],contador,valor])
                    contador = 0
                    valor = 0
    conteo_transporte.sort(reverse = True,key = lambda x:x[2])
    #Los ordena respecto al valor como pide la consigna
    return conteo_transporte    

def pais_mayor(direccion):
    valor = 0
    contador = 0
    pais_contado = []
    pais = []
    
    for linea in lista_datos:
        if linea[1] == direccion:
            pais_actual = linea[2]
            if pais_actual not in pais_contado:
                for contar in lista_datos:
                    if contar[1] == direccion:
                        if contar[2] == pais_actual:
                            contador += 1
                            valor += int(contar[9])
                pais_contado.append(pais_actual)
                pais.append([pais_actual,contador,valor])
                contador = 0
                valor = 0
    pais.sort(reverse = True,key=lambda x:x[2])
    return pais

lista_datos = []

with open("synergy_logistics_database.csv","r") as archivo_csv:
    lector = csv.reader(archivo_csv)
    
    #Copia de los datos en lista_datos
    for linea in lector:
        lista_datos.append(linea)
    lista_datos.pop(0)

#CONSIGNA 1

conteo_exportaciones = conteo('Exports')
conteo_importaciones = conteo('Imports')


#copias acomodadas por valor
conteo_exp_valor = conteo_exportaciones.copy()
conteo_imp_valor = conteo_importaciones.copy()

escribir_csv(conteo_exportaciones,'exportacionesporruta',10)
escribir_csv(conteo_importaciones,'importacionesporruta',10)

#Ordenar por valor
conteo_exp_valor.sort(reverse = True,key = lambda x:x[3])
conteo_imp_valor.sort(reverse = True,key = lambda x:x[3])

escribir_csv(conteo_exp_valor,'exportacionesporvalor',10)
escribir_csv(conteo_imp_valor,'importacionesporvalor',10)


print("Top 10 Exportaciones por transito de ruta")
imprimir_10(conteo_exportaciones)
print("Top 10 Exportaciones por valor")
imprimir_10(conteo_exp_valor)


    



print()

print("Top 10 Importaciones por transito de ruta")
imprimir_10(conteo_importaciones)
print("Top 10 Importaciones por valor")
imprimir_10(conteo_imp_valor)





#CONSIGNA 2
print("CONSIGNA 2")

transporte_exp = contador_transporte('Exports')
transporte_imp = contador_transporte('Imports')

escribir_csv(transporte_exp,'transporteexp',3)
escribir_csv(transporte_imp,'transporteimp',3)


print("Top 3 medios de transporte por valor \nEXPORTACIONES ")
imprimir2(transporte_exp)


print("Top 3 medios de transporte por valor \nIMPORTACIONES")
imprimir2(transporte_imp)

#No nos dice nada, los resultados parecen logicos



#CONSIGNA 3
#Se considera que quien hace la exportacion y quien pide la importacion es el que paga
print()
print('Consigna 3')
print()

#EXPORTACION
print('Paises que generan el 80% de ganancias en EXPORTACION, ordenados por valor:')
pais_export = pais_mayor('Exports')
total = 0
for p in pais_export:
    total += int(p[2])

count = 0
suma = 0   
for p in pais_export:
    if suma < total*0.80:
        suma += int(p[2])
        count +=1
        print('Operaciones que paga: ',p[1],p[0],'valor: ',p[2])


print('Número total de paises que dan el 80% de valor: ',count)
print("Porcentaje del valor de los paises sobre el total: %.2f" %((suma/total)*100))


#IMPORTACION
print()
print('Paises que generan el 80% de ganancias en IMPORTACION, ordenados por valor:')
pais_import = pais_mayor('Imports')
total = 0
for p in pais_import:
    total += int(p[2])

count = 0
suma = 0   
for p in pais_import:
    if suma < total*0.80:
        suma += int(p[2])
        count +=1
        print('Operaciones que paga: ',p[1],p[0],'valor: ',p[2])

print('Número total de paises que dan el 80% de valor: ',count)
print("Porcentaje del valor de los paises sobre el total: %.2f" %((suma/total)*100))


escribir_csv(pais_export,'paisexport',8)
escribir_csv(pais_import,'paisimport',8)