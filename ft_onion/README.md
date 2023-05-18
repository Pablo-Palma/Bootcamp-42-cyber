# README - Proyecto ft_onion

¡Bienvenido a **ft_onion**! Este proyecto consta de una página web estática accesible a través de una URL .onion, un servidor web Nginx, un acceso al servidor por SSH en el puerto 4242, y sin abrir ningún otro puerto ni establecer reglas de firewall.

## Archivos de Configuración

1. **index.html**: Esta es la página web estática a la que se accederá a través de la URL .onion.

2. **nginx.conf**: Este archivo contiene las configuraciones del servidor web Nginx. 

3. **sshd_config**: Aquí se encuentran las configuraciones de acceso al servidor por SSH en el puerto 4242.

4. **torrc**: Este archivo se utiliza para configurar el servicio oculto de Tor que permite el acceso a la página web a través de la URL .onion.

## Instrucciones de Uso

1. Asegúrate de tener instalado Nginx, OpenSSH y Tor en tu servidor.

2. Clona este repositorio en tu servidor.

3. Copia los archivos de configuración en sus respectivos directorios: 
   - nginx.conf a /etc/nginx/nginx.conf 
   - sshd_config a /etc/ssh/sshd_config 
   - torrc a /etc/tor/torrc

4. Reinicia Nginx, OpenSSH y Tor para que las nuevas configuraciones se apliquen.

5. La página web debe ser accesible a través de la URL .onion en el puerto 80 y debes ser capaz de acceder al servidor por SSH en el puerto 4242.
