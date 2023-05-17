# README.md

---

## :closed_lock_with_key: Infection: Herramienta de Cifrado y Descifrado de Archivos

Infection es un potente programa destinado a proporcionar un alto nivel de seguridad mediante el cifrado y descifrado de archivos con extensiones específicas. Utiliza el algoritmo criptográfico `Fernet` para garantizar la confidencialidad de tus datos.

---

### :bookmark_tabs: Instrucciones de Uso

#### :lock: Cifrado de Archivos

Para cifrar todos los archivos contenidos en la carpeta 'infection' que coincidan con las extensiones especificadas en la lista `target_extensions`, ejecuta el script sin ningún argumento. Se te solicitará una clave de encriptación de al menos 16 caracteres. Los archivos cifrados se guardarán con la extensión adicional '.ft'.

```bash
python script.py
```

#### :unlock: Descifrado de Archivos

Para descifrar archivos, necesitarás proporcionar la clave de encriptación original utilizada durante el proceso de cifrado. Utiliza la opción `-r` o `--reverse` para esto. Los archivos descifrados se recuperarán con sus extensiones originales.

```bash
python script.py -r <clave de encriptación>
```

#### :mute: Modo Silencioso

Si deseas que el script se ejecute sin producir salida, puedes activar el modo silencioso con la opción `-s` o `--silent`.

```bash
python script.py -s
```

```bash
python script.py -r <clave de encriptación> -s
```

#### :information_source: Ver la Versión del Programa

Para obtener información sobre la versión del programa, utiliza la opción `-v` o `--version`.

```bash
python script.py -v
```

---

### :warning: Precauciones

- Asegúrate de recordar la clave de encriptación que utilizaste: es necesaria para descifrar los archivos. Si la olvidas, no podrás recuperar tus datos.
- Realiza una copia de seguridad de tus archivos antes de cifrarlos. En caso de cualquier error durante el proceso de cifrado, podrías perder tus datos.
- No interrumpas el script mientras se está ejecutando. Esto podría resultar en un estado de cifrado parcial de tus archivos.
