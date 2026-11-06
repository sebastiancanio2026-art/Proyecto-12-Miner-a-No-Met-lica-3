import pandas as pd
import matplotlib.pyplot as plt
import os

def generar_graficos(input_path="datos/procesados/dataset_limpio.csv", output_dir="resultados/graficos/"):
    os.makedirs(output_dir, exist_ok=True)
    df = pd.read_csv(input_path)
    
    # Configuración general de estilo
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    
    # --- GRÁFICO 01: Líneas - Evolución temporal del total de producción anual ---
    plt.figure(figsize=(10, 5))
    df_anual = df.groupby('AÑO')['PRODUCCION_TM'].sum().reset_index()
    plt.plot(df_anual['AÑO'], df_anual['PRODUCCION_TM'], marker='o', color='b', linewidth=2)
    plt.title('Evolución Temporal de la Producción Total de Minería No Metálica', fontsize=12, fontweight='bold')
    plt.xlabel('Año', fontsize=10)
    plt.ylabel('Producción Total (Toneladas)', fontsize=10)
    plt.grid(True)
    plt.tight_layout()
    path_g1 = os.path.join(output_dir, 'grafico_01.png')
    plt.savefig(path_g1, dpi=300)
    plt.close()
    
    # --- GRÁFICO 02: Barras - Top 5 productos con mayor producción acumulada ---
    plt.figure(figsize=(10, 5))
    top_productos = df.groupby('PRODUCTO')['PRODUCCION_TM'].sum().nlargest(5).reset_index()
    plt.bar(top_productos['PRODUCTO'], top_productos['PRODUCCION_TM'], color='teal')
    plt.title('Top 5 Productos de Minería No Metálica con Mayor Producción Acumulada', fontsize=12, fontweight='bold')
    plt.xlabel('Producto', fontsize=10)
    plt.ylabel('Producción Acumulada (Toneladas)', fontsize=10)
    plt.xticks(rotation=15)
    plt.tight_layout()
    path_g2 = os.path.join(output_dir, 'grafico_02.png')
    plt.savefig(path_g2, dpi=300)
    plt.close()
    
    # --- GRÁFICO 03: Histograma - Distribución de la Producción ---
    plt.figure(figsize=(10, 5))
    plt.hist(df[df['PRODUCCION_TM'] > 0]['PRODUCCION_TM'], bins=20, color='orange', edgecolor='black')
    plt.title('Distribución de los Volúmenes de Producción Válidos', fontsize=12, fontweight='bold')
    plt.xlabel('Producción (Toneladas)', fontsize=10)
    plt.ylabel('Frecuencia', fontsize=10)
    plt.tight_layout()
    path_g3 = os.path.join(output_dir, 'grafico_03.png')
    plt.savefig(path_g3, dpi=300)
    plt.close()
    
    print(f"[INFO] Gráficos exportados exitosamente en {output_dir}")

if __name__ == "__main__":
    generar_graficos()