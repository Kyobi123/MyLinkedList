from mylinkedlist import LinkedList

# Crear una LinkedList
lista = LinkedList()

# Agregar elementos
lista.append(10)
lista.append(20)
lista.append(30)

print("Lista inicial:", lista)

# Insertar al inicio
lista.prepend(5)
print("Después de prepend:", lista)

# Buscar elemento
print("Buscando 20:", lista.find(20))

# Eliminar elemento
lista.delete(10)
print("Después de eliminar 10:", lista)