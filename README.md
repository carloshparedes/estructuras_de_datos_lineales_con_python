# Suma Piramidal

Este script de Python, `pyramid_sum.py`, contiene una función recursiva `pyramid_sum(lower, upper, margin=0)` que calcula la suma de los enteros desde `lower` hasta `upper`.

## Parámetros de la Función

- `lower`: El límite inferior del rango de enteros a sumar.
- `upper`: El límite superior del rango de enteros a sumar.
- `margin` (opcional): Este parámetro se utiliza para formatear la salida impresa y no forma parte del cálculo de la suma. Por defecto es 0.

## Cómo Funciona

La función funciona llamándose a sí misma recursivamente, incrementando el valor de `lower` en 1 y el de `margin` en 4 cada vez, hasta que `lower` es mayor que `upper`. En este punto, la función devuelve 0, terminando la recursión. La suma de los enteros se calcula sumando `lower` al resultado de la llamada recursiva.

## Salida

La función imprime los valores actuales de `lower` y `upper`, así como la suma actual, cada vez que se llama. El parámetro `margin` se utiliza para indentar la salida, creando una representación visual de la profundidad de la recursión.

## Ejemplo

Ejecutar el script ejecutará la siguiente línea de código:

```python
print(pyramid_sum(1, 10))

1 10
---- 2 10
-------- 3 10
------------ 4 10
---------------- 5 10
-------------------- 6 10
------------------------ 7 10
---------------------------- 8 10
-------------------------------- 9 10
------------------------------------ 10 10
---------------------------------------- 11 10
---------------------------------------- 0
------------------------------------ 10
-------------------------------- 19
---------------------------- 27
------------------------ 34
-------------------- 40
---------------- 45
------------ 49
-------- 52
---- 54
55
55
```
## Colecciones Incorporadas en Python

- **Listas**: Propósito general, de índices con tamaños dinámicos. Ordenables `lista =[]`.
  - Usaría las listas para almacenar una serie de números, una lista de palabras, y básicamente cualquier cosa.

- **Tuplas**: Inmutables, no se pueden añadir más elementos. Útiles para constantes por ejemplo coordenadas, direcciones. Es de tipo secuencial. `tupla =()`.
  - Las usaría cuando sé exactamente el tamaño que tendrán mis datos.

- **Conjuntos**: Almacenan objetos no duplicados (Teoría de conjuntos), son de acceso rápido, aceptan operaciones lógicas, son desordenados. `set() conjunto={1,2,3,4}`.
  - Usaría un casteo entre conjuntos y listas cuando quiero eliminar duplicados de una lista.

- **Diccionarios**: Pares de llave-valor, arrays asociativos (hash maps), son desordenados, y muy rápidos para hacer consultas. `diccionario ={'Llave':"Valor"}`.
  - Los usaría para almacenar datos, listas, objetos que perfectamente pueden volverse un dataframe, o un defaultdict.

## Consideraciones sobre el uso de Colecciones en Python

Es crucial entender cuándo es más apropiado utilizar una colección específica en Python, ya que esto puede afectar tanto el espacio en memoria que ocupa como la eficiencia de ciertas operaciones. Como regla general, se recomienda optar por tuplas en lugar de listas cuando los valores no necesiten ser modificados, ya que las tuplas ocupan menos espacio en memoria. De igual manera, los sets o diccionarios son preferibles para la búsqueda de elementos debido a su mayor velocidad.

Este es un fragmento de código que muestra el tamaño en memoria de las diferentes estructuras de datos en Python:

```python
import sys

collections = {"list": list(), "tuple": tuple(), "dict": dict(), "set": set()}

for name, collection in collections.items():
    print(f'{name} = {sys.getsizeof(collection)} bytes')
```
Resultados:

    list = 56 bytes
    tuple = 40 bytes
    dict = 232 bytes
    set = 216 bytes

## Arrays

Un array es una estructura de datos lineal que representa una colección de elementos. Cada elemento en el array se almacena en una posición específica, conocida como índice. Los arrays son fundamentales en la programación debido a su eficiencia y facilidad de uso. Aquí hay algunos términos clave relacionados con los arrays:

- **Elemento**: Es el valor que se almacena en una posición específica dentro del array.
- **Índice**: Es la referencia numérica a la posición de un elemento en el array. En la mayoría de los lenguajes de programación, los índices de los arrays comienzan en 0, lo que significa que el primer elemento del array se encuentra en el índice 0.

## Almacenamiento y Uso de Arrays

En la memoria, los arrays se almacenan de manera consecutiva, con cada elemento ocupando una posición contigua. Esto permite un acceso rápido a los elementos del array, pero también impone algunas restricciones.

Un array tiene una capacidad de almacenamiento definida en el momento de su creación. Esta capacidad no puede ser modificada posteriormente, lo que significa que no se pueden agregar ni eliminar posiciones una vez que el array ha sido creado.

Los arrays pueden tener una, dos o tres dimensiones. Sin embargo, a medida que aumenta la dimensión del array, se vuelve más complicado acceder a los datos. Por esta razón, en Python se recomienda trabajar con arrays de menos de dos dimensiones.

Es importante destacar que, aunque los arrays son un tipo de lista en Python, las listas no son arrays. Los arrays tienen restricciones adicionales y solo pueden almacenar números y caracteres.

Los arrays se utilizan en diversas aplicaciones, como los sprites en los videojuegos o los menús de opciones. A pesar de las funciones limitadas del módulo `array` en Python, es posible crear arrays personalizados para satisfacer necesidades específicas.

## Clase Array Personalizada

La clase `Array` es una implementación personalizada de un array en Python. Esta clase proporciona varias funcionalidades, incluyendo la capacidad de iterar sobre los elementos del array, acceder a elementos individuales y modificar elementos.

Aquí está la descripción de los métodos de la clase `Array`:

- `__init__(self, capacity, fill_value=None)`: Este método inicializa un nuevo array con una capacidad dada, llenando cada posición con un valor de relleno.

- `__len__(self)`: Este método devuelve la longitud del array.

- `__str__(self)`: Este método devuelve una representación en cadena del array.

- `__iter__(self)`: Este método devuelve un iterador para el array, lo que permite iterar sobre los elementos del array.

- `__getitem__(self, index)`: Este método permite acceder a un elemento del array en una posición específica.

- `__setitem__(self, index, new_item)`: Este método permite modificar el valor de un elemento en una posición específica del array.

Aquí hay un ejemplo de cómo usar la clase `Array`:

```python
my_array = Array(4, 'Hola')
print(my_array, len(my_array), str(my_array), iter(my_array), my_array[0], my_array[1], my_array[2], my_array[3], sep='\n')
```
Print

    ['Hola', 'Hola', 'Hola', 'Hola']
    4
    ['Hola', 'Hola', 'Hola', 'Hola']
    <list_iterator object at 0x7f8f7452b2b0>
    Hola
    Hola
    Hola
    Hola

# Proyecto de Nodos y Procesos

Este proyecto es una demostración simple de cómo se pueden usar los nodos para representar una cadena de procesos. Cada nodo representa un proceso individual y el atributo `next` de cada nodo apunta al siguiente proceso en la cadena.

## Código

El código principal se encuentra en el archivo `node.py`. Aquí está una descripción de lo que hace cada parte del código:

```python
# Create the nodes (processes)
process1 = Node("Start")
process2 = Node("Load data")
process3 = Node("Process data")
process4 = Node("Save results")
process5 = Node("End")
```

Esto crea cinco nodos, cada uno representando un proceso individual en la cadena de procesos.

```python
# Link the nodes
process1.next = process2
process2.next = process3
process3.next = process4
process4.next = process5
```
Esto enlaza los nodos juntos en una cadena. El atributo next de cada nodo apunta al siguiente nodo en la cadena.

```python
# Print the process chain
current_node = process1
while current_node is not None:
    print(current_node.data)
    current_node = current_node.next
```
Esto imprime cada proceso en la cadena en orden. Comienza con el primer nodo y sigue los enlaces next hasta que llega al final de la cadena.

```python
# Terminal
------------------------------
Start
Load data
Process data
Save results
End
------------------------------
```  
Este proyecto es una forma simple pero efectiva de demostrar cómo se pueden usar los nodos para representar una cadena de procesos. Puede ser útil para entender conceptos como las listas enlazadas y las estructuras de datos basadas en nodos.