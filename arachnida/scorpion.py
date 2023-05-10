import os
import argparse
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

# Argumentos de la línea de comandos
parser = argparse.ArgumentParser(description="Scorpion - Extrae y modifica metadata EXIF de las imágenes.")
parser.add_argument('images', nargs='+', help="Lista de imágenes para analizar.")
parser.add_argument('-r', '--remove', action='store_true', help="Eliminar los metadatos EXIF.")

args = parser.parse_args()  

# Función para manejar el GPSInfo
def handle_gps_info(gps_info):
    gps_data = {GPSTAGS.get(t, t): gps_info[t] for t in gps_info}
    for tag, value in gps_data.items():
        if tag == "GPSLatitude" and isinstance(value, tuple):
            gps_data[tag] = convert_to_degrees(value)
        elif tag == "GPSLongitude" and isinstance(value, tuple):
            gps_data[tag] = convert_to_degrees(value)
    return gps_data

def convert_to_degrees(value):
    d = float(value[0][0]) / float(value[0][1])
    m = float(value[1][0]) / float(value[1][1])
    s = float(value[2][0]) / float(value[2][1])
    return d + (m / 60.0) + (s / 3600.0)

# Función principal para extraer la metadata EXIF de una imagen.
def extract_metadata(image_path):
    image = Image.open(image_path)
    exif_data = {}
    if hasattr(image, '_getexif'):
        exif_info = image._getexif()
        if exif_info is not None:
            for tag, value in exif_info.items():
                tag_name = TAGS.get(tag, tag)
                if tag_name == 'GPSInfo':
                    exif_data[tag_name] = handle_gps_info(value)
                else:
                    exif_data[tag_name] = value
    return exif_data
def remove_exif(image_path):
    image = Image.open(image_path)
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)
    image_without_exif.save(image_path)

def modify_exif(image_path):
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exif_info = image._getexif()
        if exif_info is not None:
            for tag, value in exif_info.items():
                if isinstance(value, str):
                    exif_info[tag] = value.upper()
            image.save(image_path, exif=exif_info.dump())

# Procesa cada archivo de imagen
for image_file in args.images:
    if os.path.isfile(image_file):
        print(f"Metadata para {image_file}:")
        try:
            exif_data = extract_metadata(image_file)
            for key, val in exif_data.items():
                print(f"   {key}: {val}")
        except IOError:
            print('IOError ' + image_file)
    else:
        print(f"{image_file} no es un archivo válido.")

# Elimina los metadatos EXIF de las imágenes especificadas
if args.remove:
    for image_file in args.images:
        if os.path.isfile(image_file):
            print(f"Eliminando metadatos de {image_file}...")
            remove_exif(image_file)  # Aquí usamos la función remove_exif()

#for file in data/*; do python3 scorpion.py "$file"; done

