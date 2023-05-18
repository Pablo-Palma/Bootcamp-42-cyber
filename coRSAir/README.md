# coRSAir

Bienvenido a la sección coRSAir. Aquí encontrarás el código para coRSAir, una herramienta de desencriptación RSA.

## Requisitos
* OpenSSL
* GCC

## Estructura del Repositorio
```
.
├── ft_corsair.c
├── ft_corsair.h
└── Makefile
```

## Compilación
coRSAir utiliza OpenSSL, asegúrate de tenerlo instalado en tu sistema. Para compilar el código, ejecuta el siguiente comando en el directorio raíz del repositorio:
```sh
make
```

## Uso
Una vez compilado, puedes ejecutar coRSAir con el siguiente comando:

```sh
./corsair <lista de archivos.pem>
```

Esta herramienta recorre la lista de archivos.pem proporcionada, buscando claves públicas RSA que compartan un factor primo. Cuando encuentra un par, desencripta el contenido del archivo asociado con la clave y muestra el contenido desencriptado.

## Limpieza
Para limpiar los archivos generados durante la compilación, puedes usar el siguiente comando:

```sh
make clean
```

## Notas
- Este programa es solo para fines educativos. Úsalo responsablemente.
- Si encuentras algún problema, siéntete libre de abrir una Issue.
