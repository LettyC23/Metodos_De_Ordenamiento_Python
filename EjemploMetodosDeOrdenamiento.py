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
        
    
    print ("================ ORDENAMIENTO POR SELECCION ====================")

def ordenamientoPorSeleccion(numeros):
    for recorrido in range (len(numeros) -1, 0, -1):
        posicionDelMayor =0
        for recorrido in range (1, recorrido+1):
            if numeros[recorrido] > numeros[posicionDelMayor]:
                posicionDelMayor = recorrido
                
                
        aux = numeros[recorrido]
        numeros [recorrido] = numeros[posicionDelMayor]
        numeros[posicionDelMayor] = aux
        
numeros = [34, 25, 12, 87, 9, 10, 34, 37, 24, 2]
print ("Arreglo sin ordenar")
print ( numeros)
print ("Arreglo ordenado")
ordenamientoPorSeleccion(numeros)
print (numeros)
print ("==================== ORDENAMIENTO POR INSECION ====================")

def ordenamiento_por_insercion(lista):
    for indice in range (1, len(lista)):
        valor = lista[indice]
        i = indice -1
        while i>=0:
            if valor < lista [i]:
                lista [i+1] = lista [i]
            
                lista [i] = valor
                i = i-1
            else:
                break
        
lista = [34, 25, 12, 87, 9, 10, 34, 37, 24, 2]
print ("lista sin ordenar")
print (lista)

print("Lista ordenada")
ordenamiento_por_insercion(lista)
print (lista)

print ("====================== ordenamiento QuickSort ==============")

def sort (numerosQ):
    izq = []
    centro = []
    der = []
    if len(numerosQ)>1:
        pivote = numerosQ[0]
        for i in numerosQ:
            if i < pivote:
                izq.append(i)
            elif i == pivote:
                centro.append(i)
            elif i >pivote:
                der.append(i)
        return sort(izq)+ centro+sort(der)
    else:
        return numerosQ
    
a = list(range( 0, 1000))
a = Random.sample(a, 1000)
a = sort(a)
print(a[0:10])
print (a[a:9999])
