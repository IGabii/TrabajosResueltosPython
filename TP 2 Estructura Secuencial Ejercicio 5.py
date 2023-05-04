"""Tres personas invierten dinero para fundar una empresa (no necesariamente en parte iguales).
Calcular que porcentaje invirtio cada uno."""


persona1=int(input("Ingrese el dinero invertido: "))
persona2=int(input("Ingrese el dinero invertido: "))
persona3=int(input("Ingrese el dinero invertido: "))
total_dinero=persona1+persona2+persona3
persona1_inversion=persona1*total_dinero/100
persona2_inversion=persona2*total_dinero/100
persona3_inversion=persona3*total_dinero/100
print("La primera persona abono: ",persona1_inversion,"%")
print("La segunda persona abono: ",persona2_inversion,"%")
print("La tercera persona abono: ",persona3_inversion,"%")