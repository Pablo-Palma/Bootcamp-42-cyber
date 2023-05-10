import os
import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Verifica si la url es válida.
def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

# Obtiene todas las imágenes de la url proporcionada.
def get_all_images(url):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    urls = [img['src'] for img in soup.find_all("img")]
    urls = [urljoin(url, img_url) for img_url in urls]
    return [url for url in urls if is_valid(url)]

# Descarga una imagen de la url proporcionada.
def download(url, pathname):
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    response = requests.get(url, stream=True)
    filename = os.path.join(pathname, url.split("/")[-1])

    with open(filename, "wb") as f:
        for data in response.iter_content(1024):
            f.write(data)
    print(f"{filename} descargado con éxito.")

# Principal función
def main(url, path, depth):
    if depth == 0:
        return
    try:
        img_urls = get_all_images(url)
        for img_url in img_urls:
            # Si la imagen tiene una de las extensiones especificadas, descárgala.
            if any(map(img_url.endswith, [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".pdf", ".docx"])):
                download(img_url, path)
    except Exception as e:
        print(f"Ocurrió un error al procesar {url}: {e}")
        return

    # Recursividad en los enlaces internos
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for link in soup.find_all("a"):
        url = link.get("href")
        if url is not None and not url.startswith('http'):
            url = urljoin(url, url)
        if url is not None and url not in visited and url.startswith('http'):
            visited.add(url)
            main(url, path, depth - 1)

# Argumentos de la línea de comandos
parser = argparse.ArgumentParser(description="Spider - Descarga de imágenes de un sitio web de manera recursiva.")
parser.add_argument("URL", help="URL de la página web para descargar imágenes.")
parser.add_argument("-r", "--recursive", action="store_true", help="Habilita la descarga recursiva de imágenes.")
parser.add_argument("-l", "--level", type=int, default=5, help="Indica el nivel de profundidad máximo de la descarga recursiva.")
parser.add_argument("-p", "--path", default="./data/", help="Indica la ruta donde se guardarán los archivos descargados.")

args = parser.parse_args()

# Conjunto de URL visitadas
visited = set()

# Llamada a la función principal
if args.recursive:
    main(args.URL, args.path, args.level)
else:
    main(args.URL, args.path, 1)

