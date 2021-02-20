# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 13:07:40 2020

@author: elisa
"""

def lee(archivo):
    id = open(archivo,'r')
    contenido = id.read()
    id.close
    return contenido


def leeSepLineas(archivo):
    id = open(archivo,'r')
    contenido = id.read()
    listaRes = contenido.split("\n")
    id.close
    

    
    return listaRes
n = 0
listaRes= leeSepLineas("ArchivoCambios.txt")
print("La cadena")
Datos = lee("ArchivoDatos.txt")
print(Datos)
print(listaRes)
for i in listaRes:
    partes = i.split(",")
    par1 = partes[0]
    par2 = partes[1]
    Datos = Datos.replace(par1,par2)
    
    f = open("ArchivoDatos.txt")
    print("Elisa")
    print(Datos)
    f.write(Datos)
    f.close   
    print(Datos) #Aquí regresa el texto cambiado 




    
    
    