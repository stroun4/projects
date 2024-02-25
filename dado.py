import random

def lanzar_dado(caras):
    resultado = random.randint(1, caras)
    return resultado

def solicitar_numero_caras():
    while True:
        try:
            caras = int(input("Ingrese el número de caras del dado (entre 2 y 140): "))
            if 2 <= caras <= 140:
                return caras
            else:
                print("El número debe estar entre 2 y 140. Por favor, inténtelo de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

# Solicitamos al usuario el número de caras del dado
numero_de_caras = solicitar_numero_caras()

# Lanzamos el dado
resultado_dado = lanzar_dado(numero_de_caras)
print(f"Resultado del lanzamiento con un dado de {numero_de_caras} caras: {resultado_dado}")

  