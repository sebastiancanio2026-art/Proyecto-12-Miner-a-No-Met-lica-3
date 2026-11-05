# Proyecto: Análisis Automatizado de Minería No Metálica

Este proyecto forma parte de los avances prácticos para el curso de Programación Avanzada. Su objetivo es implementar un pipeline modular en Python para la ingesta, limpieza, transformación, análisis estadístico, cálculo de indicadores y visualización de datos de la minería no metálica.

---

## Estructura del Proyecto

El proyecto está organizado de manera modular bajo el directorio `src/`:

```text
proyecto12/
│
├── datos/
│   ├── procesados/         # Contiene el dataset limpio generado por el pipeline
│   └── [Datasets crudos]   # Archivos de origen (producción y exportaciones)
│
├── resultados/
│   ├── graficos/           # Gráficos generados (PNG)
│   ├── estadisticas.csv    # Resumen de estadísticas descriptivas
│   └── indicadores.csv     # Indicadores automatizados calculados
│
├── src/
│   ├── carga.py            # Módulo de carga de datos iniciales
│   ├── limpieza.py         # Módulo de limpieza y depuración
│   ├── transformacion.py   # Módulo de transformación a formato largo
│   ├── analisis.py         # Análisis inicial del dataset
│   ├── reporte.py          # Reportes y gráficos base
│   ├── estadistica.py      # Cálculo de estadísticas descriptivas
│   ├── indicadores.py      # Cálculo de indicadores clave
│   └── visualizaciones.py  # Generación de gráficos obligatorios
│
├── main.py                 # Script orquestador del pipeline completo
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación del proyecto