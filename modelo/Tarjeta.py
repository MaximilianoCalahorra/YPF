from Efectivo import Efectivo #Del módulo Efectivo.py importamos la clase Efectivo.
from Electronica import Electronica #Del módulo Electronica.py importamos la clase Electronica.
from Funciones import Funciones
import datetime
import re

#Clase Tarjeta:
class Tarjeta():
    #Constructor:
    def __init__(self, id_tarjeta, codigo, codigo_cliente):
        self.__id_tarjeta = id_tarjeta
        self.set_codigo(codigo)
        self.__codigo_cliente = codigo_cliente
        self.__compras = []
        
    #Getters:
    def get_id_tarjeta(self):
        return self.__id_tarjeta
    
    def get_codigo(self):
        return self.__codigo
    
    def get_codigo_cliente(self):
        return self.__codigo_cliente
    
    def get_compras(self):
        return self.__compras
    
    #Setters:
    def set_id_tarjeta(self, nuevo_id_tarjeta):
        self.__id_tarjeta = nuevo_id_tarjeta
        
    def set_codigo(self, nuevo_codigo):
        if re.match("^[a-zA-Z]{6}[0-9]{6}$", nuevo_codigo) == None:
            raise Exception(f"El código #{nuevo_codigo} es inválido.\n")
        self.__codigo = nuevo_codigo
        
    def set_codigo_cliente(self, nuevo_codigo_cliente):
        self.__codigo_cliente = nuevo_codigo_cliente
    
    #__str__:
    def __str__(self):
        titulo = "Tarjeta:\n"
        id_tarjeta = f"ID: #{self.__id_tarjeta}\n"
        codigo = f"Código: #{self.__codigo}\n"
        codigo_cliente = f"Código cliente: #{self.__codigo_cliente}\n"
        compras = "Compras:\n"
        for compra in self.__compras:
            compras += compra.__str__()
        return titulo + id_tarjeta + codigo + codigo_cliente + compras
    
    #Métodos:
    #CU 4:
    def agregar_compra_efectivo(self, fecha, hora, puntos_por_litro, litros_comprados, puntos_extra):
        id = 1
        if len(self.__compras) > 0:
            tamanio = len(self.__compras)
            id = self.__compras[tamanio - 1].get_id_compra() + 1
        self.__compras.append(Efectivo(id, fecha, hora, puntos_por_litro, litros_comprados, puntos_extra))    
    
    #CU 5:    
    def agregar_compra_electronica(self, fecha, hora, puntos_por_litro, litros_comprados, medio, puntos_de_regalo):
        id = 1
        if len(self.__compras) > 0:
            tamanio = len(self.__compras)
            id = self.__compras[tamanio - 1].get_id_compra() + 1
        self.__compras.append(Electronica(id, fecha, hora, puntos_por_litro, litros_comprados, medio, puntos_de_regalo) ) 
    
    #CU 7:
    def calcular_puntaje_cliente(self):
        puntaje = 0
        for compra in self.__compras:
            puntaje += compra.calcular_puntaje_final()
        return puntaje
    
    #CU 8:
    def calcular_puntaje_cliente_fecha(self, fecha):
        puntaje = 0
        for compra in self.__compras:
            if compra.get_fecha() == fecha:
                puntaje += compra.calcular_puntaje_final()
        return puntaje
    
    #CU 9:
    def calcular_puntaje_cliente_mes_anio(self, anio, mes):
        cantidad_dias = Funciones.traer_cantidad_dias_de_un_mes(self, anio, mes)
        puntaje = 0
        for i in range(1, cantidad_dias + 1):
            puntaje += self.calcular_puntaje_cliente_fecha(datetime.date(anio, mes, i))
        return puntaje
