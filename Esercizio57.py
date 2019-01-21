a=int(input())

if a==1:
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
    file.close()

if a==2:
    file=open("catalogo_film.csv","r")
    lines=file.readlines()
    conteggi2={}
    for riga in lines:
        data=riga.split(";")
        regista=data[3]
        if regista in conteggi2:
            conteggi2[regista]+=1
        else:
            conteggi2[regista]=1
    print(conteggi2)
    file.close()
