print("Calculadora simple")
numero1 = float(input("Captura un número: "))
numero2 = float(input("Captura un número: "))

def calculadora(numero1, numero2) -> float:
    operador = str(input("Elija una operación: "))
    if operador == "+":
        resultado = numero1 + numero2
        return resultado

    elif operador == "-":
        resultado = numero1 - numero2
        return resultado

    elif operador == "*":
        resultado = numero1 * numero2
        return resultado

    elif operador == "/":
        try:
            numero1/0

        except ZeroDivisionError:
            print("Cannot divide by zero!")

        finally:
            resultado = numero1 / numero2
            return resultado
    else: 
        print("Operador no permitido")
        


print(calculadora(numero1, numero2))




        


