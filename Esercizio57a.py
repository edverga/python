a=raw_input("genere del film ")
b=int(input("prezzo massimo del film "))
file=open("catalogo_film.csv","r")
lines=file.readlines()
n=0
li=[]
for riga in lines:
    data=riga.split(";")
    genere=data[1]
    prezzo=data[5]
    if a == genere:
        li.append()
    n+=1
print(li)
