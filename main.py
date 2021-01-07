"""
Creador: Hernán Araya
Fecha: 7/01/2021
Programa para Calcular el Indice de Masa Corporal
"""
from tkinter import *
from tkinter import messagebox


# Funcion para calcular el IMC
def Calculo_IMC():

    if (entry_peso.get() == "" and entry_estatura.get() == "") or\
            (entry_peso.get() == "" or entry_estatura.get() == ""):
        messagebox.showerror(title="Error de ingreso de datos",
                             message="Los campos estan vacios o ingreso un dato incorrecto")

    if entry_peso.get() != "" and entry_estatura.get() != "":
        peso = float(entry_peso.get())
        estatura = float(entry_estatura.get())
        imc = peso / (estatura * estatura)

        if imc <= 18.49:
            messagebox.showinfo(title="Por debajo del peso",
                                message="Debe cuidar su salud ya que esta por debajo del promedio")

        elif 18.5 <= imc <= 24.9:
            messagebox.showinfo(title="Saludable",
                                message="Usted es una persona muy saludable, su IMC se encuentra entre el promedio")

        elif 25 <= imc <= 29.9:
            messagebox.showinfo(title="Con sobrepeso",
                                message="Debe cuidar su salud ya que tiene sobrepeso y puede afectarle")

        elif 30 <= imc <= 39.9:
            messagebox.showinfo(title="Obeso",
                                message="Debe mejorar su salud ya que tiene problemas de obesidad")

        elif imc >= 40:
            messagebox.showinfo(title="Obesidad extrema o de alto riesgo",
                                message="Su salud esta en peligro, por favor consulte a un profesional que le ayude")

    entry_peso.delete(0, END)
    entry_estatura.delete(0, END)


window = Tk()
window.title("Calcula tu Indice de Masa Corporal")
window.iconbitmap("iconhealth.ico")
window.geometry("550x550")
window.config(bg="lightblue")
window.resizable(0, 0)

bg_imagen = PhotoImage(file=r"C:\Users\hl586\OneDrive\Escritorio\Python\Proyecto#1\bg.png")

canvas1 = Canvas(window, width=500, height=500)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg_imagen, anchor="nw")

# Etiqueta del Peso
label_peso = Label(window, text="Peso",  font=('Arial', 45))
entry_peso = Entry(window, font=('Arial', 45))
entry_peso.place(x=325, y=15, width=180, height=100)
labelPeso_Canva = canvas1.create_window(30, 25, anchor='nw', window=label_peso)

# Etiqueta de la Estatura
label_estatura = Label(window, text="Estatura", font=('Arial', 45))
labelEstatura_Canva = canvas1.create_window(30, 200, anchor='nw', window=label_estatura)
entry_estatura = Entry(window, font=('Arial', 45))
entry_estatura.place(x=325, y=185, width=180, height=100)

# Boton para calcular el IMC
boton_IMC = Button(window, text='Calcular IMC', font=('Arial', 20), command=Calculo_IMC)
botonIMC_Canva = canvas1.create_window(165, 400, anchor='nw', window=boton_IMC)


window.mainloop()
