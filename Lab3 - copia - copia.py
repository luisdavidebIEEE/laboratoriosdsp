import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt

class PlantillaGUI:

    def __init__(self, root):
        self.root = root
        self.modo_oscuro = False

        self.root.title("LABORATORIO 3 - TRANSFORMADA Z")
        self.root.geometry("900x550")

        # 🔥 GRID ROOT
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.crear_interfaz()

    # ==========================
    # TEMA
    # ==========================
    def aplicar_tema(self):
        if self.modo_oscuro:
            self.bg = "#1e1e1e"
            self.panel = "#2d2d2d"
            self.fg = "white"
        else:
            self.bg = "#f0f0f0"
            self.panel = "white"
            self.fg = "black"

        self.root.configure(bg=self.bg)

    # ==========================
    # INTERFAZ
    # ==========================
    def crear_interfaz(self):

        self.aplicar_tema()

        # ===== HEADER =====
        header = tk.Frame(self.root, bg="#d9d9d9", height=80)
        header.grid(row=0, column=0, sticky="ew")

        try:
            img = Image.open("logo_universidad.png").resize((80, 60))
            self.logo_izq = ImageTk.PhotoImage(img)
            tk.Label(header, image=self.logo_izq, bg="#d9d9d9").pack(side="left", padx=20)
        except:
            tk.Label(header, text="UFPS").pack(side="left")

        tk.Label(header, text="LABORATORIO 3, TRANSFORMADA Z",
                 font=("Arial", 14, "bold"), bg="#d9d9d9").pack(side="left", expand=True)

        try:
            img2 = Image.open("logo_programa.png").resize((60, 60))
            self.logo_der = ImageTk.PhotoImage(img2)
            tk.Label(header, image=self.logo_der, bg="#d9d9d9").pack(side="right", padx=20)
        except:
            tk.Label(header, text="PROGRAMA").pack(side="right")

        # ===== CENTRAL =====
        central = tk.Frame(self.root, bg=self.panel)
        central.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        central.grid_rowconfigure(3, weight=1)
        central.grid_columnconfigure(0, weight=1)

        # PARAMETROS
        param = tk.Frame(central, bg=self.panel)
        param.grid(row=0, column=0, pady=5)

        tk.Label(param, text="a=", bg=self.panel, fg=self.fg).grid(row=0, column=0)
        self.a = tk.Entry(param, width=5)
        self.a.insert(0, "0.5")
        self.a.grid(row=0, column=1)

        tk.Label(param, text="w=", bg=self.panel, fg=self.fg).grid(row=0, column=2)
        self.w = tk.Entry(param, width=5)
        self.w.insert(0, "1")
        self.w.grid(row=0, column=3)

        # TEXTO
        self.texto = tk.Text(central, height=8, bg=self.panel, fg=self.fg)
        self.texto.grid(row=1, column=0, sticky="ew", pady=5)

        # BOTONES
        botones = tk.Frame(central, bg=self.panel)
        botones.grid(row=2, column=0, pady=10)

        funciones = [
            ("Escalón", self.escalon),
            ("Impulso", self.impulso),
            ("Rampa", self.rampa),
            ("a^k", self.ak),
            ("Exp", self.exp),
            ("Cos", self.coseno),
            ("Sen", self.seno),
            ("Compuesta", self.compuesta)
        ]

        for t, f in funciones:
            tk.Button(botones, text=t, width=10, command=f).pack(side="left", padx=4)

        # 🔥 ESPACIO DINÁMICO (EL QUE ELIMINA EL HUECO)
        espacio = tk.Frame(central, bg=self.panel)
        espacio.grid(row=3, column=0, sticky="nsew")

        # ===== FOOTER =====
        footer = tk.Frame(self.root, bg="#d9d9d9")
        footer.grid(row=2, column=0, sticky="ew")

        tk.Button(footer, text="🌙 MODO", command=self.toggle_modo).pack(side="left", padx=20)
        tk.Button(footer, text="CRÉDITOS", command=self.creditos).pack(side="left", padx=20)
        tk.Button(footer, text="AYUDA", command=self.ayuda).pack(side="left", padx=20)
        tk.Button(footer, text="SALIR", command=self.salir).pack(side="left", padx=20)

    # ==========================
    # MODO OSCURO
    # ==========================
    def toggle_modo(self):
        self.modo_oscuro = not self.modo_oscuro
        for w in self.root.winfo_children():
            w.destroy()
        self.crear_interfaz()

    # ==========================
    # GRAFICAR
    # ==========================
    def graficar_completo(self, num, den, roc_radio, func):

        plt.style.use('dark_background' if self.modo_oscuro else 'default')

        ceros = np.roots(num)
        polos = np.roots(den)

        fig = plt.figure(figsize=(6, 6))

        ax1 = fig.add_subplot(2,1,1)

        ax1.scatter(np.real(ceros), np.imag(ceros), marker='o', label='Ceros')
        ax1.scatter(np.real(polos), np.imag(polos), marker='x', label='Polos')

        t = np.linspace(0, 2*np.pi, 200)
        ax1.plot(np.cos(t), np.sin(t), '--')

        for r in np.linspace(roc_radio, 2, 30):
            ax1.plot(r*np.cos(t), r*np.sin(t), color='green', alpha=0.05)

        ax1.axhline(0)
        ax1.axvline(0)
        ax1.set_title("Plano Z con ROC")
        ax1.legend()
        ax1.grid()
        ax1.axis('equal')

        ax2 = fig.add_subplot(2,1,2)
        n_vals = np.arange(0, 10)
        y = [func(i) for i in n_vals]

        ax2.stem(n_vals, y)
        ax2.set_title("Señal discreta")
        ax2.grid()

        plt.tight_layout()
        plt.show()

    # ==========================
    # FUNCIONES
    # ==========================
    def mostrar(self, texto):
        self.texto.delete(1.0, tk.END)
        self.texto.insert(tk.END, texto)

    def escalon(self):
        self.mostrar("u(n)\nX(z)=z/(z-1)\nROC: |z|>1")
        self.graficar_completo([1,0],[1,-1],1, lambda n:1)

    def impulso(self):
        self.mostrar("δ(n)\nX(z)=1\nROC: todo el plano")
        self.graficar_completo([1],[1],1, lambda n:1 if n==0 else 0)

    def rampa(self):
        self.mostrar("r(n)=n\nX(z)=z/(z-1)^2\nROC: |z|>1")
        self.graficar_completo([1,0],[1,-2,1],1, lambda n:n)

    def ak(self):
        a = float(self.a.get())
        self.mostrar(f"a^k\nX(z)=z/(z-{a})\nROC: |z|>{a}")
        self.graficar_completo([1,0],[1,-a],a, lambda n:a**n)

    def exp(self):
        a = float(self.a.get())
        val = np.exp(-a)
        self.mostrar(f"e^(-an)\nX(z)=z/(z-{val:.3f})\nROC: |z|>{val:.3f}")
        self.graficar_completo([1,0],[1,-val],val, lambda n:np.exp(-a*n))

    def coseno(self):
        w = float(self.w.get())
        self.mostrar("cos(wk)\nROC: |z|>1")
        self.graficar_completo([1,-np.cos(w),0],[1,-2*np.cos(w),1],1,
                               lambda n:np.cos(w*n))

    def seno(self):
        w = float(self.w.get())
        self.mostrar("sin(wk)\nROC: |z|>1")
        self.graficar_completo([np.sin(w),0],[1,-2*np.cos(w),1],1,
                               lambda n:np.sin(w*n))

    def compuesta(self):
        self.mostrar("x(n)=0.9^n u(n) - 1.1^n u(-n-1)\nROC: 0.9<|z|<1.1")
        self.graficar_completo([1],[1],1.1, lambda n:0.9**n)

    def creditos(self):
        messagebox.showinfo("Créditos","Autores UFPS")

    def ayuda(self):
        messagebox.showinfo("Ayuda","Transformada Z completa")

    def salir(self):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = PlantillaGUI(root)
    root.mainloop()