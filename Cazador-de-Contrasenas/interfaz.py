"""
interfaz.py
Interfaz gráfica del juego.
"""

import tkinter as tk
from tkinter import messagebox

from juego import JuegoCazador
from excepciones import (
    LongitudInvalidaError,
    DatoInvalidoError,
    ContrasenaInvalidaError
)


class InterfazJuego:

    def __init__(self):

        self.juego = JuegoCazador()

        self.ventana = tk.Tk()
        self.ventana.title("Cazador de Contraseñas")
        self.ventana.geometry("550x600")
        self.ventana.resizable(False, False)

        self.crear_interfaz()

    def crear_interfaz(self):

        tk.Label(
            self.ventana,
            text="CAZADOR DE CONTRASEÑAS",
            font=("Arial", 18, "bold")
        ).pack(pady=15)

        self.lbl_puntos = tk.Label(
            self.ventana,
            text="Puntos acumulados: 0",
            font=("Arial", 12)
        )
        self.lbl_puntos.pack()

        tk.Label(
            self.ventana,
            text="Nombre del jugador"
        ).pack(pady=5)

        self.nombre = tk.Entry(self.ventana, width=30)
        self.nombre.pack()

        tk.Label(
            self.ventana,
            text="Longitud de la contraseña (mínimo 8)"
        ).pack(pady=5)

        self.longitud = tk.Entry(self.ventana, width=10)
        self.longitud.pack()

        tk.Button(
            self.ventana,
            text="Iniciar juego",
            bg="green",
            fg="white",
            width=20,
            command=self.jugar
        ).pack(pady=15)

        tk.Button(
            self.ventana,
            text="Salir",
            bg="red",
            fg="white",
            width=20,
            command=self.salir
        ).pack()

        self.lbl_password = tk.Label(self.ventana, text="")
        self.lbl_password.pack(pady=15)

        self.lbl_cofre = tk.Label(self.ventana, text="")
        self.lbl_cofre.pack()

        self.lbl_estado = tk.Label(self.ventana, text="")
        self.lbl_estado.pack(pady=15)

    def jugar(self):

        try:

            nombre = self.nombre.get().strip()

            dato = self.longitud.get().strip()

            if not dato.isdigit():
                raise DatoInvalidoError(
                    "La longitud debe ser un número."
                )

            password, cofre = self.juego.jugar(
                nombre,
                int(dato)
            )

            self.lbl_password.config(
                text=f"Contraseña:\n{password}"
            )

            self.lbl_cofre.config(
                text=f"Cofre obtenido: {cofre.tipo}"
            )

            self.lbl_estado.config(
                text=f"Puntos +{cofre.puntos}",
                fg="blue"
            )

            self.lbl_puntos.config(
                text=f"Puntos acumulados: {self.juego.puntos}"
            )

            continuar = messagebox.askyesno(
                "Continuar",
                "¿Desea generar otra contraseña?"
            )

            if not continuar:
                self.salir()

        except (
            LongitudInvalidaError,
            DatoInvalidoError,
            ContrasenaInvalidaError
        ) as error:

            cofre = self.juego.penalizar()

            self.lbl_password.config(
                text="Contraseña inválida"
            )

            self.lbl_cofre.config(
                text="Cofre obtenido: Maldito"
            )

            self.lbl_estado.config(
                text=f"{error}\n{cofre.puntos} puntos",
                fg="red"
            )

            self.lbl_puntos.config(
                text=f"Puntos acumulados: {self.juego.puntos}"
            )

            messagebox.showerror(
                "Error",
                str(error)
            )

    def salir(self):

        messagebox.showinfo(
            "Resumen",
            self.juego.resumen()
        )

        self.ventana.destroy()

    def ejecutar(self):

        self.ventana.mainloop()