import datetime
import re

#Clase Funciones:
class Funciones:
    #Año bisiesto:
    def es_bisiesto(self, anio):
        return (anio % 4 == 0) and ((anio % 100 != 0) or (anio % 400 == 0))
    
    #Fecha válida:
    def es_fecha_valida(self, fecha):
        dia = fecha.day #Obtenemos el número de día en el mes.
        mes = fecha.month #Obtenemos el número de mes.
        anio = fecha.year #Obtenemos el número de año.
        valida = False #Suponemos que la fecha es inválida.
        if (anio > 0): #El año es válido...
            if (mes >= 1 and mes <= 12): #El mes es válido...
                if ((mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and (dia >= 1 and dia <= 31)): #Día con mes es válido... 
                    valida = True #La fecha es válida.
                elif ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and (dia >= 1 and dia <= 30)): #Día con mes es válido..
                    valida = True #La fecha es válida.
                else:
	 			    #El mes es 2.
                    if ((dia >= 1 and dia <= 28) or ((dia >= 1 and dia <= 29) and self.es_bisiesto(anio))): #28 para febrero y 29 para febrero de año bisiesto...
                        valida = True #La fecha es válida.
        return valida; #Retornamos si la fecha es válida o no. 
    
    #Fecha corta:
    def traer_fecha_corta(self, fecha):
        return f"{fecha.day}/{fecha.month}/{fecha.year}"


    #Hora corta:
    def traer_hora_corta(self, hora):
        return f"{hora.hour}:{hora.minute}"
	
	#Día hábil:
    def es_dia_habil(self, fecha):
        numero_dia = fecha.isoweekday() #Obtenemos el número del día en la semana.
        return  ((numero_dia >= 1) and (numero_dia <= 5)) #Retorna True si el número es de 1 a 5 (inclusive).
 
    #Nombre día de la semana:
    def traer_dia_de_la_semana(self, fecha):
        numero_dia_en_la_semana = fecha.isoweekday()
        nombre_dia = ""
        if numero_dia_en_la_semana == 1:
            nombre_dia = "Lunes"
        elif numero_dia_en_la_semana == 2:
            nombre_dia = "Martes"
        elif numero_dia_en_la_semana == 3:
            nombre_dia = "Miércoles"
        elif numero_dia_en_la_semana == 4:
            nombre_dia = "Jueves"
        elif numero_dia_en_la_semana == 5:
            nombre_dia = "Viernes"
        elif numero_dia_en_la_semana == 6:
            nombre_dia = "Sábado"
        else:
            nombre_dia = "Domingo"
        return nombre_dia
	
	#Nombre mes:
    def traer_mes_en_letras(self, fecha):
        numero_mes = fecha.month
        nombre_mes = ""
        if numero_mes == 1:
            nombre_mes = "Enero"
        elif numero_mes == 2:
            nombre_mes = "Febrero"
        elif numero_mes == 3:
            nombre_mes = "Marzo"
        elif numero_mes == 4:
            nombre_mes = "Abril"
        elif numero_mes == 5:
            nombre_mes = "Mayo"
        elif numero_mes == 6:
            nombre_mes = "Junio"
        elif numero_mes == 7:
            nombre_mes = "Julio"
        elif numero_mes == 8:
            nombre_mes = "Agosto"
        elif numero_mes == 9:
            nombre_mes = "Septiembre"
        elif numero_mes == 10:
            nombre_mes = "Octubre"
        elif numero_mes == 11:
            nombre_mes = "Noviembre"
        else:
            nombre_mes = "Diciembre"
        return nombre_mes
	
    #Fecha larga:
    def traer_fecha_larga(self, fecha):
        numero_dia = fecha.day
        anio = fecha.year
        return f"{self.traer_dia_de_la_semana(fecha)} {numero_dia} de {self.traer_mes_en_letras(fecha)} del {anio}"
 
	#Cantidad de días de un mes:
    def traer_cantidad_dias_de_un_mes(self, anio, mes):
        cantidad_dias = 0
        if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
            cantidad_dias = 31 
        elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
            cantidad_dias = 30
        else:
			#El mes es 2.
            if (self.es_bisiesto(anio)): #Si el año es bisiesto...
                cantidad_dias = 29 #La fecha es válida.
            else:
                cantidad_dias = 28
        return cantidad_dias
	
	#Aproximar con 2 decimales:
    def aproximar_2_decimal(self, valor):
        return (float(round(valor * 100))) / 100
    
    #Es número:
    def es_numero(self, c):
        resultado = re.match(r"\d{1}", c)
        if resultado != None:
            es = True
        else:
            es = False
        return es
    
    #Es letra:
    def es_letra(self, c):
        resultado = re.match(r"[a-zA-Z]{1}", c)
        if resultado != None:
            es = True
        else:
            es = False
        return es
	
	#Es cadena de números:
    def es_cadena_nros(self, cadena):
        resultado = re.match(r"^\d$", cadena)
        if resultado != None:
            es = True
        else:
            es = False
        return es
    #Es cadena de letras:
    def es_cadena_letras(self, cadena):
        resultado = re.match(r"^[a-zA-Z]$", cadena)
        if resultado != None:
            es = True
        else:
            es = False
        return es
   
