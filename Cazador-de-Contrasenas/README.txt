=========================================
CAZADOR DE CONTRASEÑAS
=========================================

Autor:
Jefferson Matabanchoy

Descripción:
-------------
Cazador de Contraseñas es un juego desarrollado en Python utilizando
Programación Orientada a Objetos (POO) y la librería Tkinter para la
interfaz gráfica.

El jugador debe ingresar su nombre y la longitud de una contraseña.
El sistema genera una contraseña aleatoria que cumple con las siguientes
reglas:

- Mínimo 8 caracteres.
- Al menos una letra mayúscula.
- Al menos una letra minúscula.
- Al menos un número.
- Al menos un carácter especial.
- No se permiten caracteres repetidos.

Si la contraseña es válida, el jugador obtiene un cofre aleatorio
(Común, Raro o Legendario) con una cantidad de puntos.

Si ocurre un error de validación, el jugador recibe un Cofre Maldito
que resta puntos.

=========================================
ESTRUCTURA DEL PROYECTO
=========================================

Cazador-de-Contrasenas/

│── main.py
│── interfaz.py
│── juego.py
│── cofre.py
│── contraseña.py
│── excepciones.py
│── README.txt

=========================================
REQUISITOS
=========================================

- Python 3.10 o superior.

No requiere instalar librerías externas.

=========================================
EJECUCIÓN
=========================================

Abrir una terminal en la carpeta del proyecto y ejecutar:

python main.py

=========================================
FUNCIONALIDADES
=========================================

✓ Generación aleatoria de contraseñas.
✓ Validación automática.
✓ Manejo de excepciones personalizadas.
✓ Sistema de puntuación.
✓ Cofres aleatorios.
✓ Interfaz gráfica con Tkinter.
✓ Resumen final del juego.

=========================================
FIN
=========================================