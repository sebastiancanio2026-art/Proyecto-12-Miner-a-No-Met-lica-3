from src.carga import cargar_todos_los_datos
from src.limpieza import limpiar_datos_produccion
from src.transformacion import transformar_a_formato_largo
from src.analisis import analizar_dataset
from src.reporte import generar_grafico_produccion

# Importamos correctamente los nuevos módulos del Avance 3 desde src
from src.estadistica import calcular_estadisticas
from src.indicadores import calcular_indicadores
from src.visualizaciones import generar_graficos

def main():
    print("=== Iniciando pipeline de análisis para Minería No Metálica ===")
    
    # 1. Carga
    df_prod_raw, df_exp_fis, df_exp_val = cargar_todos_los_datos()
    
    # 2. Limpieza
    df_prod_limpio = limpiar_datos_produccion(df_prod_raw)
    
    # 3. Análisis Inicial
    analizar_dataset(df_prod_limpio, nombre="Producción Minería No Metálica")
    
    # 4. Transformación y guardado del dataset limpio para el Avance 3
    df_prod_long = transformar_a_formato_largo(df_prod_limpio, id_col='PRODUCTO', var_name='AÑO', value_name='PRODUCCION_TM')
    df_prod_long.to_csv("datos/procesados/dataset_limpio.csv", index=False)
    
    # 5. Reporte y Visualización anterior
    generar_grafico_produccion(df_prod_long)
    
    # --- 6. NUEVAS FUNCIONALIDADES DEL AVANCE N° 3 ---
    print("\n[AVANCE 3] Calculando estadísticas descriptivas...")
    calcular_estadisticas(input_path="datos/procesados/dataset_limpio.csv", output_path="resultados/estadisticas.csv")
    
    print("[AVANCE 3] Calculando indicadores automatizados...")
    calcular_indicadores(input_path="datos/procesados/dataset_limpio.csv", output_path="resultados/indicadores.csv")
    
    print("[AVANCE 3] Generando gráficos obligatorios (PNG)...")
    generar_graficos(input_path="datos/procesados/dataset_limpio.csv", output_dir="resultados/graficos/")
    
    print("\n¡Pipeline ejecutado exitosamente!")

if __name__ == "__main__":
    main()