class Tarea:
    def __init__(self, id_tarea: int, descripcion: str):
        # Usamos doble guion bajo para hacerlos privados (encapsulamiento real)
        self.__id = id_tarea
        self.__descripcion = descripcion
        self.__estado_completado = False

    # Getters usando el decorador property para acceder a los datos de forma segura
    @property
    def id(self) -> int:
        return self.__id

    @property
    def descripcion(self) -> str:
        return self.__descripcion

    @property
    def estado_completado(self) -> bool:
        return self.__estado_completado

    # Solo permitimos marcar como completada, no desmarcar por ahora
    def marcar_completada(self):
        self.__estado_completado = True