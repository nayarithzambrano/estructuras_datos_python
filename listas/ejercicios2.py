# ejercicios listas

# metodos propios

lista =[45,32,3,78]
print("lista original:", lista)
# funcion append: añade un elemento a la lista
lista.append(995)
lista.append(7)
print("lista despues de usar append:", lista)
# funcio sort: ordena la lista
lista.sort()
print("lista ordenada:", lista)
# funcion reverse: invierte el orden de la lista
lista.reverse()
print("lista al reves:", lista)
# funcion extend: añade los elementos de una lista ala lista
lista_extend=[1,5,87,45] 
lista.extend(lista_extend)
print("lista despues de extend:", lista)
# funcion count: cuenta el numero de veces que aparece el elemento indicado como parametro dentro de la lista
print("numeros de elementos 45:", lista.count(45))
# funcion insert: añade el elemento pasado como parametro ala lista en la condicio indicada tambien por parametro
lista.insert(4,111)
print("lista despues de insert:", lista)
# funcion  remove: elimina la primera ocurriencia empezando por la izquierda de la lista del elemeto indicado como parametro
lista.remove(45)
print("lista despues de remove:", lista)
# funcion index: de vuelve la posicion de la primera ocurriencia de izquierda a derecha en la lista del elemento pasado como parametro
print("posicion del elemento 111:", lista.index(111))
# funcion pop: elimina uel ultimo elemento de la lista y lo de vuelve como resultado de la operacion
lista.pop()
print("lista despues de pop:", lista)
# funcion clear: elimina todos los elemetos de la lista
lista.clear
print("lista despues de clear:", lista)














