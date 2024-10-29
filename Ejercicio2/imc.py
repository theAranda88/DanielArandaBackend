def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def interpretar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

def main():
    print("Cálculo del Índice de Masa Corporal (IMC)")

    try:
        peso = float(input("Ingresa tu peso en kilogramos: "))
        altura = float(input("Ingresa tu altura en metros: "))

        if peso <= 0 or altura <= 0:
            print("El peso y la altura deben ser números positivos.")
            return

        imc = calcular_imc(peso, altura)
        resultado = interpretar_imc(imc)

        print(f"Tu IMC es: {imc:.2f}")
        print(f"Interpretación: {resultado}")

    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")

if __name__ == "__main__":
    main()
