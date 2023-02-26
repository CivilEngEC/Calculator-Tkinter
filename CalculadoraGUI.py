#Caluladora con Tkiner
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox
import re

class Calculadora():
    def __init__(self, master):
        self.ui = master
        self.ui.title("Calculadora")
        self.ui.resizable(0,0)
        self.ui.geometry("300x400")
        self.frame = ttk.Frame(self.ui)
        self.frame.pack(fill="both", expand=True)
        #Entradas y resultados
        self.entrada = tk.StringVar()
        self.Labelentradas =  ttk.Label(self.frame, width=40, textvariable=self.entrada)
        self.Labelentradas.grid(row=0, column=0, columnspan=4)
        self.resultado = tk.StringVar()
        self.Labelresultado = ttk.Label(self.frame, width=40, textvariable=self.resultado)
        self.Labelresultado.grid(row=1, column=0, columnspan=4)
        #Botones
        self.botones = ["+","-","*","/",
                        "7", "8", "9", "**",
                        "4", "5", "6", "=", 
                        "1", "2", "3", "C", 
                        "0", ".", "DEL", "CE"]
        self.buttons = {}
        for i, boton in enumerate(self.botones):
            self.buttons[boton] = ttk.Button(self.frame, text=boton)
            self.buttons[boton].grid(row=i//4+2, column=i%4)
            if boton == "=":
                self.buttons[boton].config(command=self.evaluar)
                self.ui.bind(boton, self.evaluar)
            elif boton == "DEL":
                self.buttons[boton].config(command=lambda:self.entrada.set(self.entrada.get()[:-1]))
            elif boton == "C":
                self.buttons[boton].config(command=lambda:self.entrada.set(""))
            elif boton == "CE":
                self.buttons[boton].config(command=lambda:(self.entrada.set(""), self.resultado.set("")))
            else:
                self.buttons[boton].config(command=self.agregar)
                if boton == "**":
                    self.ui.bind("^", self.agregar)
                else:
                    self.ui.bind(boton, self.agregar)
                
        #CalculoAuxiliar
        self.frameText = ttk.Frame(self.ui)
        self.frameText.pack(fill="both", expand=True)
        self.CalculoAuxiliar = tk.StringVar()
        self.TextCalculoAuxiliar = tk.Text(self.frameText, width=70, height=40)  
        self.TextCalculoAuxiliar.pack(fill="both", expand=True)
        self.TextCalculoAuxiliar.insert(tk.END, "Calculo Auxiliar")
        self.TextCalculoAuxiliar["state"] = "disabled"

    def agregar(self, event=None):
        if event:
            entry = event.char
        else:
            entry = self.ui.focus_get()["text"]
        if entry  == "^":
            entry = "**"
        symbols = ["+", "-", "*", "/", "**"]
        try:
            last = self.entrada.get()[-1]
        except IndexError:
            last = ""
        if entry in symbols and last in symbols:
            pass
        else:
            self.entrada.set(self.entrada.get() + entry)
        last = self.entrada.get()[-1]
        if last in symbols:
            pass
        else:
            try:
                self.resultado.set(str(eval(self.entrada.get())))
            except Exception as e:
                self.resultado.set("Error")
        
    def evaluar(self, event=None):
        if event:
            entry = event.char
        else:
            entry = self.ui.focus_get()["text"]
        try:
            self.TextCalculoAuxiliar["state"] = "normal"
            self.TextCalculoAuxiliar.insert(tk.END, "\n"+self.entrada.get()+entry+self.resultado.get())
            self.TextCalculoAuxiliar["state"] = "disabled"
            self.entrada.set(self.resultado.get())
        except Exception as e:
            self.resultado.set("Error")

        

        
        

if __name__ == "__main__":
    
    app = Calculadora(tk.Tk())
    app.ui.mainloop()