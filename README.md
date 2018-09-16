# scrap_utils
Utilidades para Universal XML Scraper
## comp.py
### Introducción
El script *comp.py* sirve para comprimir los archivos mp4 que se encuentran en el mismo directorio que el propio script, muy útil para reducir el tamaño de los vídeos obtenidos al scrapear con Universal XML Scraper. Permite:
- Elegir la duración de los vídeos. Si seleccionamos una duración de 30 s, selecciona los últimos 30 s del vídeo.
- Cambiar la resolución de los vídeos. Si el vídeo original no se ajusta al aspect ratio elegido, centra el vídeo añadiendo franjas negras horizontales o verticales.
- Seleccionar si se quiere con audio o no. Si se quiere con audio, mezcla las dos canales resultando un vídeo con audio monoaural.
- Elegir la calidad resultante de los vídeos.
- Seleccionar el preset, muy útil para hacer pruebas rápidas.
Además, este script es compatible con los sistemas operativos Windows y Linux.

### ¿Qué necesitamos?
- FFmpeg. Se ha utilizado la versión 3.4.4 para probarlo. Se puede descargar de la siguiente web: https://www.ffmpeg.org/ 
- Python 2.7. Se ha utilizado la versión 2.7.10 para probarlo. **ATENCIÓN: No funciona con python 3.X**. Se puede descargar aquí: https://www.python.org/
- Necesitas meter el path de python en la variable del sistema Path. En linux normalmente no hace falta, ya que al instalar python se hace de manera automática. En windows hay que hacerlo a mano. Para ello, ve a propiedades del sistema -> opciones avanzadas -> Variables de entorno. En la sección variables del sistema busca Path y edítala añadiendo el path donde has instalado python.

### ¿Cómo se configura?
El archivo *comp.cfg* sirve para configurarlo. Los valores válidos están indicados dentro de ese mismo archivo.

### ¿Cómo lo hago funcionar?
Copia el script y pégalo en la carpeta donde están los vídeos. Ejecútalo, para ello tienes varias opciones:
- lanza desde la consola de comandos: *python comp.py*
- haz doble click sobre *comp.py*. Si usas linux tendrías que darle permiso de ejecución al archivo y decirle el intérprete que quieres usar, para eso tendrías que añadir al principio del script esta línea:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_#!/usr/bin/python_

El tiempo de ejecución del script depende del nº de vídeos a comprimir, de la configuración y del propio sistema. Recomendable ejecutarlo en un pc, nunca en la raspberry.
Una vez finalizado el script, tendremos los vídeos comprimidos con la extensión mp4. Los vídeos originales se renombran, añadiendo la extensión .bak.

Antes de lanzar la tarea con los vídeos de un sistema completo, es recomendable utilizar un par de vídeos para ajustar el CRF hasta que se alcance el tamaño deseado sin compreter demasiado la calidad. También se recomienda probarlo en el sistema final, ya que no es lo mismo verlo redimensionado a pantalla completa en el pc que en la ventanita que se deja en el front-end.
Para esto, crea una carpeta nueva, selecciona un par de vídeos y el script y pégalo en la nueva carpeta. Ejecuta el script con esos vídeos. Tendrás que borrar los vídeos y renombrar los .bak a .mp4 (o borrarlos y pegar los originales otra vez) para realizar nuevas pruebas.


### Ejemplos de vídeos comprimidos
En el siguiente enlace se pueden encontrar varios vídeos que se han obtenido al ejecutar este script: https://github.com/mirolloeselrock/scrap_utils/tree/master/ejemplos

### Posibles errores
#### The encoder 'aac' is experimental but experimental codecs are not enabled, add '-strict -2' if you want to use it
Tienes una versión antigua de ffmpeg. Si estás en ubuntu puedes instalar una nueva de la siguiente forma:

_sudo add-apt-repository ppa:jonathonf/ffmpeg-3_

_sudo apt-get update_

_sudo apt install ffmpeg libav-tools x264 x265_

También puedes bajarte el paquete necesario de la web ffmpeg.

#### ModuleNotFoundError: No module named 'ConfigParser'
Estás con python 3.x, este script es solo compatible con python 2.7.x
