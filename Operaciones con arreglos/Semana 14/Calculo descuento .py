"""Crea una función llamada calcular_descuento que tome dos parámetros: el monto total de la compra y un valor predeterminado para el porcentaje de descuento (por ejemplo, 10% por defecto).

La función debe calcular el descuento aplicando el porcentaje al monto total de la compra.

La función debe devolver el monto del descuento calculado.

Llamada a la Función:

Llama a la función calcular_descuento al menos dos veces desde el programa principal.
En una llamada, proporciona el monto total de la compra y, en la otra, proporciona tanto el monto total de la compra como el porcentaje de descuento"""

#funcion para calcular el descuento

def calcular_descuento(valor_total, porcentaje_descuento=10):
    descuento = valor_total * porcentaje_descuento / 100
    return descuento
monto_total1= 1000
descuento1 = calcular_descuento(monto_total1)
print(f"el monto total es :", monto_total1)
descuento = calcular_descuento(1000)
print(f"el valor del descuento es : ", descuento1)

#monto total y porcentaje
monto_total2= 1500
porcentaje_descontar= 20
descuento2 = calcular_descuento(monto_total2, porcentaje_descontar)
print(f"el monto total es :", monto_total2)
print(f"el valor del descuento 2 es  :", descuento2)


