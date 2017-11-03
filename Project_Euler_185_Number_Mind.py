while k==0:                             #Rellenar de 0 a 9 la matriz de salida
    for i in range (0,10):
        ot[i][j]=i
        if i==9:
            j=j+1
        if j==12:
            k=k+1
j, k, i =  0, 0, 0
#************************************************************************
while k==0:                             #Rellenar SQ2 y SQ3
    for i in range (0,num):               
        sq3[i][j]=int(sq[i][j:j+1])
        sq2[i][j]=int(sq[i][j:j+1])
        if i==num-1:
            j=j+1
        if j==12:
            k=k+1
for i in range (0,num):                   #Eliminar los 0 de SQ3
    if nc[i]=='0':
        for j in range (0,12):
            sq3[i][j]=0
#************************************************************************
j, k, i =  0, 0, 0                      #Eliminar digitos cuando nc==0 de OT
for k in range (0,num):
    if nc[k]=='0':
        for i in range (0,10):
            for j in range (0,12):
                if sq2[k][j]==ot[i][j]:
                    ot[i][j]=0
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
j, k, i, c =  0, 0, 0, 0                #Si 1 valor de los posibles OT aparece en SQ3
for i in range (0,num):
    for j in range (0,12):
        for k in range (0,10):
            if ot[k][j]==sq2[i][j]:
                flag=ot[k][j]
                c=c+1
        if c==1:
            o[j]=flag

#************************************************************************ 
j, k, i =  0, 0, 0                     #Si un digito de o es diferente de 0 y aparece en SQ3 disminuimos nc
for i in range (0,num):
    for j in range (0,12):
        if o[j]!=0 and o[j]==sq3[i][j]:
            nc2[i]-=1
#************************************************************************
j, k, i =  0, 0, 0                     #Si tenemos 1 digito en o hacemos toda la columna 0
for i in range (0,num):
    for j in range (0,12):
        if o[j]!=0:
            sq3[i][j]=0
#************************************************************************ 

#************************************************************************     
print('************************************         RES')    
print(o)
print('************************************         OT')
for i in range (0,10):                   #RES
    print (ot[i])
print('************************************         SQ3')
for i in range (0,num):                   #SQ2
    print (sq3[i],nc[i], nc2[i])
print('************************************         SQ2')
for i in range (0,num):                   #SQ3
    print (sq2[i],nc[i],'   ', nc2[i])
