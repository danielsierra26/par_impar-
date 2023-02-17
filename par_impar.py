#PROGRAMA PARA SABER SI UN NÚMERO ES PAR O IMPAR 
print("--------------------------------")
print("---- Numero par o impar  -----")
print("--------------------------------")


#input
x = int(input("Dijite un numero: "))

#processing
r=(x%2)
if r==0:
    msj="PAR"
else:
    msj="IMPAR"  

# output
print("--------------------------------")
print("---- ----resultados------  -----")
print("--------------------------------")
print(" EL NUMERO :" + str(x) + " ES: " + msj)