# Proyecto ded Reconocimiento Facial con Django

Este proyecto es una aplicación de reconocimiento facial desarrollada con Django, que utiliza `ultralytics` (YOLOv8) y
OpenCV `cv2` para la captura y procesamiento de imágenes. El proyecto también se integra con Roboflow para la gestión de datasets.

## Requisitos Previos
 
- **Anaconda**. Utilizar el navegador de Anaconda para gestionar los entornos virtuales
- **Python 3.8**. Asegúrate de tener Python instalado.
- **Cuenta en Roboflow**. Necesitarás una cuenta de Roboflow para descargar el dataset y etiquetar las imágenes.

## Configuración del entorno

1. **Instalación de Anaconda**. Si no tienes Anonda instalado, puedes descargarlo e instalarlo desde [aqui](anaconda.com/products/navigator)
2. **Configuración del entorno virtual**. Una vez instalado Anaconda, abre una terminal (CMD, Git Bash, Power Shell, etc) y crea un nuevo entorno virtual para el proyec
```
conda create --name venv python=3.8
```
3. **Activar el entorno virtual**
```
conda activate venv
```
4. **Instalación de Dependencias**. Con el entorno virtual activado, instala las librerías necesarias:
```
pip install django ultralytics opencv-python-headless torch
```

# Ejecución del Proyecto
Para ejecutar el servidor Django, asegúrate de estar en el directorio raíz de tu proyecto y luego corre:
```
python manage.py runserver
```

# Entrenamiento de IA
Para poder realizar el entrenamiento, es necesario tener descargado el dataset generado por Roboflow.
Una vez instalado el dataset, asegurate que en el archivo *train.py* se encuentre la ruta relativa (o absoluta) donde esté ubicado tu dataset, hasta llegar al archivo **data.yaml**

El archivo **train.py** tiene el código necesario para realizar el entrenamiento. Dependiendo de las capacidades de cada computadora se le asigna lo siguiguiente al entrenamiento:

- epochs: Iteraciones de entrenamiento (Se recomienda entre 50 y 100 para un buen resultado de entrenamiento)
- batch: Cuantas imágenes se procesarán juntas en cada paso de entrenamiento

Teniendo todas las configuraciones listas, se manda a correr el archivo train.py para generar el modelo entrenado

### Pdt.  Si cuentas con una GPU, se le agrega al entrenamiento el valor device=0 para que la utilice y sea más rapido el entrenamiento