# Proyecto-Minicomputadora

## Integrantes:
* Sebastián Jiménez Arrieta
* Franco Acuña Córdoba
* Esteban Malavasi Zúñiga
* Joan Barquero Calderón
* Javier Picado Hernández

# Minicomputadora

Proyecto desarrollado en Lucia.

## Requisitos

Antes de ejecutar el proyecto, asegúrese de tener instalado:

- Lucia Compiler 1.0.0 o superior

Verificar instalación:

- lucia --version

## Cómo ejecutar el proyecto:

* git clone https://github.com/AskingManCode/TC1-Minicomputadora.git

* cd TC1-Minicomputadora

* Ejecutar lucia main.lucia

## Funcionalidades implementadas

* mostrarBienvenida(): da la bienvenida al programa y permite al usuario escoger en cuál categoría de juego (actividad) desea desarrollar.
* mostrarDespedida(): muestra al usuario un mensaje de despedidad del programa.
* Menús: menús para escoger una opción (actividad) por cada una de las categorías.
* leerOpcion(minimo : int, maximo : int) : int {}: en main.lucia, captura de opción (actividad) escogida y la debida validación.
* generarNumero(): en la clase Numeros, la función permite generar un número aleatorio.
* JugarAdivinaNumero(): en la clase Numeros, función que permite ejecutar el juego cuya función lleva su nombre.
* OrdenaLosNumeros(): en la clase Numeros, función que permite ejecutar el juego cuya función lleva su nombre.
* MayorYMenor(): en la clase Numeros, función que permite ejecutar el juego cuya función lleva su nombre.
* getListaLetras(): en la clase Letras, retorna una lista con todas las letras del dicccionario.
* getListaPalabras(): en la clase Letras, retorna una lista con todas las palabras del diccionario.
* getPalabra(): en la clase Letras, retorna una palabra buscando por llave.
* getPalabraRandom(): en la clase Letras, retorna una palabra cualquiera del diccionario.
* quitarLetraRandom(palabra: string): en la clase Letras, función auxiliar que devuelve una lista con una palabra y la letra que le falta.
* JugarBosqueLetras(): en la clase Letras, función que permite ejecutar el juego cuya función lleva su nombre.
* JugarCompletaPalabra(): en la clase Letras, función que permite ejecutar el juego cuya función lleva su nombre.
* JugarLetraIntrusa(): en la clase Letras, función que permite ejecutar el juego cuya función lleva su nombre.
* JugarCualSobra(): en la clase Lógica, función que permite ejecutar el juego cuya función lleva su nombre.
* queGrande():  en la clase Juegos, función que permite ejecutar el juego cuya función lleva su nombre.

En este proyecto se aplicó el uso de clases, funciones, estructuras de control y repetición, generación de números aleatorios.

## Diagrama de Clases
<img width="1536" height="1024" alt="Diagrama de Minicomputadoras" src="https://github.com/user-attachments/assets/536f45e9-a415-4797-99df-97a6fcff3b24" />

## Diagrama de Casos de Uso
<img width="1440" height="1960" alt="image" src="https://github.com/user-attachments/assets/c13ff5e5-099e-4a9e-8db7-3f14a03177d0" />


## Mejoras para una versión 2.0
- Agregar sistema de puntuación global
- Guardar puntuaciones en archivo
- Dificultad variable (fácil, medio, difícil)
- Más rondas en cada juego
- Juegos multijugador
- Ranking de mejores puntuaciones
- Más categorías de juegos
