import math

num = float(input("Ingrese un número: "))

if num <=0:
    print("Error: El número debe ser mayor que cero.")
else:
    cuadrado = num ** 2
    raiz_cuadrada = math.sqrt(num)
    print(f"Del número {num}, su potencia es {cuadrado} y su raíz es {raiz_cuadrada}")
#khsfd