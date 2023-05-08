# Variables con las rutas de OpenSSL
OPENSSL_INC = /opt/homebrew/opt/openssl@1.1/include
OPENSSL_LIB = /opt/homebrew/opt/openssl@1.1/lib

# Opciones de compilación
CFLAGS = -Werror -Wall -Wextra -I$(OPENSSL_INC)
LDFLAGS = -L$(OPENSSL_LIB) -lssl -lcrypto

# Objetivo predeterminado
all: corsair

# Regla de compilación del programa
corsair: ft_corsair.c
	gcc -o $@ $< $(CFLAGS) $(LDFLAGS)

# Regla para limpiar los archivos objeto y el ejecutable
clean:
	rm -f corsair

# Regla para eliminar todos los archivos generados por el Makefile
distclean: clean
	rm -f *~

