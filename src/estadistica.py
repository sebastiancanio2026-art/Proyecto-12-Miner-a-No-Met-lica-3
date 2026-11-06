import pandas as pd
import os

def calcular_estadisticas(input_path="datos/procesados/dataset_limpio.csv", output_path="resultados/estadisticas.csv"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df = pd.read_csv(input_path)
    
    # Estadísticas descriptivas generales para variables numéricas (PRODUCCION_TM, AÑO)
    desc_num = df.describe(include=['float64', 'int64']).T
    desc_num['rango'] = desc_num['max'] - desc_num['min']
    
    # Cuartiles específicos si no vienen incluidos
    desc_num['q25'] = df.select_dtypes(include=['number']).quantile(0.25)
    desc_num['q50 (mediana)'] = df.select_dtypes(include=['number']).quantile(0.50)
    desc_num['q75'] = df.select_dtypes(include=['number']).quantile(0.75)
    
    # Guardar en CSV
    desc_num.to_csv(output_path)
    print(f"[INFO] Estadísticas descriptivas guardadas en {output_path}")
    return desc_num

if __name__ == "__main__":
    calcular_estadisticas()