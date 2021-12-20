<div align="center">
  <h1>Programación Dinámica y Estocástica con Python</h1>
</div>

<div align="center"> 
  <img src="img_readme/OIP.jpg" width="500">
</div>

# CONTENIDO
- [OBJETIVOS](#OBJETIVOS)
- [INTRODUCCIÓN](#INTRODUCCIÓN)

# OBJETIVOS
- Aprender cuándo utilizar la Programación Dinámia y en que nos puede beneficiar.
- Diferenciar entre progrmación determinista y estocástica.
- Aprender a utilizar la Programación Estocástica.
- Aprender a crear simulaciones computacionales.

# INTRODUCCIÓN

<div align="center"> 
  <img src="img_readme/Richard_Bellman.jpg" width="200">
  <p>Richard Bellman</p>
</div>

En los años 50s Richard Bellman para poder conseguir financiamiento gubernamental acuño el nombre de 
**Programación Dinámica**, la cual no tenia ninguna relación con las investigaciones en Matemáticas que llevaba acabo.

_'[Nombre] Programación Dinámica se escogió para esconder a patrocinadores gubernamentales el hecho que en realidad estaba haciendo Matemáticas. La frase Programación Dinámica es algo que ningún congresista'_ - Richard Bellman.

La Programación Dinámica es una tecnica poderosa que optimiza ciertos tipos de problemas, ahora bien los problemas que puede optimizar son aquellos que tienen la siguiente estructura:

- **Subestructura Óptima**. Crear una solucion global óptima al conbinar soluciones óptimas de subproblemas locales.

- **Problemas Empalmados**. Se crea una solución óptima para resolver un mismo problema varias veces(problemas que requieren ser repetidos una y otra vez).

Cuando se nos presenta un problema donde su ejecución requiere de resolver el mismo problema varias veces podemos solucionarlo con la **Memoization**(Memorización).

La Memorización(Memoization) evita computos adicionales guardando los resultados de dicho computo en una estructura de datos que podemos consultar posteiormente de una forma rapida.
<h2>
	Caracteristicas de la Memorización
</h2>

- Técnica para guardar compútos previos y evitar realizarlos nuevamente.
- Usamos por lo regular Diccionarios para almacenar los computos, donde las consultas se pueden hacer de una manera rapida.
- Sacrificamos espacio para optimizar el proceso de ejecución.

