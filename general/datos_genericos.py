# Calcular la raíz cuadrada de 25
import math

str_numero = input("Ingrese un número: ")
float_numero = float(str_numero)
raiz_numero = math.sqrt(float_numero)
print(math.trunc(raiz_numero))
# print(math.fsum(range(0,15)))
print(f"{type(str_numero)} {type(float_numero)} {type(raiz_numero)}")