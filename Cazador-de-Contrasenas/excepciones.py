"""
excepciones.py
Excepciones personalizadas del proyecto
"""


class ErrorJuego(Exception):
    """Clase base para las excepciones del juego."""
    pass


class LongitudInvalidaError(ErrorJuego):
    """Se genera cuando la longitud de la contraseña es inválida."""

    def __init__(self, mensaje="La longitud debe ser mínimo de 8 caracteres."):
        super().__init__(mensaje)


class DatoInvalidoError(ErrorJuego):
    """Se genera cuando el usuario ingresa un dato incorrecto."""

    def __init__(self, mensaje="Dato ingresado inválido."):
        super().__init__(mensaje)


class ContrasenaInvalidaError(ErrorJuego):
    """Se genera cuando la contraseña no cumple las reglas."""

    def __init__(self, mensaje="La contraseña no cumple los requisitos."):
        super().__init__(mensaje)