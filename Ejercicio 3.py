# -*- coding: utf-8 -*-

from lxml import etree
doc = etree.parse("Empresas.xml")
raiz=doc.getroot()

#3-Lista las empresas con más de un teléfono.

nombres=raiz.findall("empresa/titulo")
telefonos=("empresa/telefono")

sep="/"

for n in nombres:
    if sep in telefonos:
        print "La asosiacion",n.text, "tiene 2 telefonos"