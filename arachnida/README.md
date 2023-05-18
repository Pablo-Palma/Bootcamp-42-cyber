# Arachnida

Arachnida es un conjunto de herramientas de ciberseguridad compuesto por dos módulos principales: **Spider** y **Scorpion**. Ambos trabajan en conjunto para ayudar en tareas de análisis web y gestión de imágenes.

## Spider 🕷️

Spider es un rastreador web en Python que descarga todas las imágenes de un sitio web de manera recursiva.

### Uso

```sh
python spider.py URL [-r] [-l LEVEL] [-p PATH]
```

Argumentos:
- **URL**: URL del sitio web desde el que descargar las imágenes.
- **-r, --recursive**: Habilita la descarga recursiva de imágenes.
- **-l, --level**: Indica el nivel de profundidad máximo de la descarga recursiva (por defecto 5).
- **-p, --path**: Ruta donde se guardarán las imágenes descargadas (por defecto "./data/").

## Scorpion 🦂

Scorpion es una herramienta que extrae y modifica la metadata EXIF de las imágenes.

### Uso

```sh
python scorpion.py IMAGES [-r]
```

Argumentos:
- **IMAGES**: Lista de imágenes para analizar.
- **-r, --remove**: Elimina los metadatos EXIF de las imágenes.

## Instalación y requisitos

1. Clona este repositorio.
2. Asegúrate de tener Python 3.6+ instalado.
3. Instala las dependencias con pip: `pip install -r requirements.txt`.

## Disclaimer

Estas herramientas están destinadas a ser utilizadas con fines de análisis y ciberseguridad y deben ser utilizadas de forma responsable y ética. No me hago responsable del uso indebido de estas herramientas.
