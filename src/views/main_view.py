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

        # Botón Finalizar Compra (inicialmente deshabilitado)
        self.finalizar_btn = ttk.Button(self, text="Finalizar Compra", bootstyle="success", state="disabled",
                                        command=self.finalizar_compra)
        self.finalizar_btn.pack(pady=10)

    def agregar_al_carrito(self, producto):
        """Agregar producto al carrito y habilitar el botón 'Finalizar Compra'."""
        self.carrito.append(producto)
        self.finalizar_btn.config(state="normal")  # Habilitar el botón de finalizar compra
        print(f"Producto agregado al carrito: {producto['nombreProducto']}")

    def finalizar_compra(self):
        """Mostrar la vista de finalizar compra."""
        self.controller.mostrar_vista("FinalizarCompraView")