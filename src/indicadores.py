import pandas as pd
import os

def calcular_indicadores(input_path="datos/procesados/dataset_limpio.csv", output_path="resultados/indicadores.csv"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df = pd.read_csv(input_path)
    
    indicadores = {}
    
    # Indicador 1: Producción Total Acumulada
    indicadores['Produccion_Total_TM'] = df['PRODUCCION_TM'].sum()
    
    # Indicador 2: Producción Promedio Anual
    indicadores['Produccion_Promedio_TM'] = df['PRODUCCION_TM'].mean()
    
    # Indicador 3: Valor Máximo de Producción Registrado
    indicadores['Produccion_Maxima_TM'] = df['PRODUCCION_TM'].max()
    
    # Indicador 4: Cantidad Total de Registros Analizados
    indicadores['Total_Registros'] = len(df)
    
    # Indicador 5: Desviación Estándar de la Producción
    indicadores['Desviacion_Estandar_TM'] = df['PRODUCCION_TM'].std()
    
    # Guardar indicadores en un DataFrame y exportar a CSV
    df_indicadores = pd.DataFrame(list(indicadores.items()), columns=['Indicador', 'Valor'])
    df_indicadores.to_csv(output_path, index=False)
    
    print(f"[INFO] Indicadores calculados y guardados exitosamente en {output_path}")

if __name__ == "__main__":
    calcular_indicadores()