import tkinter as Tk 

def suma ():
    n1 = int(entry_n1.get()) 
    n2 = int(entry_n2.get())
    resultado=n1+n2
    label_resultado.config(text="resultado: " + str(resultado))
def resta ():
    n1 = int(entry_n1.get()) 
    n2 = int(entry_n2.get())
    resultado=n1-n2
    label_resultado.config(text="resultado: " + str(resultado))
def multiplicacion ():
    n1 = int(entry_n1.get()) 
    n2 = int(entry_n2.get())
    resultado=n1*n2
    label_resultado.config(text="resultado: " + str(resultado))
def division ():
    n1 = int(entry_n1.get()) 
    n2 = int(entry_n2.get())
    resultado= n1/n2
    label_resultado.config(text="resultado: " + str(resultado))

app = Tk. Tk()
app.title("Tecnologico de estudios Superiores")

label_n1=Tk.Label(text="primer numero")
entry_n1=Tk.Entry()

label_n2=Tk.Label(text="segundo numero")
entry_n2=Tk.Entry()

label_resultado = Tk.Label(text= "****")
botton_suma=Tk.Button(text= "sumar" , command=suma)
label_espacio=Tk.Label(text="        ")
botton_resta=Tk.Button(text="restar" , command=resta)
label_espacio1=Tk.Label(text="       ")
botton_multiplicacion=Tk.Button(text="multiplicar" , command=multiplicacion)
label_espacio2=Tk.Label(text="             ")
botton_division=Tk.Button(text="division" , command=division)

label_n1.pack()
entry_n1.pack()

label_n2.pack()
entry_n2.pack()

label_resultado.pack()
botton_suma.pack()
label_resultado.pack()
label_espacio.pack()
botton_resta.pack()
label_resultado.pack()
label_espacio2.pack()
botton_multiplicacion.pack()
label_resultado.pack()
label_espacio1.pack()
botton_division.pack()
label_resultado.pack()

 


app.geometry("500x600")
app.mainloop()

