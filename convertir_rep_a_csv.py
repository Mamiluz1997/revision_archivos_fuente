import csv
import os

# Directorio raíz donde se encuentran las carpetas con los archivos .rep
directorio_raiz = 'archivos'

# Carpeta de salida para los archivos CSV
directorio_informe = 'informe'

# Carpeta específica a procesar (en este caso, 'M0024')
carpeta_especifica = 'M0024'

# Extensión de los archivos a convertir
extension_entrada = '.rep'
extension_salida = '.csv'

# Crear la carpeta "informe" si no existe
if not os.path.exists(directorio_informe):
    os.mkdir(directorio_informe)

# Función para convertir un archivo .rep a CSV
def convertir_rep_a_csv(input_file, output_folder):
    # Obtener la extensión del archivo de entrada
    extension_entrada = os.path.splitext(input_file)[1]

    # Verificar si el archivo de entrada tiene la extensión .rep
    if extension_entrada == '.rep':
        # Construir la ruta completa del archivo de salida
        output_file = os.path.splitext(os.path.basename(input_file))[0] + '.csv'
        output_path = os.path.join(output_folder, output_file)

        with open(input_file, 'r') as file_in, open(output_path, 'w', newline='') as file_out:
            # Utilizar un lector de CSV para separar datos
            reader = csv.reader(file_in, delimiter='\t')

            # Leer la primera línea (cabecera) del archivo .rep
            header = next(reader)

            # Crear un escritor de CSV para escribir en el archivo de salida
            writer = csv.writer(file_out)

            # Escribir la cabecera como una lista de columnas
            writer.writerow(header[0].split(','))

            # Copiar los datos del archivo .rep al archivo CSV
            for row in reader:
                writer.writerow(row[0].split(','))

        print(f'{input_file} convertido y guardado en {output_path}')
    else:
        print(f'Skipping {input_file}: No tiene la extensión .rep.')

# Función para procesar los archivos en una carpeta
def procesar_carpeta(carpeta):
    for root, _, files in os.walk(carpeta):
        for archivo in files:
            archivo_completo = os.path.join(root, archivo)
            if os.path.exists(archivo_completo) and archivo_completo.endswith(extension_entrada):
                convertir_rep_a_csv(archivo_completo, directorio_informe)

# Procesar la carpeta específica (en este caso, 'M0024')
carpeta_especifica = os.path.join(directorio_raiz, carpeta_especifica)
procesar_carpeta(carpeta_especifica)

print('Conversión completada. Los archivos CSV se encuentran en la carpeta "informe".')
