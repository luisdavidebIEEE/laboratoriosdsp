import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

import numpy as np
import matplotlib.pyplot as plt


class PlantillaGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("LAB DSP")
        self.root.geometry("1000x600")

        self.dark = False

        self.crear_interfaz()


# ================= GUI =================

    def crear_interfaz(self):

        self.root.configure(bg="#f0f0f0")

        # ===== HEADER =====

        header = tk.Frame(self.root, bg="#d9d9d9", height=90)
        header.pack(fill="x")


        # LOGO IZQUIERDO

        try:
            img1 = Image.open("logo_universidad.png")
            img1 = img1.resize((90, 70))
            self.logo1 = ImageTk.PhotoImage(img1)

            tk.Label(header, image=self.logo1,
                     bg="#d9d9d9").pack(side="left", padx=10)

        except:

            tk.Label(header, text="LOGO",
                     bg="white", width=10,
                     height=4).pack(side="left", padx=10)


        # TITULO

        tk.Label(
            header,
            text="Práctica de Laboratorio N° 2. Señales elementales en el tiempo discreto",
            font=("Arial", 14, "bold"),
            bg="#d9d9d9"
        ).pack(side="left", expand=True)


        # LOGO DERECHO

        try:
            img2 = Image.open("logo_programa.png")
            img2 = img2.resize((70, 70))
            self.logo2 = ImageTk.PhotoImage(img2)

            tk.Label(header, image=self.logo2,
                     bg="#d9d9d9").pack(side="right", padx=10)

        except:

            tk.Label(header, text="LOGO",
                     bg="white", width=10,
                     height=4).pack(side="right", padx=10)


        # ===== CENTRO =====

        self.central = tk.Frame(self.root, bg="white")
        self.central.pack(fill="both", expand=True)


        contenedor = tk.Frame(self.central, bg="white")
        contenedor.place(relx=0.5, rely=0.5, anchor="center")


        tk.Label(
            contenedor,
            text="SEÑALES DISCRETAS",
            font=("Arial", 13),
            bg="white"
        ).pack(pady=10)


        señales = tk.Frame(contenedor, bg="white")
        señales.pack()


        tk.Button(señales, text="Senoidal", width=12,
                  command=self.ej31).grid(row=0, column=0, padx=8, pady=5)

        tk.Button(señales, text="Impulso", width=12,
                  command=self.impulso).grid(row=0, column=1, padx=8)

        tk.Button(señales, text="Escalon", width=12,
                  command=self.escalon).grid(row=0, column=2, padx=8)

        tk.Button(señales, text="Suma", width=12,
                  command=self.suma).grid(row=0, column=3, padx=8)

        tk.Button(señales, text="Mult", width=12,
                  command=self.mult).grid(row=1, column=0, padx=8, pady=5)

        tk.Button(señales, text="Despl", width=12,
                  command=self.despl).grid(row=1, column=1, padx=8)

        tk.Button(señales, text="Inv", width=12,
                  command=self.inv).grid(row=1, column=2, padx=8)

        tk.Button(señales, text="Ej 3.8", width=12,
                  command=self.ej38).grid(row=1, column=3, padx=8)


        # ===== BOTONES ABAJO =====

        botones = tk.Frame(self.root, bg="#d9d9d9")
        botones.pack(fill="x")

        tk.Button(botones, text="Ayuda",
                  command=self.ayuda).pack(side="left", padx=5, pady=5)

        tk.Button(botones, text="Créditos",
                  command=self.creditos).pack(side="left", padx=5)

        tk.Button(botones,
                  text="Modo Oscuro / Claro",
                  command=self.modo).pack(side="left", padx=10)

        tk.Button(botones,
                  text="Salir",
                  command=self.root.destroy).pack(side="right", padx=10)


# ================= MODO OSCURO =================

    def modo(self):

        self.dark = not self.dark

        if self.dark:

            self.root.configure(bg="#222")
            self.central.configure(bg="#333")

        else:

            self.root.configure(bg="#f0f0f0")
            self.central.configure(bg="white")


# ================= 3.1 =================

    def ej31(self):

        n = np.arange(0, 21)

        x1 = np.sin(2*np.pi*n)
        x2 = np.sin(0.2*np.pi*n)

        plt.figure()

        plt.subplot(2,1,1)
        plt.stem(n, x1)
        plt.title("x1[n] = sin(2πn)")
        plt.xlabel("n")
        plt.ylabel("Amplitud")
        plt.grid()

        plt.subplot(2,1,2)
        plt.stem(n, x2)
        plt.title("x2[n] = sin(0.2πn)")
        plt.xlabel("n")
        plt.ylabel("Amplitud")
        plt.grid()

        plt.tight_layout()
        plt.show()


# ================= IMPULSO =================

    def impulso(self):

        n = np.arange(-10,11)

        x = np.zeros(len(n))
        x[n==0] = 1

        plt.stem(n,x)
        plt.title("Impulso δ[n]")
        plt.grid()
        plt.show()


# ================= ESCALON =================

    def escalon(self):

        n = np.arange(-10,11)

        x = np.heaviside(n,1)

        plt.stem(n,x)
        plt.title("Escalon u[n]")
        plt.grid()
        plt.show()


# ================= SUMA =================

    def suma(self):

        n = np.arange(0,10)

        x1 = n
        x2 = 2*n
        x = x1 + x2

        plt.figure()

        plt.subplot(3,1,1)
        plt.stem(n,x1)
        plt.title("x1[n]")

        plt.subplot(3,1,2)
        plt.stem(n,x2)
        plt.title("x2[n]")

        plt.subplot(3,1,3)
        plt.stem(n,x)
        plt.title("x1 + x2")

        plt.tight_layout()
        plt.show()


# ================= MULT =================

    def mult(self):

        n = np.arange(0,10)

        x1 = n
        x2 = n
        x = x1*x2

        plt.figure()

        plt.subplot(3,1,1)
        plt.stem(n,x1)

        plt.subplot(3,1,2)
        plt.stem(n,x2)

        plt.subplot(3,1,3)
        plt.stem(n,x)

        plt.tight_layout()
        plt.show()


# ================= DESPL =================

    def despl(self):

        n = np.arange(0,10)
        x = n
        n2 = n-3

        plt.figure()

        plt.subplot(2,1,1)
        plt.stem(n,x)
        plt.title("Original")

        plt.subplot(2,1,2)
        plt.stem(n2,x)
        plt.title("Desplazada")

        plt.tight_layout()
        plt.show()


# ================= INV =================

    def inv(self):

        n = np.arange(-5,6)
        x = n
        n2 = -n

        plt.figure()

        plt.subplot(2,1,1)
        plt.stem(n,x)
        plt.title("Original")

        plt.subplot(2,1,2)
        plt.stem(n2,x)
        plt.title("Invertida")

        plt.tight_layout()
        plt.show()


# ================= 3.8 =================

    def ej38(self):

        n = np.arange(0,21)

        u = np.heaviside(n,1)
        u10 = np.heaviside(n-10,1)
        u20 = np.heaviside(n-20,1)

        x = n*(u-u10) + 10*np.exp(-0.3*(n-10))*(u10-u20)

        plt.stem(n,x)
        plt.title("Ejercicio 3.8")
        plt.grid()
        plt.show()


# ================= OTROS =================

    def ayuda(self):

        messagebox.showinfo("Ayuda","Para visualisar el desarrollo del laboratorio\ndebes dar click en el boton\ncorrespondiente a la funcion que\ndeseas observar")

    def creditos(self):

        messagebox.showinfo("Créditos","Creadores:\n\nluis David Espinel Ballen Cod: 1161513\nCorreo: luisdavideb@ufps.edu.co\n\nFabian Andres Ramirez Sanabria Cod: 1161528\nCorreo: fabianandresrs@ufps.edu.co\n\nDocente: Msc. Sergio Alexander Castro Casadiego\nCorreo: sergio.castroc@ufps.edu.co")


# ================= MAIN =================

if __name__ == "__main__":

    root = tk.Tk()
    app = PlantillaGUI(root)
    root.mainloop()