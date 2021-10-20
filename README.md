# Proyecto de Multiprocesos   -  Guía de Uso
Este proyecto fue creado en Python utilizando Yolov3.
Se realiza un análisis de archivos de vídeo. En un inicio vamos a considerar películas o vídeos con una duración igual o superior a los 60 minutos. El repositorio esta conformado por múltiples archivos. Implementaremos multiprocesamiento a nivel del repositorio y a cada archivo (multiproceso para cada archivo).



## Instalación
1. Instalar [Python 3.7.0](https://www.python.org/downloads/release/python-370/) o Superior
2. Para el uso del programa se solicitan diferentes modulos entre ellas `cv2`, `numpy`, `pip` y otras que el [IDE Pycharm](https://www.jetbrains.com/es-es/pycharm/download/#section=windows) le indica y le facilita la instalación.
3. Un metodo de instalación comun es el `pip install "nombre"`
 ![image](https://user-images.githubusercontent.com/38516078/137266603-be925b19-62c4-4d0c-9248-d79e8f6bedf2.png)
4. Para la creación de graficos con los resultados se recomienda importar el siguiente modulo de la siguiente forma: 
```plain
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

```


4. Se requieren los archivos `yolov3.cfg` y `yolov3.weight`. Para el `yolov3.weight` se obtiene del siguiente link 

## Ejecución
La ejecución funciona de la siguiente manera:

* Se realiza la lectura del los videos, estos son procesados mediante la inteligencia de `yolov3.cfg` y `yolov3.weight` los cuales requieren conocer los objetos que se buscan, por lo tanto, se utiliza el archivo  `obj.names` el cual contiene los elementos: rifle, gun y fire.

* ![image](https://user-images.githubusercontent.com/38516078/137435172-512d5410-753a-4e32-a8c2-2b83f1884231.png)
* ![image](https://habrastorage.org/webt/cl/rf/_j/clrf_jqzkt1qfszivfchhxkujv4.png )


## Pruebas
La ejecución del programa en Python analizó una película entera de aproximadamente una hora y 35 minutos, de la cual se obtuvieron varios resultados, entre ellos el programa realizó unas graficas que se mostrarán en el siguiente apartado y además algunos objetos fueron reconocidos por la inteligencia de Yolo, estos son los que es capaz de reconocer por los previos entrenamientos según su categoría.
Algunos ejemplos son : 
Prueba de la detección de fuego 
![Fire2982](https://user-images.githubusercontent.com/47863265/137429292-f8f34273-d851-4311-b665-2b4946b46410.png)

Prueba de la detección de una pistola
![Gun926](https://user-images.githubusercontent.com/47863265/137429409-84fcbc37-5cf7-4a28-a629-3504b0b6d6ef.png)

Prueba de la detección de un rifle
![Rifle4840](https://user-images.githubusercontent.com/47863265/137429452-7c562934-16f5-4c54-9aef-40343404d15e.png)

-----------------------------Resultados--------------------------
![ResultadosParalelos](https://user-images.githubusercontent.com/38516078/138137247-9ffe53ab-94fe-48f1-a36d-4cedb0bdc8b1.PNG)


![borrar1](https://user-images.githubusercontent.com/38516078/138139587-98d9f959-7180-4424-ae2f-ee30eeecc6ac.png)
![c2](https://user-images.githubusercontent.com/38516078/138140353-15af031d-2b70-4f0a-8bed-a49ff5ed68ed.jpg)
![c3](https://user-images.githubusercontent.com/38516078/138141040-68226244-2d20-4249-8778-763920917709.png)
![c4](https://user-images.githubusercontent.com/38516078/138144551-5310b2a9-6684-4365-9779-3c33a0ebc108.png)




## Resultados
De las Gráficas ya mencionadas previamente se obtiene algunos resultados.
Estos son las graficas creadas por el mismo código:  
![Video2TiemposAparición](https://user-images.githubusercontent.com/47863265/137416102-abf55165-8d42-4b3a-b7e3-aafc34d73ed8.png)
![Video2CantidadApariciones](https://user-images.githubusercontent.com/47863265/137416112-38090e76-bb5c-4c7e-a9c9-e77943debfd6.png)
