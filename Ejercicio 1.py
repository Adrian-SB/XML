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