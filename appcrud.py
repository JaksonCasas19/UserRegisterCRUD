from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import sqlite3


#---- Funciones -----

def conexionBBDD():
	miConexion = sqlite3.connect("Usuarios")
	miCursor = miConexion.cursor()

	try:
		miCursor.execute('''
			CREATE TABLE DatosUsuarios(
			Id integer PRIMARY KEY AUTOINCREMENT,
			Nombre_Usuario varchar(50),
			Password varchar(50),
			Apellido varchar(50),
			Direccion varchar(50),
			Comentarios varchar(100)
			)
			''')
		messagebox.showinfo("BBDD","¡BBDD creada con éxito!")
	except:
		messagebox.showwarning("¡Atención!","La BBDD ya existe")

def salirAplicacion():
	valor = messagebox.askquestion("Salir","¿Deseas salir de la aplicación?")
	if(valor == "yes"):
		root.destroy()

#Resetear campos
def limpiarCampos():
	miId.set("")
	miNombre.set("")
	miPass.set("")
	miApellido.set("")
	miDireccion.set("")
	cuadroComentario.delete(1.0,END)

def crear():
	miConexion=sqlite3.connect("Usuarios")
	miCursor = miConexion.cursor()

	miCursor.execute("INSERT INTO DatosUsuarios values(NULL,'"+miNombre.get()+
		"','"+miPass.get()+
		"','"+miApellido.get()+
		"','"+miDireccion.get()+
		"','"+cuadroComentario.get("1.0",END)+"')")

	miConexion.commit()
	messagebox.showinfo("BBDD","¡Registro insertado con éxito!")

def leer():
	miConexion=sqlite3.connect("Usuarios")
	miCursor = miConexion.cursor()
	miCursor.execute("SELECT * FROM DatosUsuarios where Id="+miId.get())

	elUsuario = miCursor.fetchall()

	for usuario in elUsuario:
		miId.set(usuario[0])
		miNombre.set(usuario[1])
		miPass.set(usuario[2])
		miApellido.set(usuario[3])
		miDireccion.set(usuario[4])
		cuadroComentario.insert(1.0,usuario[5])

	miConexion.commit()

def actualizar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor = miConexion.cursor()
	miCursor.execute("UPDATE DatosUsuarios SET Nombre_Usuario='"+miNombre.get()+"',Password='"+miPass.get()+"',Apellido='"+miApellido.get()+
		"',Direccion='"+miDireccion.get()+"',Comentarios='"+cuadroComentario.get(1.0,END)+"'WHERE Id="+miId.get())

	miConexion.commit()
	messagebox.showinfo("BBDD","¡Registro actualizado con éxito!")

root = Tk()
root.title("Registro")
root.config(bg="white")

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300,height=300)
root.geometry('310x480')
root.resizable(False,False) 

#Empezar barra
bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir",command=salirAplicacion)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)

CrudMenu = Menu(barraMenu, tearoff=0)
CrudMenu.add_command(label="Crear",command=crear)
CrudMenu.add_command(label="Leer",command=leer)
CrudMenu.add_command(label="Editar",command=actualizar)
CrudMenu.add_command(label="Eliminar")

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de")

barraMenu.add_cascade(label="Archivo", menu=bbddMenu)
barraMenu.add_cascade(label="Limpiar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=CrudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#------ Mini Dashboard -----

FrameCabez = Frame(root)
FrameCabez.pack()


miConexion2=sqlite3.connect("Usuarios")
miCursor2 = miConexion2.cursor()
num = miCursor2.execute("SELECT COUNT(Id) FROM DatosUsuarios")
ok = str(num.fetchone())
miConexion2.commit()


titulo = Label(FrameCabez, text=f"{ok[1]}\nTotal Usuarios",bg="SeaGreen3",fg="white",padx=100,pady=10,justify=CENTER)
titulo.grid(row=0,column=0,sticky=E)

#----- Empezar campos -----
miFrame=Frame(root)
miFrame.config(bg="white")
miFrame.pack()

miId = StringVar()
miNombre = StringVar()
miApellido = StringVar()
miPass = StringVar()
miDireccion =StringVar()


cuadroId = Entry(miFrame,textvariable=miId)
cuadroId.grid(row=0,column=1,padx=10,pady=10)
cuadroId.config(justify="right")
cuadroNombre = Entry(miFrame,textvariable=miNombre)
cuadroNombre.grid(row=1,column=1,padx=10,pady=10)
cuadroPassword = Entry(miFrame,textvariable=miPass)
cuadroPassword.grid(row=2,column=1,padx=10,pady=10)
cuadroPassword.config(show="*")
cuadroApellido = Entry(miFrame,textvariable=miApellido)
cuadroApellido.grid(row=3,column=1,padx=10,pady=10)
cuadroDireccion = Entry(miFrame,textvariable=miDireccion)
cuadroDireccion.grid(row=4,column=1,padx=10,pady=10)

cuadroComentario = Text(miFrame, width=16,height=5)
cuadroComentario.grid(row=5,column=1,pady=10)

scrollVert=Scrollbar(miFrame,command=cuadroComentario.yview)
scrollVert.grid(row=5,column=1,pady=10,sticky="nse")
cuadroComentario.config(yscrollcommand=scrollVert.set)

idLabel = Label(miFrame, text="Id:",bg="white")
idLabel.grid(row=0,column=0,sticky="e",pady=10,padx=10)
nombreLabel = Label(miFrame, text="Nombre:",bg="white")
nombreLabel.grid(row=1,column=0,sticky="e",pady=10,padx=10)
passwordLabel = Label(miFrame, text="Password:",bg="white")
passwordLabel.grid(row=2,column=0,sticky="e",pady=10,padx=10)
apellidoLabel = Label(miFrame, text="Apellido:",bg="white")
apellidoLabel.grid(row=3,column=0,sticky="e",pady=10,padx=10)
direccionLabel = Label(miFrame, text="Direccion:",bg="white")
direccionLabel.grid(row=4,column=0,sticky="e",pady=10,padx=10)
comentarioLabel = Label(miFrame, text="Comentarios:",bg="white")
comentarioLabel.grid(row=5,column=0,sticky="e",pady=10,padx=10)


#Empezar botones
miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Crear",bd=0,bg="dodger blue",fg="white",command=crear)
botonCrear.grid(row=1,column=0,sticky="e",padx=10,pady=10)

botonLeer=Button(miFrame2, text="Leer",bd=0,bg="SeaGreen3",fg="white",command=leer)
botonLeer.grid(row=1,column=1,sticky="e",padx=10,pady=10)

botonActualizar=Button(miFrame2, text="Actualizar",bd=0,bg="goldenrod1",fg="white",command=actualizar)
botonActualizar.grid(row=1,column=2,sticky="e",padx=10,pady=10)

botonEliminar=Button(miFrame2, text="Eliminar",bd=0,bg="firebrick1",fg="white")
botonEliminar.grid(row=1,column=3,sticky="e",padx=10,pady=10)

root.mainloop()