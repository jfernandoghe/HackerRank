import array
import array
num=int(input())
nc={}
nc2={}
sq={}
j, k, i, e, tot, count = 0,  0, 0, 0, 0, 0
sq2 = [[0 for x in range(12)] for y in range(num)] 
sq3 = [[0 for x in range(12)] for y in range(num)] 
sq4 = [[0 for x in range(12)] for y in range(num)]
ot  = [[0 for x in range(12)] for y in range(10)]
o = [0,0,0,0,0,0,0,0,0,0,0,0]
for i in range (0,num):
    entry = str(input()).split(" ")
    sq[i] = str(entry[0])
    nc[i] = str(entry[1])
    nc2[i]= int(nc[i])
while k==0:                             #Rellenar de 0 a 9 la matriz de salida
    for i in range (0,10):
        ot[i][j]=i
        if i==9:
            j=j+1
        if j==12:
            k=k+1
#************************************************************************
j, k, i =  0, 0, 0
while k==0:                             #Rellenar SQ2 y SQ3
    for i in range (0,num):               
        sq3[i][j]=int(sq[i][j:j+1])
        sq2[i][j]=int(sq[i][j:j+1])
        sq4[i][j]=int(sq[i][j:j+1])
        if i==num-1:
            j=j+1
        if j==12:
            k=k+1
#************************************************************************
while count<12:
    for i in range (0,num):                   #Eliminar los 0 de SQ3
        if nc2[i]==0:
            for j in range (0,12):
                sq3[i][j]=0
                sq4[i][j]=0
#************************************************************************
    j, k, i =  0, 0, 0                      #Eliminar digitos cuando nc==0 de OT
    for k in range (0,num):
        if nc[k]=='0':
            for i in range (0,10):
                for j in range (0,12):
                    if sq2[k][j]==ot[i][j]:
                        ot[i][j]=0
#************************************************************************ 
    j, k, i =  0, 0, 0                      #Si hay 1 solo valor en ot buscan similares en el vector fila
    for i in range (0, num):
        for j in range (0,12):
            if o[j]!=0:
                if sq3[i][j]==o[j]:
                    sq3[i][j]=0
#************************************************************************ 
    j, k, i =  0, 0, 0                      #Si hay 1 solo valor en ot se lo asigna a o
    for i in range (0, 12):
        for j in range (0,10):
            if ot[j][i]!=0:
                flag=ot[j][i]
                k=k+1
        if k==1:
            o[i]=flag
#************************************************************************ 
    j, k, i =  0, 0, 0                     #Si un digito de o es diferente de 0 y aparece en SQ3 disminuimos nc
    for i in range (0,num):
        for j in range (0,12):
            if o[j]!=0 and o[j]==sq3[i][j]:
                nc2[i]-=1
                if nc2[i]==0:
                    sq3[i][j]=0

#************************************************************************ 
    j, k, i,e = 0, 0, 0, 0                     #Si un num de los OT aparece en la secuencia disponible SQ3 lo da 
    for i in range (0,num):
        for j in range (0,12):
            for k in range (0,10):                
                if e==1:    
                    o[j]=ot[k][j]
    #                nc2[i]-=1
    #            if ot[k][j]==sq3[i][j] and ot[k][j]!=0:
    #                e=e+1

#************************************************************************
    j, k, i =  0, 0, 0                     #Si nc2<0 damos toda la fila en 0
    for i in range (0,num):
        for j in range (0,12):
            if nc2[i]<=0:
                sq3[i][j]=0
                nc2[i]=0
#************************************************************************
    j, k, i =  0, 0, 0                     #Si tenemos 1 digito en o hacemos toda la columna 0
    for i in range (0,num):
        for j in range (0,12):
            if o[j]!=0:
                sq3[i][j]=0
    count+=1
    if count>=12:
        break
#************************************************************************     
print('************************************         RES')    
print(o)
print('************************************         OT')
for i in range (0,10):                   #RES
    print (ot[i])
print('************************************         SQ3')
for i in range (0,num):                   #SQ3
    print (sq3[i],nc[i], ' ', nc2[i])
print('************************************         SQ4')
for i in range (0,num):                   #SQ4
    print (sq4[i],nc[i], ' ', nc2[i])
print('************************************         SQ2')
for i in range (0,num):                   #SQ3
    print (sq2[i], nc[i])
