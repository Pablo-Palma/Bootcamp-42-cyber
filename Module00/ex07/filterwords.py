import sys
import string

def main():
    # Verificar que se han pasado dos argumentos: una cadena y un entero
    if len(sys.argv) != 3:
        print("Debe proporcionar dos argumentos: una cadena y un entero.")
        return

    # Obtener los argumentos de la línea de comandos
    cadena = sys.argv[1]
    try:
        n = int(sys.argv[2])
    except ValueError:
        print("El segundo argumento debe ser un entero.")
        return

    # Crear una lista de palabras en la cadena
    palabras = cadena.split()

    # Crear una lista de palabras que cumplen la condición
    palabras_filtradas = [palabra.translate(str.maketrans("", "", string.punctuation)) for palabra in palabras if len(palabra.translate(str.maketrans("", "", string.punctuation))) > n]

    # Imprimir la lista de palabras filtradas
    print(palabras_filtradas)

if __name__ == '__main__':
    main()

