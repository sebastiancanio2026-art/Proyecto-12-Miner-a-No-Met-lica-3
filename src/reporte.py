import matplotlib.pyplot as plt
import os

def generar_grafico_produccion(df_long):
    if df_long is None or df_long.empty:
        return
    
    os.makedirs("reportes", exist_ok=True)
    
    # Agrupar por año sumando toda la producción nacional no metálica usando 'PRODUCCION_TM'
    df_agrupado = df_long.groupby('AÑO')['PRODUCCION_TM'].sum().reset_index()
    
    plt.figure(figsize=(10, 5))
    plt.plot(df_agrupado['AÑO'], df_agrupado['PRODUCCION_TM'], marker='o', color='teal', linewidth=2)
    plt.title('Evolución de la Producción de Minería No Metálica en Chile')
    plt.xlabel('Año')
    plt.ylabel('Toneladas Métricas')
    plt.grid(True, linestyle='--', alpha=0.6)
    
    ruta_figura = 'reportes/evolucion_produccion.png'
    plt.savefig(ruta_figura, bbox_inches='tight')
    plt.close()
    print(f"Gráfico guardado exitosamente en: {ruta_figura}")