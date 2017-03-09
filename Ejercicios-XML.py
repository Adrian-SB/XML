# -*- coding: utf-8 -*-

from lxml import etree
doc = etree.parse("Empresas.xml")
raiz=doc.getroot()

zurrapa=['\\n','\n','<p>','</p>','<br>','<br/>','...']

print "\n1-Lista las empresa con su residencia correspondiente.\n"

nombre=raiz.findall("empresa/titulo")
residencia=raiz.findall("empresa/residencia")

for n, r in zip(nombre,residencia):
    for z in zurrapa:#Limpiador
            n.text=n.text.replace(z,"")

    print "Nombre de la empresa:",n.text
    print "Residencia:",r.text,"\n"

print "\n2-Tras introducir una cadena de texto, muestra el número de empresa en las que su descripción coincida con dicha cadena(Tipo de empresa).\n"

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


print "\n3-Lista las empresas con más de un teléfono.\n"

pausa=raw_input("Pulsa Intro")
print""

telefonos1=("empresa/telefono")

sep="/"

for n in nombre:
    if sep in telefonos1:
        print "La empresa",n.text, "tiene 2 teléfonos"

print "\n4-Solicita el nombre de un residencia y muestra la longitud y latitud en un mapa.\n"

longitud=raiz.findall("empresa/longitud")
latitud=raiz.findall("empresa/latitud")

pal=raw_input("Dime la residencia:")

for r,lo,la in zip (residencia,longitud,latitud):
    if pal == r.text:
        print r.text,"URL ->","\nhttps://www.openstreetmap.org/#map=18/",la.text,"/",lo.text

print "\n5-Programa que lea por teclado el nombre de la empresa y muestra su teléfonos,fax,email y pagina web.\n"

telefonos2=raiz.findall("empresa/telefono")
fax=raiz.findall("empresa/fax")
email=raiz.findall("empresa/mail")
web=raiz.findall("empresa/web")
nemp=raw_input("Dime una empresa: ")
zurrapa2=['</a']

for n,t,f,em,w in zip (nombre,telefonos2,fax,email,web):
    if n.text == nemp:
        print "\nTeléfono:",t.text
        print "Fax:",f.text
        for z in zurrapa2:#Limpiador:
            em.text=em.text.replace(z,"")
            print "Correo electrónico",em.text.split(">")[1]
            w.text=w.text.replace(z,"")
            print "Página Web:",w.text.split(">")[1]