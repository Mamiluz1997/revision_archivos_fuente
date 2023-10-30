import pandas as pd
import os

# Ruta de la carpeta con los archivos CSV de entrada
carpeta_informe = "informe"

# Ruta de la carpeta para guardar los archivos de informe
carpeta_archivos_informe = "archivos_informe"

# Crear la carpeta de informe si no existe
if not os.path.exists(carpeta_archivos_informe):
    os.makedirs(carpeta_archivos_informe)

# Ruta del archivo CSV de salida
archivo_csv_salida = os.path.join(carpeta_archivos_informe, "archivo_informe.csv")

# Inicializar un DataFrame vacío para almacenar los resultados
resultado_df = pd.DataFrame()

# Listar todos los archivos CSV en la carpeta
archivos_csv = [f for f in os.listdir(carpeta_informe) if f.endswith(".csv")]

for archivo_csv in archivos_csv:
    # Imprimir el nombre del archivo en la consola
    print(f"Procesando archivo: {archivo_csv}")

    # Leer el archivo CSV original
    df = pd.read_csv(os.path.join(carpeta_informe, archivo_csv))

    # Seleccionar las columnas deseadas
    columnas_seleccionadas = [
        'fecha',
        '1_29341m',
        '1_29311m',
        '1_29321m',
        '1_9141m',
        '1_9111m',
        '1_9121m',
        '2_18741m',
        '2_18711m',
        '2_18721m'
    ]
    df = df[columnas_seleccionadas]

    # Formatear las fechas válidas y mantener las no válidas
    df['fecha'] = pd.to_datetime(df['fecha'], format='%Y%m%d%H%M%S', errors='coerce')
    df['fecha'] = df['fecha'].apply(lambda x: x.strftime('%m/%d/%Y %H:%M') if not pd.isna(x) else x)

    # Calcular los promedios de las columnas numéricas
    df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')
    promedios = df.iloc[:, 1:].mean()

    # Crear un nuevo DataFrame con la primera fecha y los promedios
    nuevo_df = pd.DataFrame({'fecha': [df.iloc[0, 0]], **promedios})

    # Concatenar el resultado al DataFrame principal
    resultado_df = pd.concat([resultado_df, nuevo_df], ignore_index=True)

# Guardar el DataFrame combinado en un solo archivo CSV
resultado_df.to_csv(archivo_csv_salida, index=False)

print(f"Archivo CSV de informe combinado guardado en: {archivo_csv_salida}")
