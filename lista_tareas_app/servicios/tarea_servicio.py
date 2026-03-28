from modelos.tarea import Tarea

class TareaServicio:
    def __init__(self):
        self.__tareas = [] # Aquí guardamos todo en memoria 
        self.__siguiente_id = 1 # Para simular un ID autoincremental de base de datos

    def agregar_tarea(self, descripcion: str) -> Tarea:
        nueva_tarea = Tarea(self.__siguiente_id, descripcion)
        self.__tareas.append(nueva_tarea)
        self.__siguiente_id += 1 # Preparamos el id para la siguiente 
        return nueva_tarea

    def completar_tarea(self, id_tarea: int) -> bool:
        # Buscamos la tarea por id y le cambiamos el estado
        for tarea in self.__tareas:
            if tarea.id == id_tarea:
                tarea.marcar_completada()
                return True
        return False

    def eliminar_tarea(self, id_tarea: int) -> bool:
        # Usamos enumerate para saber el índice exacto y hacer un del
        for i, tarea in enumerate(self.__tareas):
            if tarea.id == id_tarea:
                del self.__tareas[i]
                return True
        return False

    def obtener_tareas(self) -> list[Tarea]:
        # Retorna la lista actual
        return self.__tareas