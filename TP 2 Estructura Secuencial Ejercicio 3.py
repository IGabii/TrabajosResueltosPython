"""Calcular el promedio de las notas que obtiene un alumno al rendir los dos parciales"""

cantidad,suma=0,0
nota=int(input("Ingrese su nota o -1 para finalizar: "))
while nota!=-1:
    cantidad=cantidad+1
    suma=suma+nota
    nota=int(input("Ingrese su nota o -1 para finalizar: "))
promedio=suma/cantidad

print("Su promedio final es de: ",promedio)
