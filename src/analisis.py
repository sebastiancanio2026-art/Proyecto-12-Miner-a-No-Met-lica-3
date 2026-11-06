import pandas as pd

def analizar_dataset(df, nombre="Dataset"):
    print(f"\n--- ANÁLISIS ESTADÍSTICO: {nombre} ---")
    if df is None:
        print("No hay datos para analizar.")
        return

    print(f"Dimensiones (Filas, Columnas): {df.shape}")
    print(f"Cantidad de valores nulos totales: {df.isna().sum().sum()}")
    print(f"Filas duplicadas: {df.duplicated().sum()}")
    
    # Resumen estadístico básico
    print("\nResumen descriptivo (primeras columnas numéricas):")
    print(df.describe().iloc[:, :5])