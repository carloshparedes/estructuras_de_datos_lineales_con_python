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