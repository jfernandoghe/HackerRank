import array
import array
num=int(input())
nc={}
nc2={}
sq={}
j, k, i, e, flag, count = 0,  0, 0, 0, 0, 0
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
#************************************************************************
while count<num:
    for i in range (0,num):                   #Eliminar los 0 de SQ3 cuanco nc[i]==0
        if nc2[i]==0:
            for j in range (0,12):
                flag=sq3[i][j]
                sq3[i][j]=0
                sq4[i][j]=0
                for k in range (0,num):
                    if sq3[k][j]==flag:
                        sq3[k][j]=0
#************************************************************************
    j, k, i =  0, 0, 0                      #Evaluar si los ot estan dentro de sq3, sino los elimina de ot
    for i in range (0,num):
        for j in range (0,12):
            if sq2[i][j]!=sq3[i][j]:
                for k in range (0,10):
                    if ot[k][j]==sq2[i][j]:
                        ot[k][j]=0
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
    count+=1
    if count>=12:
        break
#************************************************************************
#Eliminar para resultado final
#for i in range (0,12):
#    if o[i]!=0:
#        for j in range (0,10):
#            ot[j][i]=0
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
for i in range (0,num):                   #SQ2
    print (sq2[i], nc[i])
