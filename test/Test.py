import sys
sys.path.append('D:\Curso POO Python\YPF\modelo') #Agregamos la ruta al paquete modelo.

import datetime
from SistemaYPF import SistemaYPF #Importamos del módulo SistemaYPF.py la clase SistemaYPF.

#Test:
sistema_ypf = SistemaYPF()

#Test 1:
print("\nTest 1:")
try: 
    sistema_ypf.agregar_tarjeta("ABCDEFG123456", "DNI11222333")
except Exception as e:
    print(e)
try:
    sistema_ypf.agregar_tarjeta("ABCDE1234567", "DNI11222333")
except Exception as e:
    print(e)
try:
    sistema_ypf.agregar_tarjeta("ABCDEFG12345", "DNI11222333")
except Exception as e:
    print(e)
    
#Test 2:
print("Test 2:")
try:
    sistema_ypf.agregar_tarjeta("ABCDEF123456", "DNI11222333")
    sistema_ypf.agregar_tarjeta("GHIJKL987654", "DNI44555666")
    sistema_ypf.agregar_tarjeta("MNOPQR456654", "DNI77888999")
    print(sistema_ypf)
except Exception as e:
    print(e)
    
#Test 3.1:
print("Test 3.1:")
tarjeta = sistema_ypf.traer_tarjeta("DNI11222333")
tarjeta.agregar_compra_efectivo(datetime.date(2021, 9, 10), datetime.time(10, 30), 100.0, 25.0, 20.0)
tarjeta.agregar_compra_efectivo(datetime.date(2021, 10, 1), datetime.time(20, 30), 200.0, 40.0, 50.0)
tarjeta.agregar_compra_electronica(datetime.date(2021, 9, 15), datetime.time(10, 30), 100.0, 30.0, "MODO", 500.0)
tarjeta.agregar_compra_electronica(datetime.date(2021, 10, 1), datetime.time(20, 30), 200.0, 20.0, "MODO", 500.0)
print("Lista de compras de la tarjeta con código de cliente DNI11222333:")
for compra in tarjeta.get_compras():
    print(compra)
    print(f"Puntaje final: {compra.calcular_puntaje_final()} puntos\n")
    
#Test 3.2:
print("Test 3.2:")
sistema_ypf.traer_tarjeta("DNI44555666").agregar_compra_efectivo(datetime.date(2021, 9, 11), datetime.time(15, 0), 100.0, 20.0, 20.0)
print("Compra agregada\n")

#Test 3.3:
print("Test 3.3:")
sistema_ypf.traer_tarjeta("DNI44555666").agregar_compra_electronica(datetime.date(2021, 9, 16), datetime.time(15, 0), 100.0, 35.0, "MERCADO PAGO", 1000.0)
print("Compra agregada\n")

#Test 4:
print("Test 4:")
print(f"Puntaje total cliente DNI11222333: {tarjeta.calcular_puntaje_cliente()} puntos\n")

#Test 5:
print("Test 5:")
print(f"Puntaje total cliente DNI11222333 el día 1/10/2021: {tarjeta.calcular_puntaje_cliente_fecha(datetime.date(2021, 10, 1))} puntos\n")

#Test 6:
print("Test 6:")
print(f"Puntaje total del cliente DNI11222333 durante 9/2021: {tarjeta.calcular_puntaje_cliente_mes_anio(2021, 9)} puntos\n")

#Test 7:
print("Test 7:")
print("Tarjetas con compras en efectivo entre el 1/8/2021 y el 1/11/2021:")
tarjetas = sistema_ypf.traer_tarjetas_compras_efectivo(datetime.date(2021, 8, 1), datetime.date(2021, 11, 1))
for tarjeta in tarjetas:
    print(tarjeta)
