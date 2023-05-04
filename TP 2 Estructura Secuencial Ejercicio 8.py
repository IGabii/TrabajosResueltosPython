"""Leer una medida en metros e imprimir esta medida expresada en centímetros, pulgadas, pies y yardas.
Los factores de conversión son:

1 pie=12 pulgadas
1 yarda = 3 pies
1 pulgada= 2,54cm
1 metro= 100cm"""


medida=int(input("Ingrese la medida que quiera saber: "))
cm=medida*100
pulgada=medida*39.37
pies=pulgada/32
yarda=pies/3

print("Su medida en cm es", cm)
print("Su medida en pulgada es de ",pulgada)
print("Su medida en pies es de ",pies)
print("Su medida en yarda es de ",yarda)