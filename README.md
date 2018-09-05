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

### ¿Qué necesitamos?
- FFmpeg que podéis encontrar en su página web: https://www.ffmpeg.org/
- Python. Se ha utilizado la versión 2.7.10 para probarlo. Se puede descargar aquí: https://www.python.org/

### ¿Cómo se configura?
El archivo *comp.cfg* sirve para configurarlo. Los valores válidos están indicados dentro de ese mismo archivo.

### ¿Cómo lo hago funcionar?
Copia el script y pégalo en la carpeta donde están los vídeos. Ejecútalo, para ello tienes varias opciones:
- lanza desde la consola de comandos: *python comp.py*
- haz doble click sobre *comp.py*

El tiempo de ejecución del script depende del nº de vídeos a comprimir, de la configuración y del propio sistema. Recomendable ejecutarlo en un pc, nunca en la raspberry.
Una vez finalizado el script, tendremos los vídeos comprimidos con la extensión mp4. Los vídeos originales se renombran, añadiendo la extensión .bak.

Antes de lanzar la tarea con los vídeos de un sistema completo, es recomendable utilizar un par de vídeos para ajustar el CRF hasta que se alcance el tamaño deseado sin compreter demasiado la calidad. También se recomienda probarlo en el sistema final, ya que no es lo mismo verlo redimensionado a pantalla completa en el pc que en la ventanita que se deja en el front-end.
Para esto, crea una carpeta nueva, selecciona un par de vídeos y el script y pégalo en la nueva carpeta. Ejecuta el script con esos vídeos. Tendrás que borrar los vídeos y renombrar los .bak a mp4 (o borrarlos y pegar los originales otra vez) para realizar nuevas pruebas.


### Ejemplos de vídeos comprimidos
En el siguiente enlace se pueden encontrar varios vídeos que se han obtenido al ejecutar este script: https://github.com/mirolloeselrock/scrap_utils/tree/master/ejemplos
