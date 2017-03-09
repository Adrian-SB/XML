# -*- coding: utf-8 -*-

from lxml import etree
doc = etree.parse("Empresas.xml")
raiz=doc.getroot()

#2-Tras introducir una cadena de texto, muestra el número de empresa en las que su descripción coincida con dicha cadena(Tipo de empresa).


palabra=raw_input("Busqueda por palabras claves:")

nombre=raiz.findall("empresa/titulo")
descripcion=raiz.findall("empresa/descripcion")
print ""

try:
    for n, d in zip(nombre,descripcion):
        contDescripcion=d.text
        if palabra in contDescripcion:
            veces=contDescripcion.count(palabra)
            print "La palabra",palabra,"aparece",veces, "veces en la descripción de",n.text
except:
    print ""