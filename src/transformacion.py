import pandas as pd

def transformar_a_formato_largo(df, id_col='PRODUCTO', var_name='AÑO', value_name='VALOR'):
    if df is None:
        return None
    
    # Seleccionar columnas de años
    anios_cols = [col for col in df.columns if col != id_col]
    
    df_long = pd.melt(df, id_vars=[id_col], value_vars=anios_cols, 
                      var_name=var_name, value_name=value_name)
    
    df_long[var_name] = pd.to_numeric(df_long[var_name], errors='coerce')
    df_long = df_long.dropna(subset=[var_name, value_name])
    return df_long