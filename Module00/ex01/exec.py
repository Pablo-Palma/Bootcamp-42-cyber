import sys

# Verificar si el programa tiene al menos un argumento
if len(sys.argv) > 1:
    # Unir los argumentos en una sola cadena separada por un espacio
    input_string = ' '.join(sys.argv[1:])

    # Revertir la cadena y cambiar el caso de las letras
    output_string = input_string[::-1].swapcase()

    # Imprimir la cadena resultante
    print(output_string)
else:
    # Imprimir un mensaje de uso
    print("Prueba introduciendo un argumento")

