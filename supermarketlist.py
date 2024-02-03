# Crear una lista vacía para guardar los elementos

lista_compras = []

# Mostrar un menú con las opciones disponibles

def mostrar_menu ():
  print ('Bienvenido a SuperMarketApp')
  print ('opciónes:')
  print ('1. Añadir a la lista')
  print ('2. Eliminar de la lista')
  print ('3. Mostrar lista')
  print ('4. Salir')

# Agregar un elemento a la lista

def agregar_elemento ():
  elemento = input ('Que desea añadir? ')
  lista_compras.append (elemento)
  print ('Se agregó {} a la lista'.format (elemento))

# Eliminar un elemento de la lista

def eliminar_elemento ():
  elemento = input ('Que desea eliminar: ')
  try:
    lista_compras.remove (elemento)
    print ('Se eliminó {} de la lista'.format (elemento))
  except ValueError:
    print ('No está en la lista')

# Mostrar la lista

def mostrar_lista ():
  print ('Su lista de compras es:')
  for i, elemento in enumerate (lista_compras):
    print ('{}. {}'.format (i + 1, elemento))

# Ejecutar el programa

mostrar_menu ()
opcion = int (input ('Ingrese su opción: '))
while opcion != 4:
  if opcion == 1:
    agregar_elemento ()
  elif opcion == 2:
    eliminar_elemento ()
  elif opcion == 3:
    mostrar_lista ()
  else:
    print ('Opción inválida')
  mostrar_menu ()
  opcion = int (input ('Ingrese su opción: '))
print ('Gracias por usar SuperMarketApp')
