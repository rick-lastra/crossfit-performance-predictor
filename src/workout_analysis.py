"""Python code exported from the course project workflow notebook. Review paths and data access before use."""

#1. Importar las librerias de NumPy, Pandas y Matplotlib.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#2. Importar mi fichero de datos
print("Cargando el archivo workouts.csv...")
#3. Genera un dataframe con los datos incluidos en el fichero
crossfit_df = pd.read_csv('workouts.csv')
print("Fichero cargado correctamente.")
print(crossfit_df)

# Organiza la información dentro de Dataframe de la forma que mejor se adecue a la
# problemática que se desea analizar, modifica el tipo de variable en caso de ser necesario.

#revisar el tipo de datos
crossfit_df.dtypes

#Valores NO NULOS de cada característica o columna
crossfit_df.count()

#Determinar los valores faltantes
crossfit_df.isnull().sum()

# Genera estadísticas descriptivas excluyendo los datos NaN
crossfit_df.describe()

# --- Organización y Limpieza del DataFrame ---
print("\n--- Limpieza y Organización de Datos ---")

# Convertir la columna 'date' a un formato de fecha real (datetime)
crossfit_df['date'] = pd.to_datetime(crossfit_df['date'])
crossfit_df.head(10)

# Seleccionar solo las columnas más relevantes para este análisis inicial
# Basado en la earlier project workflow, estas columnas son las más importantes
columnas_relevantes = ['date', 'title', 'score_type', 'best_result_display', 'rx_or_scaled']
crossfit_df_limpio = crossfit_df[columnas_relevantes].copy()
crossfit_df_limpio.head(10)

# Eliminar filas donde no hay un resultado registrado ('best_result_display' es nulo)
crossfit_df_limpio.dropna(subset=['best_result_display'], inplace=True)

# Reemplazar los valores NaN en 'score_type' por 'For Time'
crossfit_df_limpio['score_type'].fillna('For Time', inplace=True)

print("Tipos de datos después de la limpieza inicial:")
print(crossfit_df_limpio.info())

crossfit_df_limpio.isnull().sum()

crossfit_df_limpio.head(10)

# --- Aplicación de una Función Matemática: Convertir Tiempos a Segundos ---
# El objetivo es analizar entrenamientos medidos por tiempo ('For Time').
# La columna 'best_result_display' contiene texto como "10:02". Necesitamos convertirlo a un número (segundos) para poder analizarlo.
def convertir_a_segundos(tiempo):
    if isinstance(tiempo, str):
        partes = tiempo.split(':')
        if len(partes) == 2: #MM:SS
            try:
                minutos = int(partes[0])
                segundos = int(partes[1])
                return minutos * 60 + segundos
            except ValueError:
                return None
        elif len(partes) == 3: #HH:MM:SS
             try:
                horas = int(partes[0])
                minutos = int(partes[1])
                segundos = int(partes[2])
                return horas * 3600 + minutos * 60 + segundos
             except ValueError:
                return None
        else:
            return None
    else:
        return None

# Filtrar para quedarnos solo con los WODs cuyo resultado es por tiempo
crossfit_df_tiempo = crossfit_df_limpio[crossfit_df_limpio['score_type'] == 'For Time'].copy()

# Aplicar la función a la columna 'best_result_display' para crear una nueva columna 'resultado_en_segundos'
print("\nAplicando función para convertir tiempos a segundos...")
crossfit_df_tiempo['resultado_en_segundos'] = crossfit_df_tiempo['best_result_display'].apply(convertir_a_segundos)

# Convertir la nueva columna a un tipo numérico, coercing errors
crossfit_df_tiempo['resultado_en_segundos'] = pd.to_numeric(crossfit_df_tiempo['resultado_en_segundos'], errors='coerce')

print("Conversión completada.")
print("Tipos de datos después de la conversión de tiempos:")
print(crossfit_df_tiempo.head(10))

# --- ANÁLISIS MUESTRA METROS: ENTRENAMIENTO DE RESISTENCIA (DISTANCIA) ---
import matplotlib.dates as mdates
print("\n--- Análisis y Visualización de Muestra Metros: Resistencia (por Distancia) ---")
df_metros = crossfit_df_limpio[crossfit_df_limpio['score_type'] == 'Meters'].copy()
df_metros['resultado_en_metros'] = pd.to_numeric(df_metros['best_result_display'], errors='coerce')
df_metros.dropna(subset=['resultado_en_metros'], inplace=True)

# Filtrar por entrenamientos que contengan "Bike" en el título para ser consistentes
df_muestra_metros = df_metros[df_metros['title'].str.contains("Bike", na=False)].copy()
df_muestra_metros = df_muestra_metros.sort_values(by='date')

if df_muestra_metros.empty:
    print("No se encontraron datos para entrenamientos de Bike Erg medidos en metros.")
else:
    print(f"\nDatos encontrados para entrenamientos de Bike Erg (por distancia):")
    print(df_muestra_metros[['date', 'title', 'resultado_en_metros']].tail()) # Mostrar los últimos para ver los más recientes
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.plot(df_muestra_metros['date'], df_muestra_metros['resultado_en_metros'], marker='o', linestyle='-', color='#0a9396')
    ax.set_title('Evolución en Entrenamientos de Bike Erg (por Distancia)', fontsize=16, weight='bold')
    ax.set_xlabel('Fecha del Entrenamiento', fontsize=12)
    ax.set_ylabel('Distancia Total (en metros)', fontsize=12)
    fig.autofmt_xdate()
    # Para distancia, un valor más alto es mejor
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Añadir una línea de tendencia
    x_fechas_metros = mdates.date2num(df_muestra_metros['date'])
    z_metros = np.polyfit(x_fechas_metros, df_muestra_metros['resultado_en_metros'], 1)
    p_metros = np.poly1d(z_metros)
    ax.plot(x_fechas_metros, p_metros(x_fechas_metros), "r--", color='#ee9b00', linewidth=2, label='Línea de Tendencia')
    ax.legend()

    print("\nGenerando gráfico de Resistencia (por Distancia)...")
    plt.show()

