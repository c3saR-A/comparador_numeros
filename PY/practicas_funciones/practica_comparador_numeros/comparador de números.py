def get_name():
    # Solicita el nombre y lo retorna en un saludo
    name = input("Hola usuario ¿Cuál es tu nombre?: ").title()
    return f"Mucho gusto, {name}, hora de trabajar"
def get_numbers():
    # Solicita dos números, validando que sean números y los retorna en una lista
    numbers = []
    for i in range(2):
        while True:
            try:
                num = float(input("Ingresa un número: "))
                break
            except ValueError:
                print("Solo se permiten números")
        numbers.append(num)
    return numbers

def evaluation(numbers):
    # Compara los números y retorna un mensaje si son iguales o cual es mayor
    if numbers[0] == numbers[1]:
        return "Los dos números ingresados son iguales"
    elif numbers[0] > numbers[1]:
        return f"Los números ingresados son diferentes, el primer número ({numbers[0]}) es mayor"
    else:
        return f"Los números ingresados son diferentes, el segundo número ({numbers[1]}) es mayor"

def query():
    # Pregunta al usuario si quiere hacerlo de nuevo y retorna la respuesta
    while True:
        ask = input("¿Quieres hacerlo de nuevo? (si/no): ").strip().lower()
        if ask in ["si", "no"]:
            return ask
        print("Respuesta no válida, intenta de nuevo")

def main():
    print(get_name())
    while True:
        numbers = get_numbers()
        print(evaluation(numbers))
        if query() == "no":
            break
    print(f"Gracias por tu tiempo cuídate")

if __name__ == "__main__":
    main()
