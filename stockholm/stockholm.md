# README.md

## Descripción
Este es un programa de cifrado y descifrado de archivos con extensiones específicas. Utiliza el módulo de criptografía `Fernet` para el cifrado y descifrado.

## Cómo usar
1. **Cifrado de archivos:** Para cifrar todos los archivos con las extensiones especificadas en la lista `target_extensions` dentro de la carpeta 'infection', simplemente ejecuta el script sin ningún argumento. Se te pedirá que introduzcas una clave de encriptación de al menos 16 caracteres. Los archivos cifrados se guardarán con la extensión '.ft'.

    ```
    python script.py
    ```

2. **Descifrado de archivos:** Para descifrar los archivos, debes proporcionar la misma clave de encriptación que se utilizó para cifrar los archivos utilizando la opción `-r` o `--reverse`. Los archivos descifrados se guardarán con sus extensiones originales.

    ```
    python script.py -r <clave de encriptación>
    ```

3. **Modo silencioso:** Si prefieres que el script se ejecute sin producir ningún output, puedes utilizar la opción `-s` o `--silent`.

    ```
    python script.py -s
    ```

    o para descifrar en modo silencioso:

    ```
    python script.py -r <clave de encriptación> -s
    ```

4. **Ver la versión:** Para ver la versión del programa, puedes utilizar la opción `-v` o `--version`.

    ```
    python script.py -v
    ```

## Precauciones
- Asegúrate de recordar la clave de encriptación que utilices, ya que es necesaria para descifrar los archivos. Si la olvidas, no podrás recuperar tus archivos.
- Antes de cifrar tus archivos, se recomienda realizar una copia de seguridad de los mismos. Si ocurre algún error durante el proceso de cifrado, podrías perder tus datos.
- No interrumpas el script mientras se está ejecutando. Esto podría dejar tus archivos en un estado de cifrado parcial.
