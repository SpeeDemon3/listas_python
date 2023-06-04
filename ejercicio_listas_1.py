# Array de nombres
names = ['Antonio', 'Chula', 'Arya', 'Patricia']

# Imprimo cada elemento de names accediendo a su posicion
print(f"{names[0]}, {names[1]}, {names[2]}, {names[3]}")

# Creo un mensaje de bienvenida
message = "Bienvenido/a a Python:\n\t"

# Imprimo por consola un saludo para cada elemento de la lista
print(message + names[0])
print(message + names[1])
print(message + names[2])
print(message + names[3])

# Cambio el valor del primer elemento de la lista
names[0] = 'Lobezno'
print("\n" + names[0])

# Añadir elementos al final de la lista con el metodo .append('nuevo_elemento')
names.append('Antonio')
print(names)
names.append('Terminator')
print(names)

# Creo una lista vacia y le añado elementos
avengers = [] # Lista vacia
avengers.append('Iron Man') # Añado un elemento con el metodo append()
avengers.append('Hulk') # Añado un elemento con el metodo append()
avengers.append('Winter Soldier') # Añado un elemento con el metodo append()
# Imprimo la lista creada
print(f" New list {avengers}")

# Inserta un elemento en una posicion en concreto de la lista utilizando el metodo insert(indice, 'nuevo_elemento')
avengers.insert(0, 'Spiderman')
print(avengers)

# Eliminar un elemento de la lista conociendo su posicion/indice con el metodo ->   del lista[posicion]
del avengers[0] # Elimino a Spiderman de la lista
print(avengers)

# Eliminar el ultimo elemento de la lista permitienda trabajar con el, despues de eliminarlo con el metodo -> pop()
popped_final_avenger = avengers.pop() # Elimino el ultimo elemento de la lista y lo guardo en una variable
print(avengers)
print(popped_final_avenger)

# Sacar un elemento de una lista con el metodo pop(indicando_aqui_el_indice_del_elemento)
green_avenger = avengers.pop(1) # Saco el elemento en el indice 1 de la tupla para poder trabajar con el, este elemento
print(green_avenger)            # ya no estara en la tupla, con el metodo "del"el elemento se elimina y con el metodo
                                # pop el elemento se saca de la lista, pero se puede seguir trabajando con el fuera de la lista

# Eliminar un elemento de la lista por "valor"
animals = ["dog", "cat", "lion", "python", "snake"]
print(animals)
animals.remove("cat") # Con el metodo remove(valor) elimino el elemento por valor
print(animals)

too_dangerous = 'lion'
animals.remove(too_dangerous) # Paso la variable con el valor a eliminar
print(animals)
print(f"{too_dangerous.title()} is more dangerous") # Con el metodo remove aun nos permite trabajar con el valor eliminado de la lista

### Lista de invitados ###
famous = ["Messi", "Ronaldo", "Florentino", "Pepe"]
invitation = "do you want to go to my party???"
print(f"{famous[0]}, {invitation}")
print(f"{famous[1]}, {invitation}")
print(f"{famous[2]}, {invitation}")
print(f"{famous[3]}, {invitation}")

### Cambiar la lista de invitados
can_not_attend = 'Messi' # Invitado que no puede asistir
print(f"{can_not_attend} can not attend")
new_guest = 'Antonio' # Invitado que asiste en su lugar
famous.remove(can_not_attend)
famous.insert(0, new_guest) # Añado el nuevo invitado en la posicion en la que estaba el invitado que no va ha asistir
print(famous)
message = 'There are new guests!!'
print(message) # Llegan nuevos invitados
famous.insert(0, "Pele") # Inserto un nuevo invitado al principio de la lista
print(len(famous)) # Compruebo la longitud de la lista con el metodo len()
famous.insert(2, "Romario") # Inserto un nuevo invitado en la mitad de la lista
famous.append("Maradona") # Inserto un invitado al final de la lista
print(f"List of guests: {famous}")

### Reducir la lista de invitados
message = 'I can only invite two guests...'
print(message)
message_sorry = 'Sorry, I cant´t invite you to my party' # Mensaje de disculpa
print(len(famous)) # Compruebo he imprimo la longitud de la lista para saber cuantos elementos contiene
last_guest = famous.pop() # Elimino el ultimo invitado de la lista
print(f"{message_sorry} {last_guest}") # Mensaje de despedida para el invitado
guest_2 = famous.pop(0) # Elimino el primer elemento de la lista
print(f"{message_sorry} {guest_2}")
guest_3 = famous.pop(2) # Elimino el elemento en la posicion 3
print(f"{message_sorry} {guest_3}")
guest_4 = famous.pop(1) # Elimino el elemento el la posicion 2
print(f"{message_sorry} {guest_4}")
guest_5 = famous.pop() # Elimino el elemento en la ultima posicion
print(f"{message_sorry} {guest_5}")
print(famous) # Imprimo los invitados que quedan

message = "continue guest"
print(f"{famous[0].title()} {message}")
print(f"{famous[1].title()} {message}")

### Elimino los ultimos invitados de la lista con el metodo del
del famous[0]
del famous[0]
print("The list contains:")
print(len(famous)) # Compruebo si la lista contiene algun elemento

### Organizar una Lista ###
games = ['soccer', 'basketball', 'tennis', 'golf']
# Ordenar una lista de forma permanente con el metodo sort() en orden alfabetico
print(games) # Imprimo la lista desordenada
games.sort() # Ordeno la lista alfabeticamente
print(games) # Imprimo la lista ordenada alfabeticamente
# Ordenar una lista de forma permanente con el metodo sort() en orden alfabetico inverso
games.sort(reverse = True) # Al pasar por parametro "reverse = True" la lista se ordenara algabeticamente de forma inversa
print(games)

# Con el metodo sorted() ordenamos la lista temporalmente sin modificar el orden real
fruits = ['lemon', 'apple', 'orange', 'watermelon']
print(fruits)
asc_order = sorted(fruits) # Orden alfabetico
print(asc_order)
desc_order = sorted(fruits, reverse= True) # Orden alfabetico inverso
print(desc_order)

print(fruits) # El orden de la lista no a sido modificado

# Invertir el orden de una lista
numbers_ = ['1', '2', '3', '4']
print(numbers_)
numbers_.reverse() # Con el metodo reverse() invertimos el orden de la lista de forma permanente
print(numbers_)
numbers_.reverse() # Si lo volvemos a aplicar se vuelve a invertir el orden de forma permanente
print(numbers_)

### Ver el mundo ###
world = ['Spain', 'USA', 'England', 'Chinese', 'Germany']

print(world)

world_order = sorted(world) # Ordeno la lista temporalmente en orden alfabetico
print(world_order) # Imprimo la lista ordenada
print(world) # Imprimo la lista en el orden originaL

world_des_order = sorted(world, reverse = True) # Ordeno la lista de forma inversa sin cambiar el orden original
print(world_des_order)
print(world) # Compruebo que sigue el orden original de la lista

world.reverse() # Cambio de forma permanente el orden ha inverso
print(world)

world.reverse() # Vuelvo el cambiar el orden de forma permanente al original volviendo a invertir el orden
print(world)

world.sort() # Ordeno la lista alfabeticamente de forma permanente
print(world)

world.sort(reverse = True) # Ordeno la lista alfabeticamente de forma inversa permanentemente
print(world)

