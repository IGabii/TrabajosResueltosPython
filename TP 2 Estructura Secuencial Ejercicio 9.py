"""Una inmobiliaria paga a sus vendedores un salario de $50000,
más una comisión de $5000 por cada venta realizada, más el 5% del valor de las ventas.
Realizar un programa que imprima el número del vendedor y el salario que le corresponde en un determinado mes.
Se leen el número del vendedor, la cantidad de ventas que realizó y el valor total de las mismas. """

salario=50000
vendedor=int(input("Ingrese la cantidad de ventas q realizo: "))
comision=5000*vendedor*0.5
print("La cantidad de ventas fue de ",vendedor)
print("Y el salario mas comision es de ",salario+comision,"$")