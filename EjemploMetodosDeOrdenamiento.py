'''
Created on 14/11/2018

@author: lety
'''

print ("================= ORDENAMIENTO CON BURBUJA =====================")

def ordenamientoConBurbuja(numero):
    
    for r in range (len (numero)):
        for a in range (len (numero)):
            if numero [r] > numero[a]:
                aux = numero[r]
                numero[r] = numero [a]
                numero[a] = aux
                
numero = [34, 25, 12, 87, 9, 10, 34, 37, 24, 2]
print ("Burbuja 0")
print ("Arreglo sin ordenar")
print (numero)
print ("Arreglo ordenado")
ordenamientoConBurbuja(numero)
print (numero)

def ordenamientoConBurbuja1(numeros1):
    for r in range (len (numeros1)+2):
        for a in range (len (numeros1)-1):
            if numeros1 [a] > numeros1[a+1]:
                aux = numeros1[a]
                numeros1[a] = numeros1 [a+1]
                numeros1[a+1] = aux
numeros1 = [34, 25, 12, 87, 9, 10, 34, 37, 24, 2]
print ("burbuja 1")
print ("Arreglo sin ordenar")
print (numeros1)
print ("Arreglo ordenado")
ordenamientoConBurbuja1(numeros1)
print (numeros1)

def ordenamientoConBurbuja2(numeros2):
    i=0
    ordenado = False
    while (i>numeros2.length and ordenado==True):
        if (i<numeros2.length and ordenado==False):
              for r in range (len (numeros2)):
                  for a in range (len (numeros2)-1):
                       if numeros2 [a] > numeros2[a+1]:
                        aux = numeros2[a]
                        numeros2[a] = numeros2 [a+1]
                        numeros2[a+1] = aux
            
    
numeros2 = [34, 25, 12, 87, 9, 10, 34, 37, 24, 2]
print ("burbuja 2")
print ("Arreglo sin ordenar")
print (numeros2)
print ("Arreglo ordenado")
ordenamientoConBurbuja1(numeros2)
print (numeros2)

def ordenamientoConBurbuja3(numeros3):
    
    for r in range (len (numeros2)):
        minimo=r
        for a in range (len (numeros2)):
            if numeros3 [a] > numeros3[minimo]:
                minimo = a
            aux = numeros3[r]
            numeros3[r] = numeros3[minimo]
            numeros3[minimo] = aux
            
numeros3 = [34, 25, 12, 87, 9, 10, 34, 37, 24, 2]
print ("burbuja 3")
print ("Arreglo sin ordenar")
print (numeros3)
print ("Arreglo ordenado")
ordenamientoConBurbuja1(numeros3)
print (numeros3)                
        