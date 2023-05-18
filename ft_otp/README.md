# README - Proyecto ft_otp

¡Bienvenido a **ft_otp**! Este es un proyecto de autenticación de dos factores (2FA) basado en One-Time Password (OTP). La aplicación genera una contraseña única de uso temporal a través de un algoritmo HMAC-SHA1.

## Cómo Usarlo

1. **Creación de clave secreta**: Para generar una clave secreta, deberás introducir una cadena hexadecimal de al menos 64 caracteres. El script te solicitará una clave de encriptación para proteger esta clave secreta. Ejecuta el script de la siguiente manera: 
    ```
    python ft_otp.py -g nombre_del_archivo
    ```
    donde `nombre_del_archivo` es el archivo que contiene tu cadena hexadecimal.

2. **Generación de OTP**: Para generar la OTP, deberás introducir la clave de encriptación previamente establecida. Ejecuta el script así: 
    ```
    python ft_otp.py -k
    ```

## Detalles Técnicos

El script de **ft_otp** realiza los siguientes pasos:

1. **Encriptación**: Si se proporciona un archivo con una cadena hexadecimal de 64 o más caracteres, la cadena se encripta utilizando Fernet basado en la clave de encriptación proporcionada por el usuario.

2. **OTP**: La OTP se genera calculando el HMAC-SHA1 de la clave secreta y la hora actual, seguido por una serie de operaciones para obtener un número de 6 dígitos.

3. **Visualización de OTP**: Finalmente, la OTP se imprime y también se muestra como un código QR en la terminal.

## Importante

Por seguridad, no compartas tu clave secreta ni tu clave de encriptación. La clave de encriptación es esencial para descifrar tu clave secreta y generar las OTPs.

¡Gracias por usar **ft_otp**! Esperamos que te ayude a fortalecer la seguridad de tus sistemas y servicios.
