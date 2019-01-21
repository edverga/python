file=open("catalogo_film.csv","r")
lines=file.readlines()
conteggi={}
for riga in lines:
    data=riga.split(";")
    genere=data[1]
    if genere in conteggi:
        conteggi[genere]+=1
    else:
        conteggi[genere]=1
print(conteggi)
