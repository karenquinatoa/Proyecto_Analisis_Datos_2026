import pandas as pd
import os

# Tu ruta exacta:
ruta = r'C:\Users\USUARIO\Documents\GitHub\Proyecto_Analisis_Datos_2026\data\raw\nucleos_rs18.csv'

# Verificación de seguridad
if os.path.exists(ruta):
    print("¡Archivo encontrado! Cargando datos...")
    
    # Intentamos leer el archivo
    df = pd.read_csv(ruta, sep=',', encoding='latin-1')
    
    # Resultados
    print("-" * 30)
    print(f"El archivo tiene {df.shape[0]} filas y {df.shape[1]} columnas.")
    print("-" * 30)
    print("Aquí tienes las primeras 5 filas:")
    print(df.head())
else:
    print(f"Error: Aún no encuentro el archivo. Por favor verifica que el archivo realmente esté en: {ruta}")