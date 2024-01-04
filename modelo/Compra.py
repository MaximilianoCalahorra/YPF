from abc import ABC, abstractclassmethod

#Clase Compra:
class Compra(ABC):
    #Constructor:
    def __init__(self, id_compra, fecha, hora, puntos_por_litro, litros_comprados):
        self._id_compra = id_compra
        self._fecha = fecha
        self._hora = hora
        self._puntos_por_litro = puntos_por_litro
        self._litros_comprados = litros_comprados
        
    #Getters:
    def get_id_compra(self):
        return self._id_compra
    
    def get_fecha(self):
        return self._fecha
    
    def get_hora(self):
        return self._hora
    
    def get_puntos_por_litro(self):
        return self._puntos_por_litro
    
    def get_litros_comprados(self):
        return self._litros_comprados
    
    #Setters:
    def set_id_compra(self, nuevo_id_compra):
        self._id_compra = nuevo_id_compra
        
    def set_fecha(self, nueva_fecha):
        self._fecha = nueva_fecha
        
    def set_hora(self, nueva_hora):
        self._hora = nueva_hora
        
    def set_puntos_por_litro(self, nuevos_puntos_por_litro):
        self._puntos_por_litro = nuevos_puntos_por_litro
    
    def set_litros_comprados(self, nuevos_litros_comprados):
        self._litros_comprados = nuevos_litros_comprados
        
    #__str__:
    def __str__(self):
        id = f"ID: #{self._id_compra}\n"
        fecha = f"Fecha: {self._fecha}\n"
        hora = f"Hora: {self._hora}\n"
        puntos_por_litro = f"Puntos por litro: {self._puntos_por_litro}\n"
        litros_comprados = f"Litros comprados: {self._litros_comprados}\n" 
        return id + fecha + hora + puntos_por_litro + litros_comprados
    
    #Métodos:
    #CU 6:
    @abstractclassmethod
    def calcular_puntaje_final(self):
         pass #Implementación en cada clase hija de Compra.
    