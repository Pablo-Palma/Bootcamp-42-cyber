#!/bin/bash

# Instalar python3-venv
sudo apt install python3-venv -y

# Instalar python3-pip
sudo apt install python3-pip -y

# Instalar python3-crypto
sudo apt install python3-crypto -y

# Instalar pycryptodomex
python3 -m pip install pycryptodomex

# Mostrar mensaje de instalación completada
echo "Instalación completada."

