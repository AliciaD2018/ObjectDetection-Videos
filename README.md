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


![image](https://user-images.githubusercontent.com/38516078/138114607-57dd1f0c-5d12-43c3-bb08-3ea86068d146.png = 250x250)
![image](https://user-images.githubusercontent.com/38516078/138114700-865cdd80-4709-44e4-9546-acd68fb1a218.png = 250x250)


![image](https://user-images.githubusercontent.com/38516078/138116471-2edd5fc5-57fb-4568-a789-96cbf99384e1.png)
![image](https://user-images.githubusercontent.com/38516078/138116509-a39b0a7c-28a6-4d4f-b419-f452d93b68b4.png)


![Video3CantidadApariciones](https://user-images.githubusercontent.com/38516078/138116549-e384220a-ba8e-4b3e-ad95-ce152b1d3ac1.png)
![image](https://user-images.githubusercontent.com/38516078/138116584-a8710f37-b290-45bd-8e69-481020a9176a.png)


![image](https://user-images.githubusercontent.com/38516078/138117566-aa484da7-3267-4fe7-9087-06a8a5b69143.png)
![image](https://user-images.githubusercontent.com/38516078/138118090-0666ec85-f23c-4dd6-9214-d4808154af1e.png)




## Resultados
De las Gráficas ya mencionadas previamente se obtiene algunos resultados.
Estos son las graficas creadas por el mismo código:  
![Video2TiemposAparición](https://user-images.githubusercontent.com/47863265/137416102-abf55165-8d42-4b3a-b7e3-aafc34d73ed8.png)
![Video2CantidadApariciones](https://user-images.githubusercontent.com/47863265/137416112-38090e76-bb5c-4c7e-a9c9-e77943debfd6.png)
