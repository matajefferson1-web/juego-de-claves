"""
contraseña.py
Clase encargada de generar y validar contraseñas.
"""

import random
import string

from excepciones import LongitudInvalidaError


class Contrasena:

    CARACTERES_ESPECIALES = "¿¡?=)(/¨*+-%&$#!"

    def __init__(self, longitud):
        self.longitud = longitud
        self.password = ""

    def generar(self):

        if self.longitud < 8:
            raise LongitudInvalidaError(
                "La contraseña debe tener mínimo 8 caracteres."
            )

        caracteres = (
            string.ascii_uppercase +
            string.ascii_lowercase +
            string.digits +
            self.CARACTERES_ESPECIALES
        )

        if self.longitud > len(set(caracteres)):
            raise LongitudInvalidaError(
                "La longitud es demasiado grande."
            )

        while True:

            lista = random.sample(caracteres, self.longitud)

            random.shuffle(lista)

            self.password = "".join(lista)

            if self.validar():
                return self.password

    def validar(self):

        if len(set(self.password)) != len(self.password):
            return False

        if not any(c.isupper() for c in self.password):
            return False

        if not any(c.islower() for c in self.password):
            return False

        if not any(c.isdigit() for c in self.password):
            return False

        if not any(c in self.CARACTERES_ESPECIALES for c in self.password):
            return False

        return True