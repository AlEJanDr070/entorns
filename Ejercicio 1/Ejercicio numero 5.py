num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if num1 < 0:
    producto = num1 * num2 * num3
    print(f"El producto de los tres numeros es: {producto}")
else:
    suma = num1 + num2 + num3
    print(f"La suma de los tres números es: {suma}")