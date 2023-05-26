#!/bin/bash

# Eliminar la instalación anterior de Homebrew si existe
rm -rf "$HOME/.brew"

# Clonar Homebrew en el directorio de goinfre
git clone https://github.com/Homebrew/brew "$HOME/goinfre/.brew"

# Agregar el directorio de Homebrew al PATH en el archivo .zshrc
echo 'export PATH="$HOME/goinfre/.brew/bin:$PATH"' >> "$HOME/.zshrc"
source "$HOME/.zshrc"

# Actualizar Homebrew e instalar openssl@1
brew update
#brew install vagrant
