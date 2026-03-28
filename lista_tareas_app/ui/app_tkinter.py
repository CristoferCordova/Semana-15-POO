import tkinter as tk
from tkinter import messagebox
from servicios.tarea_servicio import TareaServicio

class AppTkinter:
    def __init__(self, root: tk.Tk, servicio: TareaServicio):
        self.__root = root
        self.__servicio = servicio
        self.__root.title("To-Do List")

        # Frame superior para el input y el botón de añadir
        self.__frame_entrada = tk.Frame(self.__root)
        self.__frame_entrada.pack(pady=10)

        self.__entry_tarea = tk.Entry(self.__frame_entrada, width=40)
        self.__entry_tarea.pack(side=tk.LEFT, padx=5)
        # Bindeamos la tecla Enter para que llame a la función de agregar más rápido
        self.__entry_tarea.bind("<Return>", self.__evento_agregar_tarea) 

        self.__btn_agregar = tk.Button(self.__frame_entrada, text="Añadir Tarea", command=self.__agregar_tarea)
        self.__btn_agregar.pack(side=tk.LEFT)

        # Usamos Listbox porque es más sencillo para este caso, pero Treeview también servía
        self.__listbox_tareas = tk.Listbox(self.__root, width=50, height=15)
        self.__listbox_tareas.pack(pady=10)
        # Doble clic para marcar como hecha sin tener que ir al botón
        self.__listbox_tareas.bind("<Double-1>", self.__evento_completar_tarea) 

        # Frame inferior para los botones de acción
        self.__frame_botones = tk.Frame(self.__root)
        self.__frame_botones.pack(pady=5)

        self.__btn_completar = tk.Button(self.__frame_botones, text="Marcar Completada", command=self.__completar_tarea)
        self.__btn_completar.pack(side=tk.LEFT, padx=5)

        self.__btn_eliminar = tk.Button(self.__frame_botones, text="Eliminar", command=self.__eliminar_tarea)
        self.__btn_eliminar.pack(side=tk.LEFT, padx=5)

        # Cargamos la lista al iniciar por si acaso
        self.__actualizar_lista()

    # Wrappers para los eventos de teclado y ratón (necesitan recibir el parámetro 'event')
    def __evento_agregar_tarea(self, event):
        self.__agregar_tarea()

    def __evento_completar_tarea(self, event):
        self.__completar_tarea()

    def __agregar_tarea(self):
        descripcion = self.__entry_tarea.get().strip()
        if descripcion:
            self.__servicio.agregar_tarea(descripcion)
            self.__entry_tarea.delete(0, tk.END) # Limpiamos el input
            self.__actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "No puedes agregar una tarea vacía.")

    def __completar_tarea(self):
        seleccion = self.__listbox_tareas.curselection()
        if seleccion:
            index = seleccion[0]
            # Obtenemos la tarea real desde la capa de servicios 
            tarea = self.__servicio.obtener_tareas()[index]
            self.__servicio.completar_tarea(tarea.id)
            self.__actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Primero selecciona una tarea de la lista.")

    def __eliminar_tarea(self):
        seleccion = self.__listbox_tareas.curselection()
        if seleccion:
            index = seleccion[0]
            tarea = self.__servicio.obtener_tareas()[index]
            self.__servicio.eliminar_tarea(tarea.id)
            self.__actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Selecciona qué quieres eliminar.")

    def __actualizar_lista(self):
        # Borramos todo visualmente y lo volvemos a pintar
        self.__listbox_tareas.delete(0, tk.END)
        for tarea in self.__servicio.obtener_tareas():
            texto = tarea.descripcion
            if tarea.estado_completado:
                texto += " [Hecho]" # Feedback visual
                self.__listbox_tareas.insert(tk.END, texto)
                self.__listbox_tareas.itemconfig(tk.END, {'fg': 'gray'}) # La ponemos en gris
            else:
                self.__listbox_tareas.insert(tk.END, texto)
                self.__listbox_tareas.itemconfig(tk.END, {'fg': 'black'})