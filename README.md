# Server Client Communication 📡

Este es un simple script en Python para establecer una comunicación básica entre servidor y cliente utilizando sockets.

## Funcionalidades 🚀

- **Establecimiento de Conexión:** El servidor crea un socket TCP IPv4 y espera conexiones entrantes en una dirección IP y puerto específicos.
- **Envío de Mensajes:** Una vez que se establece la conexión con un cliente, el servidor envía un mensaje de saludo.
- **Interacción con el Cliente:** Después de establecer la conexión, el servidor entra en un shell interactivo donde puede recibir comandos del cliente y ejecutarlos.

## Uso 🛠️

### Lado del Servidor:

1. Ejecuta el script `server.py`.
3. Una vez que se establezca una conexión, enviará un mensaje de saludo al cliente.
4. Después de establecer la conexión, el servidor entrará en un shell interactivo donde puede recibir comandos del cliente.

### Lado del Cliente:

1. Ejecuta el script `client.py`.
3. Después de establecer la conexión, el cliente enviará un mensaje de saludo al servidor.
4. Luego, el cliente esperará recibir comandos del servidor y los ejecutará.

## Dependencias 📦

- Se requiere Python instalado en el sistema.
- La biblioteca `termcolor` se utiliza para la salida en color en el lado del servidor. Puedes instalarla usando `pip install termcolor`.

## Desarrollador 👨‍💻

Este proyecto fue desarrollado por Fdev.

## Notas Importantes ℹ️

- Asegúrate de ajustar la dirección IP y el puerto en ambos scripts de acuerdo con la configuración de tu red.
- Esta es una implementación básica y puede requerir mejoras para su uso a nivel de producción, como manejo de errores, autenticación y encriptación.
