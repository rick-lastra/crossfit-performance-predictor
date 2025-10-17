# crossfit-performance-predictor
AI model to predict CrossFit athlete performance using historical data and IBM Watson.
Modelo Predictivo de Rendimiento para Atletas de CrossFit
Descripción General
Este proyecto utiliza Machine Learning para predecir el rendimiento de un atleta de CrossFit basándose en más de 900 registros históricos de entrenamiento. El modelo fue desarrollado como parte de la Maestría en Inteligencia Artificial de la Universidad TecMilenio en colaboración con IBM, y fue entrenado y desplegado utilizando el ecosistema de IBM Cloud.

Planteamiento del Problema
El objetivo es optimizar el plan de entrenamiento de un atleta mediante la predicción de resultados en futuros WODs (Workout of the Day). Esto permite identificar patrones de rendimiento, determinar áreas críticas de mejora y minimizar el riesgo de sobreentrenamiento, aplicando la metodología ASUM-DM para alinear los objetivos técnicos con las metas deportivas.   

Stack Tecnológico y Librerías
Lenguaje: Python

Librerías Principales: Pandas, NumPy, Scikit-learn, Matplotlib, Requests

Plataforma Cloud: IBM Cloud

Herramientas de IA: IBM Watson Studio, AutoAI, Watson Machine Learning

Entorno de Desarrollo: Jupyter Notebooks (Google Colab)

Estructura del Proyecto
crossfit_predictor.ipynb: El notebook de Jupyter que contiene todo el proceso, desde la limpieza de datos hasta el consumo de la API del modelo desplegado.

workouts.csv: El conjunto de datos original con más de 900 registros de entrenamientos.

requirements.txt: Las dependencias de Python necesarias para ejecutar el proyecto.

Fases del Proyecto
El desarrollo siguió un ciclo de vida de Machine Learning estructurado:

Ingeniería de Datos: Se realizó la recolección, limpieza y transformación de los datos con Python y Pandas. Se implementaron funciones para estandarizar diversos formatos de resultados (tiempos, repeticiones) en valores numéricos.   

Modelado Automatizado: Se utilizó IBM Watson Studio y AutoAI para entrenar y evaluar múltiples algoritmos de regresión. El modelo Random Forest Regressor fue seleccionado como el de mayor precisión.   

Despliegue en la Nube: El modelo final fue desplegado como un punto final de API en línea a través de IBM Watson Machine Learning, listo para realizar inferencias en tiempo real.   

Consumo de la API: Se desarrolló un script en Python para autenticarse con IBM Cloud y enviar datos de nuevos entrenamientos a la API, recibiendo una predicción de rendimiento como respuesta.

Cómo Ejecutar el Proyecto
Clona este repositorio:bash git clone https://github.com/tu-usuario/crossfit-performance-predictor.git

Navega a la carpeta del proyecto:

Bash

cd crossfit-performance-predictor
(Opcional pero recomendado) Crea un entorno virtual:

Bash

python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
Instala las dependencias:

Bash

pip install -r requirements.txt
Abre el notebook crossfit_predictor.ipynb en Jupyter o Google Colab para ver el análisis y el código.

Resultados Clave
El modelo desplegado es capaz de recibir las características de un nuevo WOD (ej. "Fran", "21-15-9 thrusters and pull-ups") y devolver una predicción numérica del resultado esperado, demostrando un pipeline de IA funcional de extremo a extremo.   
