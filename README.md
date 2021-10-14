# Proyecto de Multiprocesos
Este proyecto fue creado en Python utilizando Yolov3.
Se realiza un análisis de archivos de vídeo. En un inicio vamos a considerar películas o vídeos con una duración superior a los 60 minutos. El repositorio debe estar conformado por múltiples archivos. Implementaremos multiprocesamiento a nivel del repositorio y a cada archivo (multiproceso para cada archivo).

## Instalación
1. Para el uso del programa se instalan diferentes bibliotecas que se instalan entre ellas `cv2`, `numpy`, `pip` y otras que el IDE pycharm le indica y le facilita la intalación.
2. Se requieren los archivos `yolov3.cfg` y `yolov3.weight`. Para el `yolov3.weight` se obtiene del siguiente link 

## Ejecución
La ejecución funciona de la siguiente manera:
* Se realiza la lectura del los videos, estos son procesados mediante la inteligencia de `yolov3.cfg` y `yolov3.weight` los cuales requieren conoce los objetos que se buscan por lo tanto requieren el archivo  `obj.names` el cual contiene los elementos: rifle, gun y fire.
## Pruebas
## Resultados
