# FeriaFácil: Sistema de Gestión para Mercado Local
---

## 1. Introducción

El comercio en mercados locales y ferias libres constituye una de las actividades económicas más tradicionales y significativas del Ecuador. Ciudades como Quito albergan decenas de mercados tradicionales donde cientos de vendedores atienden diariamente a miles de familias, ofreciendo productos de primera necesidad como frutas, verduras y tubérculos a precios accesibles.

Sin embargo, la forma en que estos negocios operan ha cambiado muy poco en las últimas décadas. La mayoría de vendedores continúa utilizando cuadernos, papeles y cálculos mentales para llevar el control de su inventario y sus ventas, lo cual genera errores frecuentes, pérdida de información y dificultades para conocer la rentabilidad real de su negocio al final del día.

FeriaFácil es un sistema de gestión desarrollado en el lenguaje de programación Python que busca atender esta problemática. Se trata de un software funcional que permite al vendedor registrar su inventario de productos, procesar ventas con cálculo automático de subtotales, recibir alertas cuando un producto está por agotarse, y visualizar un resumen completo de las ventas realizadas durante el día.

Este proyecto integra los conceptos aprendidos durante las cuatro unidades de la asignatura Lógica de Programación, demostrando cómo la tecnología puede transformar procesos cotidianos simples en soluciones digitales accesibles e inmediatamente útiles.

---

## 2. Descripción del Problema

### 2.1 Contexto

En los mercados y ferias libres del Ecuador, los vendedores enfrentan diariamente una serie de desafíos relacionados con la gestión de su negocio. Al no contar con herramientas tecnológicas adecuadas, muchos de ellos experimentan las siguientes dificultades:

- **Control de inventario impreciso:** Sin un registro digital, es difícil saber exactamente cuántas unidades quedan de cada producto, lo que lleva tanto a quedarse sin stock como a desperdiciar producto sobrante.
- **Errores en el cálculo de precios:** Al hacer los cálculos mentalmente o con papel, es frecuente cometer errores al multiplicar cantidades por precios, especialmente cuando hay múltiples clientes esperando.
- **Desconocimiento de las ganancias del día:** Al cierre del día, muchos vendedores no pueden determinar con exactitud cuánto dinero recaudaron ni cuáles fueron sus productos más vendidos.
- **Falta de alertas de reabastecimiento:** Sin un sistema de monitoreo, los vendedores suelen darse cuenta de que un producto se agotó únicamente cuando un cliente lo solicita y ya no hay existencias.

### 2.2 Problema Principal

El problema central es la **ausencia de una herramienta digital accesible** que permita al vendedor de mercado local gestionar su inventario, procesar ventas automáticamente y obtener un resumen de su jornada comercial, sin necesidad de conocimientos tecnológicos avanzados ni de costosos equipos o software especializado.

### 2.3 Solución Propuesta

FeriaFácil resuelve este problema mediante un sistema de consola en Python que, a través de un menú interactivo simple y claro, permite al vendedor:

1. Consultar su inventario en tiempo real
2. Registrar ventas con cálculo automático de subtotales
3. Agregar nuevos productos al sistema
4. Buscar productos específicos
5. Recibir alertas automáticas cuando el stock es bajo
6. Visualizar el resumen y total recaudado del día
7. Conocer las categorías activas de su inventario

---

## 3. Relación con los Contenidos de la Asignatura

FeriaFácil integra de manera práctica y aplicada los conocimientos adquiridos durante las cuatro unidades de la asignatura Lógica de Programación:

### Unidad 1 — Lógica, Algoritmos y Resolución de Problemas

Antes de escribir una sola línea de código, se siguió la metodología de resolución de problemas enseñada en clase: **identificar el problema, comprenderlo, diseñar la solución y luego implementarla**. Se elaboraron los diagramas de casos de uso, flujo y arquitectura para entender el sistema en su totalidad antes de comenzar a programarlo.

El sistema en sí mismo es la aplicación práctica de un algoritmo: un conjunto finito de pasos ordenados y deterministas que, ante cualquier entrada del usuario (opción del menú), produce siempre la misma salida esperada (respuesta coherente del sistema).

### Unidad 2 — Variables, Tipos de Datos, Entrada y Salida

En FeriaFácil se utilizan todos los tipos de datos trabajados en clase:

- **Strings (`str`):** Nombres de productos, categorías, mensajes al usuario
- **Enteros (`int`):** Cantidades de stock, número de ventas, cantidades a vender
- **Flotantes (`float`):** Precios, subtotales, total recaudado, promedios
- **Booleanos (`bool`):** Variable `sistema_activo` para el control del bucle principal, variable `hay_alertas` para el reporte de alertas

Se aplica la conversión de tipos (`int()`, `float()`) sobre los datos ingresados por el usuario con `input()`, dado que Python trata toda entrada como cadena de texto. El módulo `math` se emplea para el cálculo del promedio en el resumen diario. Las f-strings se usan extensamente para dar formato legible y profesional a los mensajes de salida.

### Unidad 3 — Estructuras de Control

El flujo del programa se controla mediante las estructuras aprendidas en clase:

- **Condicionales (`if`, `elif`, `else`):** Presentes en todas las funciones. Se usan para validar entradas del usuario (¿existe el producto?, ¿la cantidad es válida?, ¿hay stock suficiente?), para mostrar alertas de stock bajo y para dirigir al usuario a la función correcta según su elección del menú.
- **Bucle `while`:** Controla el menú principal, mantiendo el sistema activo hasta que el usuario elija la opción de salida (opción `"0"`).
- **Bucle `for`:** Se usa en varias funciones para recorrer el diccionario de inventario (con `.items()`), la lista de ventas del día y el set de categorías.

### Unidad 4 — Estructuras de Datos y Funciones

FeriaFácil hace uso de las cuatro estructuras de datos trabajadas en la última unidad:

| Estructura | Variable | Uso en el sistema |
|---|---|---|
| **Diccionario** | `inventario` | Almacena cada producto con sus datos (precio, stock, categoría). Permite búsqueda eficiente por nombre. |
| **Lista** | `ventas_del_dia` | Registra cronológicamente cada transacción usando `.append()`. Permite recorrer el historial con `for`. |
| **Tupla** | `CATEGORIAS_VALIDAS` | Almacena las categorías del sistema. Al ser inmutable, garantiza que no sean modificadas accidentalmente. |
| **Set** | `categorias_activas` | Identifica automáticamente las categorías únicas en uso, eliminando duplicados gracias a la propiedad del set. |

El código se organiza en **funciones** (`def`), lo cual hace que cada parte del sistema sea independiente, reutilizable y fácil de mantener. Cada función tiene una responsabilidad clara y bien definida, siguiendo los principios del Zen de Python enseñados en clase (explícito es mejor que implícito, simple es mejor que complejo).

---

## 4. Explicación del Sistema Desarrollado

### 4.1 Arquitectura del Sistema

FeriaFácil está organizado en tres capas lógicas:

**Capa de Presentación:** Todo lo que el usuario ve e interactúa. Está formada por el menú principal y los mensajes de confirmación, error e información mostrados con `print()` y formateados con f-strings.

**Capa de Lógica:** Las ocho funciones del sistema (`mostrar_menu`, `mostrar_inventario`, `registrar_venta`, `agregar_producto`, `buscar_producto`, `mostrar_alertas`, `resumen_del_dia`, `ver_categorias`) que implementan la lógica de negocio del vendedor.

**Capa de Datos:** Las estructuras de datos (`inventario`, `ventas_del_dia`, `CATEGORIAS_VALIDAS`, `LIMITE_MINIMO`, `total_recaudado`) que mantienen el estado del sistema durante la ejecución.

### 4.2 Flujo Principal del Sistema

Al ejecutar el programa, el usuario es recibido con un mensaje de bienvenida. A continuación, un bucle `while` mantiene el sistema en ejecución mientras `sistema_activo` sea `True`. En cada iteración, se muestra el menú y se espera la opción del usuario. Una estructura `if/elif/else` determina qué función ejecutar. Al elegir la opción `0`, el sistema muestra el resumen final y cambia `sistema_activo = False`, terminando el bucle y el programa.

### 4.3 Proceso de Registro de Venta

El proceso más importante del sistema es el registro de una venta. Su flujo es:

1. Mostrar el inventario actual como referencia
2. Solicitar el nombre del producto (validar que exista)
3. Mostrar precio y stock disponible del producto
4. Solicitar la cantidad a vender (validar que sea positiva y que haya stock)
5. Calcular el subtotal (precio × cantidad)
6. Descontar la cantidad vendida del stock en el diccionario
7. Crear un registro de la venta y agregarlo a la lista
8. Sumar el subtotal al total recaudado del día
9. Verificar si el stock restante activa una alerta de reabastecimiento

---

## 5. Reflexión sobre el Impacto de la Tecnología

FeriaFácil representa, a pequeña escala, algo que está ocurriendo a nivel global: **la democratización de la tecnología como herramienta para resolver problemas cotidianos**.

En la actualidad, las nuevas tecnologías han transformado sectores enteros de la economía. Las aplicaciones de gestión que antes estaban reservadas para grandes empresas con costosos sistemas ERP, hoy pueden ser construidas con herramientas accesibles y gratuitas como Python, y ejecutadas en cualquier computadora básica o incluso en el navegador a través de Google Colab.

Este proyecto demuestra que no se necesitan años de experiencia ni equipos costosos para comenzar a digitalizar un negocio. Un vendedor de mercado que adopte un sistema como FeriaFácil puede comenzar a tomar decisiones basadas en datos reales: saber exactamente qué productos se venden más, cuándo reabastecer, y cuánto dinero genera cada día.

Desde la perspectiva de la formación como ingenieros de software, este proyecto refuerza una lección fundamental: **la programación no es solo escribir código, es entender problemas reales y diseñar soluciones funcionales**. La capacidad de identificar un problema, modelarlo como algoritmo e implementarlo en código es la habilidad más valiosa que un desarrollador puede tener, independientemente del lenguaje o las herramientas que se usen en el futuro.

El impacto de la tecnología en la sociedad no siempre viene de grandes innovaciones. Muchas veces, el cambio más significativo es el que ayuda a una persona a hacer mejor su trabajo de cada día.
