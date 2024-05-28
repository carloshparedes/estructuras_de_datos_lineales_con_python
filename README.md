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