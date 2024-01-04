from Compra import Compra #Del módulo Compra.py importamos la clase Compra.

#Clase Efectivo:
class Efectivo(Compra):
    #Constructor:
    def __init__(self, id_compra, fecha, hora, puntos_por_litro, litros_comprados, puntos_extra):
        super().__init__(id_compra, fecha, hora, puntos_por_litro, litros_comprados)
        self.__puntos_extra = puntos_extra
        
    #Getter:
    def get_puntos_extra(self):
        return self.__puntos_extra
    
    #Setters:
    def set_puntos_extra(self, nuevos_puntos_extra):
        self.__puntos_extra = nuevos_puntos_extra
    
    #__str__:
    def __str__(self):
        titulo = "Efectivo:\n"
        puntos_extra = f"Puntos extra: {self.__puntos_extra}\n"
        return titulo + super().__str__() + puntos_extra
    
    #Métodos:
    #CU 6:
    def calcular_puntaje_final(self):
         return (self._puntos_por_litro + self.__puntos_extra) * self._litros_comprados