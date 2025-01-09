import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import json

class AlimentosAgricolasView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        factor = 1.35

        # Crear un canvas para el desplazamiento
        self.canvas = ttk.Canvas(self)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Crear un frame dentro del canvas para contener los productos
        self.frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        # Configurar el canvas y la scrollbar en la ventana principal utilizando grid
        self.canvas.grid(row=0, column=0, padx=int(50 * factor), pady=int(50 * factor), sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        # Configurar el frame para que tenga el tamaño adecuado
        self.frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # Título
        label = ttk.Label(self.frame, text="Alimento De Animales", font=("Helvetica", int(16 * factor)))
        label.grid(row=0, column=0, pady=(int(20 * factor), int(10 * factor)), columnspan=3)

        # Cargar productos desde el archivo JSON
        productos = self.cargar_productos()

        # Crear botones dinámicos para cada producto
        for i, producto in enumerate(productos):
            nombre = producto["nombreProducto"]
            precio = producto["precio"]
            btn_text = f"{nombre} {precio}"

            # Crear el botón con el mismo color de fondo que los del MainView
            btn = ttk.Button(self.frame, text=btn_text, bootstyle="primary", width=int(30 * factor))

            # Organizar los botones en 3 columnas
            row = (i // 3) + 1  # Calculamos la fila
            column = i % 3  # Columna 0, 1, o 2

            # Colocar el botón en la posición calculada
            btn.grid(row=row, column=column, pady=int(5 * factor), padx=int(20 * factor), sticky="nsew")

        # Crear un Frame para contener el botón "Volver"
        back_frame = ttk.Frame(self)
        back_frame.grid(row=1, column=0, pady=int(10 * factor), sticky="nsew")

        # Botón para volver a la vista principal fuera de la grid
        back_btn = ttk.Button(back_frame, text="Volver", bootstyle="secondary", width=int(15 * factor),
                              command=lambda: controller.mostrar_vista("MainView"))
        back_btn.grid(row=0, column=0, pady=int(10 * factor), padx=int(20 * factor))

        # Asegurarse de que los botones se expandan para llenar la ventana
        self.frame.grid_rowconfigure(0, weight=0)  # Fila del título
        self.frame.grid_rowconfigure(len(productos) // 3 + 1, weight=0)  # Fila del botón de 'Volver'

        # Configuración para las filas de los botones
        for i in range(len(productos) // 3 + 1):
            self.frame.grid_rowconfigure(i + 1, weight=1)  # Expande las filas de los botones

        # Configuración de columnas para que los botones se distribuyan uniformemente
        for i in range(3):  # Tres columnas
            self.frame.grid_columnconfigure(i, weight=1)

        # Configuración de la ventana principal para que todo esté centrado
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Establecer la geometría de la ventana para que sea flexible
        self.master.state('normal')  # Asegurarse de que la ventana esté en modo ventana
        self.master.attributes('-fullscreen', True)  # Activar pantalla completa con bordes
        self.master.geometry("1920x1080")  # Establecer un tamaño predeterminado de ventana (ajustable)
        self.master.resizable(True, True)  # Hacer la ventana redimensionablecle

    def cargar_productos(self):
        """Cargar productos desde un archivo JSON"""
        try:
            with open("productos_agricolas.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception as e:
            print(f"Error al cargar productos: {e}")
            return []
