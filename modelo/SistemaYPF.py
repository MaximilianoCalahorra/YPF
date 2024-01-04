from Tarjeta import Tarjeta #Del módulo Tarjetas.py importamos la clase Tarjeta.
from Efectivo import Efectivo

#Clase SistemaYPF
class SistemaYPF:
    #Constructor:
    def __init__(self):
        self.__tarjetas = []
        
    #Getter:
    def get_tarjetas(self):
        return self.__tarjetas   
    
    #__str__:
    def __str__(self):
        tarjetas = "Lista de tarjetas:\n"
        for tarjeta in self.__tarjetas:
            tarjetas += (tarjeta.__str__() + "\n")
        return tarjetas
    
    #Métodos:   
    #CU 2:
    def traer_tarjeta(self, codigo_cliente):
        tarjeta_auxiliar = None
        tarjeta_buscada = None
        i = 0
        while tarjeta_buscada == None and i < len(self.__tarjetas):
            tarjeta_auxiliar = self.__tarjetas[i]
            if tarjeta_auxiliar.get_codigo_cliente() == codigo_cliente:
                tarjeta_buscada = tarjeta_auxiliar
            i += 1
        return tarjeta_buscada 
    
    #CU 3:
    def agregar_tarjeta(self, codigo, codigo_cliente):
        id = 1
        if len(self.__tarjetas) > 0:
            tamanio = len(self.__tarjetas)
            id = self.__tarjetas[tamanio - 1].get_id_tarjeta() + 1
        return self.__tarjetas.append(Tarjeta(id, codigo, codigo_cliente))
    
    #CU 10:
    def traer_tarjetas_compras_efectivo(self, fecha_desde, fecha_hasta):
        tarjetas_que_cumplen = []
        for tarjeta in self.__tarjetas:
            i = 0
            cumple = False
            while not cumple and i < len(tarjeta.get_compras()):
                compra = tarjeta.get_compras()[i]
                if isinstance(compra, Efectivo) and not(compra.get_fecha() < fecha_desde) and not(compra.get_fecha() > fecha_hasta) :
                    tarjetas_que_cumplen.append(tarjeta)
                    cumple = True
                i += 1
        return tarjetas_que_cumplen    