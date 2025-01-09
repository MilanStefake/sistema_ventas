import ttkbootstrap as ttk
from views.main_view import MainView
from views.alimentos_agricolas import AlimentosAgricolasView
from views.comida import ComidaView  # Vista de comida
from views.finalizar_compra import FinalizarCompraView


class VentanaPrincipal(ttk.Window):
    def __init__(self):
        super().__init__(themename="darkly")
        self.title("Sistema de Ventas")
        self.geometry("1920x1080")
        
        self.frames = {}
        self.carrito = []  # Lista para almacenar los productos en el carrito
        self.crear_vistas()
        self.mostrar_vista("MainView")

    def crear_vistas(self):
        # Crear las vistas y asignar la referencia del carrito
        self.frames["MainView"] = MainView(self, self)
        self.frames["AlimentosAgricolasView"] = AlimentosAgricolasView(self, self)
        self.frames["ComidaView"] = ComidaView(self, self)
        self.frames["FinalizarCompraView"] = FinalizarCompraView(self, self, self.carrito)  # Pasar el carrito
        for frame in self.frames.values():
            frame.pack(fill="both", expand=True)

    def mostrar_vista(self, nombre_vista):
        """Mostrar una vista específica."""
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[nombre_vista].pack(fill="both", expand=True)




def main():
    app = VentanaPrincipal()
    app.mainloop()

if __name__ == "__main__":
    main()