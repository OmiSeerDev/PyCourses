#CRUD de listas

#Create

lista = [1,2,3,4,5]

#Read

lista[0]

#Update
lista[4] = 9 

lista.append(5)
print(lista)

lista.insert(5, 10)
print(lista)
#Delete

lista.pop() #extrae el último elemento
print(lista)

lista.remove(1) #extrae un elemento conocido
print(lista)

lista.remove(9)
print(lista)