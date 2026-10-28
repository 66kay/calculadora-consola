# Calculadora de consola
# Suma, resta, multiplica y divide dos numeros.

print("=== Calculadora ===")

seguir = "s"

while seguir == "s":
    a = float(input("Primer numero: "))
    operacion = input("Operacion (+, -, *, /): ")
    b = float(input("Segundo numero: "))

    if operacion == "+":
        print("Resultado:", a + b)
    elif operacion == "-":
        print("Resultado:", a - b)
    elif operacion == "*":
        print("Resultado:", a * b)
    elif operacion == "/":
        if b == 0:
            print("No se puede dividir por cero")
        else:
            print("Resultado:", a / b)
    else:
        print("Operacion no valida")

    seguir = input("Otra operacion? (s/n): ")

print("Hasta luego!")
