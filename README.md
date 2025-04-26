# Proyecto de Carga de Archivos de Texto Plano

Este proyecto es una aplicación desarrollada con Django que permite cargar archivos de texto plano y valida que cada registro del archivo tenga el formato correcto, con 5 columnas por registro.

## Tecnologías utilizadas

- **Python 3.x**
- **Django 5.2**

## Instalación

Para ejecutar este proyecto en tu entorno local, sigue estos pasos:

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Katsbriell/django-project

2. Entra en la carpeta del proyecto:
   ```bash
   cd django-project

3. Crear un entorno virtual
- Windows
   ```bash
   python -m venv env
   env\Scripts\activate
- Linux/Mac
  ```bash
  python -m venv env
  source env/bin/activate
4. Instalar dependencias
   ```bash
   pip install r requirements.txt

5. Correr el servidor
   ```bash
   python manage.py runserver
6. Abrir la aplicación en el navegador con: http://127.0.0.1:8000/index/

## Uso 
Esta aplicación permite cargar un archivo .txt para validar su formato de registros que contienen 5 columnas, siguiendo las siguientes reglas:
- El archivo solo debe permitir las 5 columnas, si existen más o menos
deberá alertar al usuario
- Columna 1: Solo debe permitir números enteros entre 3 y 10 caracteres
- Columna 2: Solo debe permitir correos electrónicos
- Columna 3: Solo debe permitir los valores “CC” o “TI”
- Columna 4: Solo debe permitir valores entre 500000 y 1500000
- Columna 5: Permite cualquier valor
