import pandas as pd
import numpy as np

def limpiar_datos_produccion(df_raw):
    if df_raw is None:
        return None
    
    # La primera fila contiene los años como cabeceras reales
    headers = df_raw.iloc[0].values
    df = df_raw.iloc[1:].copy()
    df.columns = headers
    df.rename(columns={df.columns[0]: 'PRODUCTO'}, inplace=True)
    
    # Limpiar espacios en blanco en productos
    df['PRODUCTO'] = df['PRODUCTO'].astype(str).str.strip()
    
    # Reemplazar 'n.d.' por NaN y convertir valores a numéricos
    for col in df.columns[1:]:
        df[col] = pd.to_numeric(df[col].astype(str).str.replace('n.d.', 'nan', case=False), errors='coerce')
        
    df = df.dropna(subset=['PRODUCTO'])
    return df