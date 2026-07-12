# ==========================================================
# CAZADOR DE CONTRASEÑAS
# Juego interactivo con Tkinter + Programación Orientada a Objetos
# ==========================================================

import tkinter as tk
from tkinter import messagebox
import random
import string



# EXCEPCIONES PERSONALIZADAS


class LongitudInvalidaError(Exception):
    pass


class DatoInvalidoError(Exception):
    pass


class ContrasenaInvalidaError(Exception):
    pass


# CLASE CONTRASEÑA


class Contrasena:

    caracteres_especiales = "¿¡?=)(/¨*+-%&$#!"

    def __init__(self, longitud):
        self.longitud = longitud
        self.password = ""

    def generar(self):

        if self.longitud < 8:
            raise LongitudInvalidaError("La contraseña debe tener mínimo 8 caracteres.")

        caracteres = ( string.ascii_uppercase +string.ascii_lowercase +string.digits +self.caracteres_especiales)

        if self.longitud > len(set(caracteres)):
            raise LongitudInvalidaError("La longitud es demasiado grande.")

        while True:

            lista = random.sample(caracteres,self.longitud)

            random.shuffle(lista)

            self.password = "".join(lista)

            if self.validar():
                return self.password


    def validar(self):

        if len(set(self.password)) != len(self.password):
            return False

        if not any(letra.isupper()for letra in self.password):
            return False

        if not any(letra.islower()for letra in self.password):
            return False

        if not any(numero.isdigit()for numero in self.password):
            return False

        if not any(caracter in self.caracteres_especiales for caracter in self.password):
            return False

        return True




# CLASE COFRE


class Cofre:

    def __init__(self, tipo, puntos):

        self.tipo = tipo
        self.puntos = puntos


    @staticmethod
    def crear_cofre(valido):

        if not valido:

            return Cofre("Maldito",-20)


        cofres = [Cofre("Común", 10),Cofre("Raro",25),Cofre("Legendario",50)]


        return random.choice(cofres)



# CLASE JUEGO CAZADOR


class JuegoCazador:


    def __init__(self):

        self.nombre = ""

        self.puntos = 0

        self.historial = {"Común":0,"Raro":0,"Legendario":0,"Maldito":0}


        self.ventana = tk.Tk()

        self.ventana.title("Cazador de Contraseñas")

        self.ventana.geometry("550x600")

        self.ventana.resizable(False,False)


        self.crear_interfaz()



    
    # CREAR INTERFAZ
    

    def crear_interfaz(self):


        titulo = tk.Label(self.ventana,text="CAZADOR DE CONTRASEÑAS",font=("Arial",18,"bold"))

        titulo.pack(pady=15)


        self.lbl_puntos = tk.Label(self.ventana,text="Puntos acumulados: 0",font=("Arial",12))

        self.lbl_puntos.pack()



        tk.Label(self.ventana,text="Nombre del jugador").pack(pady=5)


        self.nombre_entry = tk.Entry(self.ventana,width=30)

        self.nombre_entry.pack()



        tk.Label(self.ventana,text="Longitud contraseña (mínimo 8)").pack(pady=5)


        self.longitud_entry = tk.Entry(self.ventana,width=10)

        self.longitud_entry.pack()



        self.btn_jugar = tk.Button(self.ventana,text="Iniciar juego",bg="green",fg="white",width=20,command=self.jugar)

        self.btn_jugar.pack(pady=15)



        self.btn_salir = tk.Button(self.ventana,text="Salir",bg="red",fg="white",width=20,command=self.finalizar)

        self.btn_salir.pack()



        self.lbl_password = tk.Label(self.ventana,text="Contraseña generada:")

        self.lbl_password.pack(pady=15)



        self.lbl_cofre = tk.Label(self.ventana,text="Cofre obtenido:")

        self.lbl_cofre.pack()



        self.lbl_mensaje = tk.Label(self.ventana,text="")

        self.lbl_mensaje.pack(pady=15)




    # MÉTODO JUGAR
   

    def jugar(self):

        try:

            self.nombre = self.nombre_entry.get().strip()


            if self.nombre == "":

                raise DatoInvalidoError("Debe escribir el nombre del jugador.")


            dato_longitud = self.longitud_entry.get().strip()


            if not dato_longitud.isdigit():

                raise DatoInvalidoError("La longitud debe ser un número.")


            longitud = int(dato_longitud)


            # Crear generador de contraseña

            generador = Contrasena(longitud)


            password = generador.generar()


            valida = generador.validar()



            if not valida:

                raise ContrasenaInvalidaError("La contraseña no cumple los requisitos.")



            # Cofre aleatorio

            cofre = Cofre.crear_cofre(True)



        except (LongitudInvalidaError,DatoInvalidoError,ContrasenaInvalidaError) as error:


            # Cofre maldito por error

            cofre = Cofre.crear_cofre(False)


            self.puntos += cofre.puntos


            self.historial["Maldito"] += 1



            self.lbl_password.config(text="Contraseña generada: INVÁLIDA")


            self.lbl_cofre.config(text="Cofre obtenido: Maldito")


            self.lbl_mensaje.config(text=f"{error}\nPuntos: {cofre.puntos}",fg="red")


            self.actualizar_puntos()


            return




        
        # CONTRASEÑA CORRECTA
   


        self.puntos += cofre.puntos


        self.historial[cofre.tipo] += 1



        self.lbl_password.config(text=f"Contraseña generada:\n{password}")


        self.lbl_cofre.config(text=f"Cofre obtenido: {cofre.tipo}")


        self.lbl_mensaje.config(text=f"Puntos obtenidos: +{cofre.puntos}",fg="blue")


        self.actualizar_puntos()



        continuar = messagebox.askyesno("Continuar","¿Desea generar otra contraseña?")


        if not continuar:

            self.finalizar()




    # ACTUALIZAR PUNTAJE
   

    def actualizar_puntos(self):

        self.lbl_puntos.config(text=f"Puntos acumulados: {self.puntos}")




    # RESUMEN FINAL
  

    def finalizar(self):


        total = sum(self.historial.values())


        resumen = (

            "========= RESUMEN DEL JUEGO =========\n\n"

            f"Jugador: {self.nombre}\n\n"

            f"Puntaje final: {self.puntos}\n\n"

            f"Cofres abiertos: {total}\n\n"

            f"Cofres Comunes: "
            f"{self.historial['Común']}\n"

            f"Cofres Raros: "
            f"{self.historial['Raro']}\n"

            f"Cofres Legendarios: "
            f"{self.historial['Legendario']}\n"

            f"Cofres Malditos: "
            f"{self.historial['Maldito']}"

        )


        messagebox.showinfo("Resumen final",resumen)


        self.ventana.destroy()




   
    # EJECUTAR APLICACIÓN
   

    def ejecutar(self):

        self.ventana.mainloop()





# INICIO DEL PROGRAMA


if __name__ == "__main__":

    juego = JuegoCazador()

    juego.ejecutar() 