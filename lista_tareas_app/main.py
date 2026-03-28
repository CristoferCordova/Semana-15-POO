import tkinter as tk
from servicios.tarea_servicio import TareaServicio
from ui.app_tkinter import AppTkinter

# Punto de entrada de la app
if __name__ == "__main__":
    root = tk.Tk()
    servicio = TareaServicio()
    
    # Le pasamos el root y el servicio a la interfaz para que se comuniquen
    app = AppTkinter(root, servicio)
    
    # Arrancamos el loop de la ventana principal
    root.mainloop()