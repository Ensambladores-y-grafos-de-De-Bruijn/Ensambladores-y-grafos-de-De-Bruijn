# Ensambladores y Gráficas de De Bruijn
## Facultad de Ciencias - UNAM
### Semestre 2022-1

Proyecto final del equipo 1 de [Genómica computacional - Grupo 7099]( https://www.fciencias.unam.mx/docencia/horarios/presentacion/327603 )

## Pre-requisitos :clipboard:

Para poder dibujar las digráficas de De Bruijn es necesario Python 3.6+ y tener el instalado:

- *graphviz*:\
```pip install graphviz```

## Ejecutar el programa :file_folder:

Para poder utilizar el programa de forma interactica basta correr el script con la bandera *-i*:

```
> python -i DeBruijn.py
```

En otro caso simplemente correr
```
> python DeBruijn.py
```

## Introducción

La teoría de gráficas ha sido extremadamente útil para modelar y resolver problemas de la vida real. En especial, existe una clase de gráficas que son muy especial: las gráficas de De Bruijn.

Una gráfica es un conjunto finito no vacío, al que llamamos el conjunto de vértices, y un conjunto de lineas que unen dichos vértices, a las que llamamos aristas.

El matemático holandés Nicolaas de Bruijn para encontrar una secuencia cíclica de letras tomadas de un alfabeto dado para el cual cada palabra posible de cierta longitud de tamaño k aparece como una subcadena de caracteres consecutivos en la secuencia cíclica exactamente una vez utilizó gráficas, las cuáles son llamadas De Debruijn en su nombre. Para esto, se basó en la idea original de Euler y su respuesta al problema de los puentes de Konigsberg: el paseo euleriano. Un paseo euleriano es aquel que pasa por cada una de las aristas deuna gráfica sin usar más de una vez ninguna arista, si el vértice inicial y final coinciden, le llamamos paseo euleriano cerrado. Aunque este problema parezca ser muy teórico, puede ser usado para resolver una basta cantidad de problemas. En especial, el problema que a nosotros concierne: el ensamblaje del genóma.

Usando gráficas de De Bruijn es posible reconstruir genomas dadas las lecturas que se hagan a una secuencia. Por ejemplo [IDBA](https://github.com/loneknightpy/idba) es ensamblador que usa gráficas de De Bruijn para lecturas de secuenciación.

## Objetivos
- Comprender la base teórica sobre las gráficas de De Bruijn.

- Escrbir un programa que implemente las gráficas de De Bruijn usando el algoritmo básico que estas utilizan.

- Comprender el ensamblador [IDBA](https://github.com/loneknightpy/idba).

- Aprender a usar dicho ensamblador.

## Diagrama Metodológico

<p align="center">
  <img src="figures/Diagrama.png" />
</p>

El link si lo quieren editar [aquí](https://drive.google.com/file/d/1is4nNsdQQ7tbTNOh7B3rVVUc1i9vO9cV/view?usp=sharing)

## Conclusiones

Se investigó y profundizó sobre teoría de gráficas y sus aplicaciones al ensamblaje de genomas. Se aplicaron los conocimientos de programación adquiridos en el curso para la implementación del algoritmo básico que usan las gráficas de De Bruijn.

## Referencias
- Compeau, P. E. C. (2011, 8 noviembre). How to apply de Bruijn graphs to genome assembly. Nature. https://www.nature.com/articles/nbt.2023?error=cookies_not_supported&code=c5e20b2b-ee43-43b0-81e0-4f35d99a74b8

- IDBA-Bioinfomatics Research Group of Hong Kong University. (s. f.). Bioinfomatics Research Group Computer Science, The University of Hong Kong. Recuperado 1 de febrero de 2021, de https://i.cs.hku.hk/%7Ealse/hkubrg/projects/idba/

- Ben Langmead. (2015, 7 mayo). VER LISTA DE REPRODUCCIÓN COMPLETA 55 REPRODUCIENDO Algorithms for DNA Sequencing. Algorithms for DNA Sequencing. Recuperado 1 de febrero de 2022, de https://www.youtube.com/watch?v=hpb-mH-yjLc&list=PL2mpR0RYFQsBiCWVJSvVAO3OJ2t7DzoHA

## Autores :busts_in_silhouette:

-  []() (Marco Cruz Maya)

-  [axelprestegui]( https://github.com/axelprestegui) (K. Axel Prestegui Ramos)

-  [anapaurv]( https://github.com/anapaurv ) (Ana Paula Rubio Vargas)

-  [samuelruizperez]( https://github.com/VianeyAileen ) (Samuel Ruiz Pérez)