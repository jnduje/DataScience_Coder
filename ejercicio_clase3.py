dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
valores = [200, 225, 232, 221, 243, 256, 255]
dias_baja = []

for i in range (1, 7):     
    #print (i)
    if valores[i] < valores [i-1]:
        dias_baja.append(dias[i])
        #print(dias[i])

print(dias_baja)