import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class FinalizarCompraView(ttk.Frame):
    def __init__(self, parent, controller, carrito):
        super().__init__(parent)

        # Mostrar el título
        label = ttk.Label(self, text="Finalizar Compra", font=("Helvetica", 18))
        label.pack(pady=20)

        # Crear un frame para mostrar los productos
        productos_frame = ttk.Frame(self)
        productos_frame.pack(pady=10)

        # Mostrar los productos del carrito
        total = 0
        for i, producto in enumerate(carrito):
            nombre = producto["nombreProducto"]
            precio = producto["precio"]
            total += precio
            producto_label = ttk.Label(productos_frame, text=f"{nombre} - ${precio}", font=("Helvetica", 14))
            producto_label.grid(row=i, column=0, pady=5)

        # Mostrar el total de la compra
        total_label = ttk.Label(self, text=f"Total: ${total}", font=("Helvetica", 16, "bold"))
        total_label.pack(pady=20)

        # Botón de volver
        back_btn = ttk.Button(self, text="Volver", bootstyle="secondary", width=20, 
                              command=lambda: controller.mostrar_vista("AlimentosAgricolasView"))
        back_btn.pack(pady=10)

        # Botón de confirmar compra
        confirm_btn = ttk.Button(self, text="Confirmar Compra", bootstyle="success", width=20)
        confirm_btn.pack(pady=10)