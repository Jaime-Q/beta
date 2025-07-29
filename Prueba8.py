def ingresar_numeros(cantidad):
    N = []

    for i in range(cantidad):
        while True:
            try:
                nuevo = int(input(f"Ingrese el número #{i + 1}: "))
                if len(N) >= 2 and nuevo == N[-1] + N[-2]:
                    print("⚠️ No puedes ingresar ese número. Es igual a la suma del último y penúltimo valor.")
                else:
                    N.append(nuevo)
                    break
            except ValueError:
                print("❗ Entrada inválida. Por favor, ingresa un número entero.")

    print("\n📦 Vector final:")
    print(N)

ingresar_numeros(5)