from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import sqlite3

root = Tk()
root.title("Registro")
root.config(bg="white")

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300,height=300)
root.geometry('310x460')
root.resizable(False,False) 

#Empezar barra
bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar")
bbddMenu.add_command(label="Salir")

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos")

CrudMenu = Menu(barraMenu, tearoff=0)
CrudMenu.add_command(label="Crear")
CrudMenu.add_command(label="Leer")
CrudMenu.add_command(label="Editar")
CrudMenu.add_command(label="Eliminar")

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de")

barraMenu.add_cascade(label="Archivo", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=CrudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#------ Mini Dashboard -----

FrameCabez = Frame(root)
FrameCabez.pack()

titulo = Label(FrameCabez, text="500\nTotal Usuarios",bg="SeaGreen3",fg="white",padx=100,pady=10,justify=CENTER)
titulo.grid(row=0,column=0,sticky=E)

#----- Empezar campos -----
miFrame=Frame(root)
miFrame.config(bg="white")
miFrame.pack()

cuadroId = Entry(miFrame)
cuadroId.grid(row=0,column=1,padx=10,pady=10)
cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=1,column=1,padx=10,pady=10)
cuadroPassword = Entry(miFrame)
cuadroPassword.grid(row=2,column=1,padx=10,pady=10)
cuadroPassword.config(show="*")
cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=3,column=1,padx=10,pady=10)
cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=4,column=1,padx=10,pady=10)

cuadroComentario = Text(miFrame, width=16,height=5)
cuadroComentario.grid(row=5,column=1,pady=10)

scrollVert=Scrollbar(miFrame,command=cuadroComentario.yview)
scrollVert.grid(row=5,column=1,pady=10,sticky="nse")
cuadroComentario.config(yscrollcommand=scrollVert.set)

idLabel = Label(miFrame, text="Id:",bg="white")
idLabel.grid(row=0,column=0,sticky="w",pady=10,padx=10)
idLabel = Label(miFrame, text="Nombre:",bg="white")
idLabel.grid(row=1,column=0,sticky="w",pady=10,padx=10)
idLabel = Label(miFrame, text="Password:",bg="white")
idLabel.grid(row=2,column=0,sticky="w",pady=10,padx=10)
idLabel = Label(miFrame, text="Apellido:",bg="white")
idLabel.grid(row=3,column=0,sticky="w",pady=10,padx=10)
idLabel = Label(miFrame, text="Direccion:",bg="white")
idLabel.grid(row=4,column=0,sticky="w",pady=10,padx=10)
idLabel = Label(miFrame, text="Comentarios:",bg="white")
idLabel.grid(row=5,column=0,sticky="w",pady=10,padx=10)


#Empezar botones
miFrame1=Frame(root)
miFrame1.pack()


root.mainloop()