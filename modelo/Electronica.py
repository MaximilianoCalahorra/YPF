from Compra import Compra #Del módulo Compra.py importamos la clase Compra.

#Clase Electronica:
class Electronica(Compra):
    #Constructor:
    def __init__(self, id_compra, fecha, hora, puntos_por_litro, litros_comprados, medio, puntos_de_regalo):
        super().__init__(id_compra, fecha, hora, puntos_por_litro, litros_comprados)
        self.__medio = medio
        self.__puntos_de_regalo = puntos_de_regalo
        
    #Getters:
    def get_medio(self):
        return self.__medio
    
    def get_puntos_de_regalo(self):
        return self.__puntos_de_regalo
    
    #Setters:
    def set_medio(self, nuevo_medio):
        self.__medio = nuevo_medio
        
    def set_puntos_de_regalo(self, nuevos_puntos_de_regalo):
        self.__puntos_de_regalo = nuevos_puntos_de_regalo
    
    #__str__:
    def __str__(self):
        titulo = "Electrónica:\n"
        medio = f"Medio: {self.__medio}\n"
        puntos_de_regalo = f"Puntos de regalo: {self.__puntos_de_regalo}\n"
        return titulo + super().__str__() + medio + puntos_de_regalo
    
    #Métodos:
    #CU 6:
    def calcular_puntaje_final(self):
         return (self._puntos_por_litro * self._litros_comprados) + self.__puntos_de_regalo
     