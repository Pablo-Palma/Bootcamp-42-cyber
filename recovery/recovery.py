# -*- coding: utf-8 -*-

import subprocess
import argparse
import winreg
import os
from datetime import datetime, timedelta, timezone
from browser_history import get_history

def get_all_browsers_history(hours):
    now = datetime.now(timezone.utc)  # make it timezone-aware
    start_time = now - timedelta(hours=hours)

    outputs = get_history()

    for item in outputs.histories:
        if start_time <= item[0] <= now:
            print(f'URL: {item[1]}, Fecha y hora de visita: {item[0]}')


def registry_changes(hours=24):
    key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path)
    except Exception as e:
        print("Error al abrir la clave del registro:", e)
        return

    num_values = winreg.QueryInfoKey(key)[1]  # Obtener el número de valores en esta clave

    for i in range(num_values):
        try:
            value_name, value_data, _ = winreg.EnumValue(key, i)  # Obtener el nombre y los datos de cada valor
            print("Valor:", value_name)
            print("Datos:", value_data)
            print()
        except Exception as e:
            print("Error al enumerar los valores del registro:", e)
            return

    # Si todavía quieres imprimir la última fecha de modificación de la clave en sí:
    try:
        timestamp = winreg.QueryInfoKey(key)[2]  # Obtener el tiempo de modificación de la clave
        epoch = datetime(1601, 1, 1)
        delta = timedelta(microseconds=timestamp / 10)
        fecha_modificacion = epoch + delta

        # Comprobando si la fecha de modificación se encuentra dentro del intervalo especificado
        now = datetime.now()
        difference = now - fecha_modificacion
        if difference <= timedelta(hours=hours):
            print("Última modificación:", fecha_modificacion)
        else:
            print("La última modificación no se encuentra dentro del rango de tiempo especificado.")
    except Exception as e:
        print("Error al obtener la fecha de modificación del registro:", e)



def recent_files(hours=24):
    try:
        recent_folder = os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Recent")
        now = datetime.now()

        for file_name in os.listdir(recent_folder):
            file_path = os.path.join(recent_folder, file_name)

            if os.path.isfile(file_path):
                try:
                    modification_date = datetime.fromtimestamp(os.path.getmtime(file_path))

                    if now - modification_date <= timedelta(hours=hours):  # Here's the change
                        print("Archivo:", file_path)
                        print("Ãšltima modificaciÃ³n:", modification_date)
                        print()
                except Exception as e:
                    print("Error al obtener la informaciÃ³n del archivo:", e)
    except Exception as e:
        print(f"Error al obtener la lista de archivos recientes: {e}")

def installed_programs(hours=24):
    try:
        key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path)

        now = datetime.now()  # Changed from datetime.datetime.now()

        for i in range(winreg.QueryInfoKey(key)[0]):
            subkey_name = winreg.EnumKey(key, i)
            subkey = winreg.OpenKey(key, subkey_name)

            try:
                program_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                program_version = winreg.QueryValueEx(subkey, "DisplayVersion")[0]
                install_date = winreg.QueryValueEx(subkey, "InstallDate")[0]

                # Convertir la fecha de instalaciÃ³n en un objeto de fecha y hora
                install_datetime = datetime.strptime(install_date, "%Y%m%d")  # Changed from datetime.datetime.strptime()

                # Calcular la diferencia de tiempo entre la fecha de instalaciÃ³n y ahora
                time_difference = now - install_datetime

                # Comprobar si la diferencia de tiempo estÃ¡ dentro del rango especificado
                if time_difference <= timedelta(hours=hours):  # Changed from datetime.timedelta()
                    print("Programa:", program_name)
                    print("VersiÃ³n:", program_version)
                    print("Fecha de instalaciÃ³n:", install_datetime)
                    print()

            except Exception as e:
                # Omitir subclaves sin nombre de programa o versiÃ³n
                continue

            winreg.CloseKey(subkey)

        winreg.CloseKey(key)

    except Exception as e:
        print(f"Error al obtener la lista de programas instalados: {e}")

def get_open_programs():
    try:
        now = datetime.now()  # Changed from datetime.datetime.now()

        programs = []

        # Ejecutar el comando tasklist para obtener la lista de programas abiertos
        output = subprocess.check_output(['tasklist']).decode('utf-8')

        # Dividir las lÃ­neas de salida en una lista de lÃ­neas
        lines = output.split('\n')

        # Recorrer las lÃ­neas y extraer el nombre del programa
        for line in lines[3:-1]:  # Ignorar las primeras 3 lÃ­neas de encabezado y la Ãºltima lÃ­nea vacÃ­a
            program_name = line.split()[0]
            programs.append(program_name)

        return programs
    except Exception as e:
        print(f"Error al obtener la lista de programas abiertos: {e}")
        return []

def connected_devices():
    # Dispositivos conectados
    try:
        subprocess.check_call(r'reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2', shell=True)
    except subprocess.CalledProcessError:
        print("Error al ejecutar el comando de dispositivos conectados")

def system_logs(hours_ago):
    powershell_command = f"""
    $hoursAgo = {hours_ago}
    Get-WinEvent -FilterHashtable @{{Logname='System'; StartTime=(Get-Date).AddHours(-$hoursAgo)}}
    """

    # Ejecuta el comando de PowerShell
    process = subprocess.Popen(
        ["powershell", "-Command", powershell_command],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # Obtiene la salida y los errores del comando
    output, error = process.communicate()

    # Imprime los errores o la salida
    if error:
        print(f"Error: {error.decode()}")
    else:
        print(output.decode())

def login_events():

    try:
        # Este comando obtendrÃ¡ los 5 eventos de inicio de sesiÃ³n mÃ¡s recientes
        subprocess.check_call(r'wevtutil qe Security /q:"*[System[(EventID=4624)]]" /c:5 /rd:true /f:text', shell=True)
    except subprocess.CalledProcessError:
        print("Error al ejecutar el comando de eventos de inicio de sesiÃ³n")

def main():
    parser = argparse.ArgumentParser(description='Forensic tool')
    parser.add_argument('-b', '--branch', action='store_true', help='Get recent registration branch change dates')
    parser.add_argument('-r', '--recent', action='store_true', help='Get recent files')
    parser.add_argument('-i', '--installed', action='store_true', help='Get installed programs')
    parser.add_argument('-a', '--active', action='store_true', help='Get active programs')
    parser.add_argument('-n', '--nav', action='store_true', help='Show only browser history')
    parser.add_argument('-c', '--connected', action='store_true', help='Get connected devices')
    parser.add_argument('-l', '--logs', action='store_true', help='Get system log events')
    parser.add_argument('-L', '--login', action='store_true', help='Get user login events')
    parser.add_argument('-t', '--time', type=int, default=24, help='Specify time range in hours. Default is 24 hours')
    args = parser.parse_args()

    now = datetime.now()

    # Calcular la fecha y hora de inicio basada en el rango de tiempo proporcionado
    start_time = now - timedelta(hours=args.time)


    # AsegÃºrate de que se ha proporcionado al menos una opciÃ³n
    if not any([args.branch, args.recent, args.installed, args.active,args.nav, args.connected, args.logs, args.login]):
        print("Por favor, proporciona al menos una opciÃ³n")
        return

    if args.branch:
        registry_changes(args.time)
    if args.recent:
        recent_files(args.time)
    if args.installed:
        installed_programs(args.time)

    if args.active:
        programs = get_open_programs()
        for program in programs:
            print("Programa:", program)

    if args.nav:
        get_all_browsers_history(args.time)

    if args.connected:
        connected_devices()
    if args.logs:
        hours_ago=args.time if args.time else 24
        system_logs(hours_ago)

    if args.login:
        login_events()

if __name__ == "__main__":
    main()
