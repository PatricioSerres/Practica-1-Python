from random import choice, randrange #Un rango random
from datetime import datetime #Importa la hora

# Operadores posibles
operators = ["+", "-", "*", "/"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo
# Esto toma la fecha y hora actual.
init_time = datetime.now()
contador = 0

print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
# Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    # Debido a que no es posible la division por 0, repetimos hasta que tenga un valor valido
    while ((operator == "/") and (number_2 == 0)):
        number_2 = randrange(10)
        operator = choice(operators)

    match operator:
        case "+":
            cuenta = number_1 + number_2
        case "-":
            cuenta = number_1 - number_2
        case "*":
            cuenta = number_1 * number_2
        case "/":
            cuenta = number_1 / number_2

# Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
# Le pedimos al usuario el resultado
    result = float(input("resultado: "))
    if(result == cuenta):
        print("El resultado es correcto")
        contador += 1
    else:
        print("El resultado no es correcto")

incorrectos = times - contador
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")
print(f"Tuviste {contador} resultados correctos y {incorrectos} resultados incorrectos")