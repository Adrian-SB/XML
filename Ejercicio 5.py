# -*- coding: utf-8 -*-

from lxml import etree
doc = etree.parse("Empresas.xml")
raiz=doc.getroot()

#5-Programa que lea por teclado el nombre de la empresa y muestra su teléfonos,fax,email y pagina web.

nombre=raiz.findall("empresa/titulo")
telefonos2=raiz.findall("empresa/telefono")
fax=raiz.findall("empresa/fax")
email=raiz.findall("empresa/mail")
web=raiz.findall("empresa/web")
nemp=raw_input("Dime una empresa(Ejemplo Z2 Arquitectos):")
zurrapa2=['</a']


try:
    for n,t,f,em,w in zip (nombre,telefonos2,fax,email,web):
        if n.text == nemp:
            print "\nTeléfono:",t.text
            print "Fax:",f.text
            for z in zurrapa2:#Limpiador:
                em.text=em.text.replace(z,"")
                print "Correo electrónico:",em.text.split(">")[1]
                w.text=w.text.replace(z,"")
                print "Página Web:",w.text.split(">")[1]
except:
    print ""