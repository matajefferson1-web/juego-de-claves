"""
cofre.py
Clase que representa los cofres del juego.
"""

import random


class Cofre:

    def __init__(self, tipo, puntos):
        self.tipo = tipo
        self.puntos = puntos

    @staticmethod
    def crear_cofre(valido):
        """
        Si la contraseña es inválida devuelve un cofre maldito.
        Si es válida devuelve un cofre aleatorio.
        """

        if not valido:
            return Cofre("Maldito", -20)

        cofres = [
            Cofre("Común", 10),
            Cofre("Raro", 25),
            Cofre("Legendario", 50)
        ]

        return random.choice(cofres) 