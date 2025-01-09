import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class MainView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.carrito = []  # Carrito de compras

        label = ttk.Label(self, text="Bienvenido al Sistema de Ventas", font=("Helvetica", 18))
        label.pack(pady=20)

        categories = [
            ("Nutrición Animal", "AlimentosAgricolasView"),
            ("Comida", "ComidaView"),
        ]

        for category, view_name in categories:
            btn = ttk.Button(self, text=category, bootstyle="primary",
                             command=lambda vn=view_name: controller.mostrar_vista(vn))
            btn.pack(pady=10)
