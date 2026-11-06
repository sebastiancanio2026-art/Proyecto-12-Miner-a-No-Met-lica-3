import pandas as pd

def cargar_excel(ruta, skiprows=2):
    """
    Carga un archivo Excel de Cochilco/Aduanas manejando errores estándar.
    """
    try:
        xls = pd.ExcelFile(ruta)
        # Si tiene múltiples hojas (como exportaciones), cargamos la principal
        sheet_name = 'Exportaciones' if 'Exportaciones' in xls.sheet_names else xls.sheet_names[0]
        df_raw = pd.read_excel(ruta, sheet_name=sheet_name, skiprows=skiprows)
        return df_raw
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta '{ruta}'.")
    except Exception as e:
        print(f"Error al leer el archivo {ruta}: {e}")
    return None

def cargar_todos_los_datos():
    """
    Carga los tres datasets principales del proyecto.
    """
    ruta_prod = "datos/Produccion-Mineria-No-Metalica-1996-2025.xlsx"
    ruta_exp_fis = "datos/Exportaciones-Fisicas-Por-Destino-Mineria-No-Metalica-2002-2025.xlsx"
    ruta_exp_val = "datos/Exportaciones-Valorizadas-Por-Destino-Mineria-No-Metalica-2002-2025 (1).xlsx"

    df_prod = cargar_excel(ruta_prod, skiprows=2)
    df_exp_fis = cargar_excel(ruta_exp_fis, skiprows=3)
    df_exp_val = cargar_excel(ruta_exp_val, skiprows=3)

    return df_prod, df_exp_fis, df_exp_val