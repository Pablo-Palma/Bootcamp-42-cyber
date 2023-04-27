import hashlib
import hmac
import struct
import time

def TOTP(secret_key, interval=30):
    """
    Calcula el TOTP basado en el tiempo actual y la SecretKey.

    Args:
        secret_key (str): la SecretKey compartida entre el servidor y el cliente.
        interval (int): el intervalo de tiempo en segundos para el cual el TOTP es válido.
            Por defecto es 30 segundos.

    Returns:
        str: el valor del TOTP.
    """
    # Calcula el valor del tiempo actual en segundos dividido por el intervalo T1.
    # tiempo en segundo desde 1/1/70 partido de 30 devolvera la cantidad de intervalos de 30s
    time_slice = int(time.time()) // interval

    # Convierte el valor del tiempo actual en un arreglo de bytes de 8 bytes.i
    #struct.pack empaqueta, ">" indica big-endian, "Q" indica una cadena de 64 bits
    time_bytes = struct.pack(">Q", time_slice)

    # Calcula el HMAC-SHA-1 de la SecretKey y el valor del tiempo.
    #digest se utiliza para devolver el valor hash como una cadena de bytes.
    #.encode() convierte la secret_key en una cadena de bytes UTF-8
    #hmac_sha1 será un objeto de 20 bytes(160 bits).
    hmac_sha1 = hmac.new(secret_key.encode(), time_bytes, hashlib.sha1).digest()

    # Obtiene los últimos 4 bits del resultado del HMAC-SHA-1 para utilizarlos como índice.
    # con [-1] accedemos al ultimo byte de hmac_sha1
    #con la operación AND(&) con el valor 0x0F en binario: 00001111, obtenemos los ultimos 4 bits.(para usarlos como índice)
    # estos ultimos 4 bits representan un valor entre 0 y 15
    offset = hmac_sha1[-1] & 0x0F

    # Toma los siguientes 4 bytes del resultado del HMAC-SHA-1 ,a partir del índice.
    four_bytes = hmac_sha1[offset:offset+4]

    # Convierte los 4 bytes a un entero sin signo de 32 bits.
    value = struct.unpack(">I", four_bytes)[0]

    # Obtiene el valor de 6 dígitos del TOTP tomando el módulo de 10^6.
    totp = value % 1000000

    # Rellena el valor del TOTP con ceros a la izquierda si es necesario.
    totp_str = str(totp).zfill(6)

    return totp_str

secret_key = "secretkey"
totp = TOTP(secret_key)
print("Tu código TOTP es:", totp)
