import tkinter as tk
from dotenv import load_dotenv
import os

load_dotenv()

app_user = os.getenv("APP_USER")
app_password = os.getenv("APP_PASSWORD")

ventana = tk.Tk()
ventana.title("Validación de credenciales")
ventana.geometry("400x350")

ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)

label = tk.Label(
    ventana,
    text="LOGIN",
    font=("Calibri", 15, "bold"),
    fg="black"
)
label.grid(row=0, column=0, columnspan=2, pady=15)


label_usuario = tk.Label(ventana, text="Usuario")
label_usuario.grid(row=1, column=0, padx=10, pady=8, sticky="e")

entry_usuario = tk.Entry(ventana)
entry_usuario.grid(row=1, column=1, padx=10, pady=8, sticky="w")


label_password = tk.Label(ventana, text="Contraseña")
label_password.grid(row=2, column=0, padx=10, pady=8, sticky="e")

entry_password = tk.Entry(ventana, show="*")
entry_password.grid(row=2, column=1, padx=10, pady=8, sticky="w")


def capturar_credenciales():
    usuario = entry_usuario.get()
    contrasena = entry_password.get()
    validar_credenciales(usuario, contrasena)


def validar_credenciales(usuario, contrasena):
    if usuario == app_user and contrasena == app_password:
        mostrar_mensaje(True)
    else:
        mostrar_mensaje(False)


def mostrar_mensaje(acceso):
    if acceso:
        label_mensaje.config(
            text="Acceso correcto",
            fg="green"
        )
    else:
        label_mensaje.config(
            text="Usuario o contraseña incorrectos",
            fg="red"
        )

boton = tk.Button(
    ventana,
    text="Iniciar sesión",
    bg="black",
    fg="white",
    pady=2,
    padx=23,
    command=capturar_credenciales
)
boton.grid(row=3, column=0, columnspan=2, pady=15)


label_mensaje = tk.Label(ventana, text="")
label_mensaje.grid(row=4, column=0, columnspan=2, padx=10, pady=8)

ventana.mainloop()
