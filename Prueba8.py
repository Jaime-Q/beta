def solicitar_vector(n):
    vector = []
    while len(vector) < n:
        nuevo = int(input(f"Ingrese el valor #{len(vector)+1}: "))
        while len(vector) >= 2 and nuevo == vector[-1] + vector[-2]:
            print(f"⚠️ No se puede ingresar {nuevo}, ya que es igual a la suma de {vector[-1]} + {vector[-2]}. Intente otro número.")
            nuevo = int(input(f"Ingrese un nuevo valor distinto a la suma: "))
        vector.append(nuevo)
    return vector

# Ejemplo de uso:
tamano = int(input("¿Cuántos números desea ingresar al vector?: "))
resultado = solicitar_vector(tamano)
print("✅ Vector final:", resultado)