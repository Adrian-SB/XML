# -*- coding: utf-8 -*-

from lxml import etree
doc = etree.parse("Empresas.xml")
raiz=doc.getroot()

#4-Solicita el nombre de un residencia y muestra la longitud y latitud en un mapa.

residencia=raiz.findall("empresa/residencia")
longitud=raiz.findall("empresa/longitud")
latitud=raiz.findall("empresa/latitud")

pal=raw_input("Dime una residencia (Ejemplo: Roces)")

print "-------------------------------------------------------------"

for r,lo,la in zip (residencia,longitud,latitud):
    if pal == r.text:
        print r.text,"URL ->","\nhttps://www.openstreetmap.org/#map=18/",la.text,"/",lo.text
        print "-------------------------------------------------------------"
