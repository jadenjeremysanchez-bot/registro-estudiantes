import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.title("Sistema de Registro de Estudiantes")
ventana.geometry("900x600")

estudiantes = []

marco_datos = tk.LabelFrame(
    ventana,
    text="Datos del estudiante",
    padx=10,
    pady=10
)
marco_datos.place(x=20, y=20, width=300, height=400)

tk.Label(marco_datos, text="Nombre:").pack(anchor="w")
entrada_nombre = tk.Entry(marco_datos)
entrada_nombre.pack(fill="x", pady=5)

tk.Label(marco_datos, text="Edad:").pack(anchor="w")
entrada_edad = tk.Entry(marco_datos)
entrada_edad.pack(fill="x", pady=5)

tk.Label(marco_datos, text="Curso:").pack(anchor="w")

combo_curso = ttk.Combobox(
    marco_datos,
    values=[
        "Matemáticas",
        "Lenguaje",
        "Ciencias",
        "Inglés",
        "Historia",
        "Computación"
    ]
)
combo_curso.pack(fill="x", pady=5)

tk.Label(marco_datos, text="Nota:").pack(anchor="w")
entrada_nota = tk.Entry(marco_datos)
entrada_nota.pack(fill="x", pady=5)

def guardar():

    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    curso = combo_curso.get()
    nota = entrada_nota.get()

    if nombre == "" or edad == "" or curso == "" or nota == "":
        messagebox.showwarning(
            "Aviso",
            "Completa todos los campos"
        )
        return

    estudiantes.append(
        [nombre, edad, curso, nota]
    )

    mostrar()

    messagebox.showinfo(
        "Información",
        "Estudiante guardado correctamente"
    )


def mostrar():

    for fila in tabla.get_children():
        tabla.delete(fila)

    for i, estudiante in enumerate(estudiantes, 1):

        tabla.insert(
            "",
            "end",
            values=(
                i,
                estudiante[0],
                estudiante[1],
                estudiante[2],
                estudiante[3]
            )
        )


def eliminar():

    seleccionado = tabla.selection()

    if seleccionado:

        fila = tabla.item(
            seleccionado[0]
        )

        numero = int(
            fila["values"][0]
        )

        estudiantes.pop(numero - 1)

        mostrar()

        messagebox.showinfo(
            "Información",
            "Estudiante eliminado"
        )

    else:
        messagebox.showwarning(
            "Aviso",
            "Selecciona un estudiante"
        )


def limpiar():

    entrada_nombre.delete(0, tk.END)
    entrada_edad.delete(0, tk.END)
    combo_curso.set("")
    entrada_nota.delete(0, tk.END)

tk.Button(
    marco_datos,
    text="Guardar",
    command=guardar,
    bg="green",
    fg="white"
).pack(fill="x", pady=5)

tk.Button(
    marco_datos,
    text="Mostrar",
    command=mostrar,
    bg="blue",
    fg="white"
).pack(fill="x", pady=5)

tk.Button(
    marco_datos,
    text="Eliminar",
    command=eliminar,
    bg="red",
    fg="white"
).pack(fill="x", pady=5)

tk.Button(
    marco_datos,
    text="Limpiar",
    command=limpiar,
    bg="gray",
    fg="white"
).pack(fill="x", pady=5)

marco_lista = tk.LabelFrame(
    ventana,
    text="Lista de estudiantes",
    padx=10,
    pady=10
)

marco_lista.place(
    x=340,
    y=20,
    width=530,
    height=400
)

tabla = ttk.Treeview(
    marco_lista,
    columns=(
        "ID",
        "Nombre",
        "Edad",
        "Curso",
        "Nota"
    ),
    show="headings"
)

tabla.heading("ID", text="ID")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Edad", text="Edad")
tabla.heading("Curso", text="Curso")
tabla.heading("Nota", text="Nota")

tabla.column("ID", width=40)
tabla.column("Nombre", width=130)
tabla.column("Edad", width=60)
tabla.column("Curso", width=130)
tabla.column("Nota", width=60)

tabla.pack(
    fill="both",
    expand=True
)

marco_buscar = tk.LabelFrame(
    ventana,
    text="Buscar estudiante",
    padx=10,
    pady=10
)

marco_buscar.place(
    x=340,
    y=440,
    width=530,
    height=90
)

entrada_buscar = tk.Entry(
    marco_buscar
)

entrada_buscar.pack(
    side="left",
    fill="x",
    expand=True
)


def buscar():

    texto = entrada_buscar.get().lower()

    for fila in tabla.get_children():
        tabla.delete(fila)

    for i, estudiante in enumerate(estudiantes, 1):

        if texto in estudiante[0].lower():

            tabla.insert(
                "",
                "end",
                values=(
                    i,
                    estudiante[0],
                    estudiante[1],
                    estudiante[2],
                    estudiante[3]
                )
            )


tk.Button(
    marco_buscar,
    text="Buscar",
    command=buscar,
    bg="orange"
).pack(side="right", padx=5)


ventana.mainloop()