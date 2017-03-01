# -*- coding: utf-8 -*-

from lxml import etree
doc = etree.parse("Empresas.xml")
raiz=doc.getroot()

zurrapa=['\\n','\n','<p>','</p>','<br>','<br/>','...']

#1-Lista las empresa con su residencia correspondiente.

nombre=raiz.findall("empresa/titulo")
residencia=raiz.findall("empresa/residencia")

for n, r in zip(nombre,residencia):
    for z in zurrapa:#Limpiador
            n.text=n.text.replace(z,"")

    print "Nombre de la empresa:",n.text
    print "Residencia:",r.text,"\n"

#2-Tras introducir una cadena de texto, muestra el número de empresa en las que su descripción coincida con dicha cadena(Tipo de empresa).

palabra=raw_input("Busqueda por palabras claves:")

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

