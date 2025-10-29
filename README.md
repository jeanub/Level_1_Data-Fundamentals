# Nivel 1 - Fundamentos del Dato: "Del Caos al Orden"
**Ruta de Aprendizaje en Business Intelligence y Extracción de Datos - DataNova Corp**

---

## Contexto Narrativo
DataNova Corp acaba de nacer. Los datos llegan desordenados, incompletos y sin control.
Este nivel representa el proceso de dar vida, orden y significado a los datos.
Cada proyecto simboliza una fase de madurez técnica y mental: pasar de limpiar a comprender, y de comprender a automatizar.

> "El analista no domina los datos. Los escucha hasta que revelan su lógica."

---

## Objetivo General del Nivel
Construir el pipeline base de Business Intelligence:
Extracción → Limpieza → Exploración → Visualización → Automatización
para sentar las bases de la futura arquitectura analítica de la empresa.

---

## Competencias Desarrolladas
- Extracción de datos desde archivos y web.
- Limpieza y normalización con Pandas.
- Análisis exploratorio (EDA) y correlaciones.
- Creación de dashboards en Power BI.
- Automatización de reportes (Python / Power Automate).
- Control de versiones con Git.
- Documentación reflexiva y storytelling analítico.

---

## Proyectos Realizados

### 1) El nacimiento del dato
Objetivo: transformar un dataset caótico en información limpia y confiable.
Logros:
- Dataset sin nulos ni duplicados.
- Estandarización de columnas y tipos.
- Validaciones automáticas de calidad.
Competencias: limpieza, estructuración, validación.
Símbolo: Nacimiento - el dato cobra vida.

---

### 2) Tu primer tablero de ventas
Objetivo: construir un dashboard interactivo con KPIs básicos.
Logros:
- KPIs de ingresos, pedidos, ticket promedio.
- Filtros por año, región y producto.
- Visual storytelling para dirección.
Competencias: visualización, diseño, storytelling.
Símbolo: Claridad - el caos se vuelve comprensible.

---

### 3) Anatomía de un dataset
Objetivo: analizar relaciones entre variables y entender patrones ocultos.
Logros:
- Correlaciones visuales (heatmaps, scatterplots).
- Identificación de outliers y variables críticas.
- Síntesis de insights con impacto.
Competencias: análisis exploratorio, pensamiento crítico, interpretación.
Símbolo: Descubrimiento - entender lo que los datos intentan decir.

---

### 4) Limpieza inteligente
Objetivo: crear un script modular que limpie y valide automáticamente datasets.
Logros:
- ETL automatizado con logs y validaciones.
- Modularidad para reutilizar funciones.
- Auditoría de calidad mediante registro de eventos.
Competencias: automatización de limpieza, programación estructurada, auditoría.
Símbolo: Sistema - el orden se vuelve ley.

---

### 5) Reporte semanal automatizado
Objetivo: automatizar la generación y distribución de reportes.
Logros:
- Generación automática de reportes en PDF.
- Integración con Scheduler o Power Automate.
- Flujo reproducible con logs y control de ejecución.
Competencias: automatización, reporting, integración.
Símbolo: Autonomía - los datos trabajan por sí mismos.

---

## Resultados Globales del Nivel
| Área | Habilidad Alcanzada | Evidencia |
|------|---------------------|-----------|
| Limpieza | 100% automatizable | `4_Smart_cleaning/scripts/cleaner.py`, `4_Smart_cleaning/output/cafe_sales_clean.csv` |
| Visualización | Dashboard funcional | `2_Display_of_data/datanova.pbix` |
| Análisis | Correlaciones y outliers | `3_anatomy_of_a_data_set/notebooks/eda_analysis.ipynb` |
| Automatización | Flujo semanal operativo | `5_Automated_weekly_report/scripts/automation.py`, `5_Automated_weekly_report/reports/weekly_report_YYYYMMDD.pdf` |
| Documentación | README principal del nivel | `README.md` |

---

## Estructura General del Nivel
```
1_the_birth_of_data/
  data/ sales_data_sample.csv
  notebooks/ analisis.ipynb, data_cleaning.ipynb
  output/ sales_data_clean.csv

2_Display_of_data/
  data/ sales_data_clean.csv
  datanova.pbix
  img/ dashboard_preview.png

3_anatomy_of_a_data_set/
  data/ sales_data_clean.csv
  notebooks/ eda_analysis.ipynb
  output/ correlation_heatmap.png, Scatterplot.png, Sales_by_Country.png

4_Smart_cleaning/
  data/ dirty_cafe_sales.csv
  scripts/ cleaner.py
  output/ cafe_sales_clean.csv
  logs/ cleaner.log

5_Automated_weekly_report/
  data/ cafe_sales_clean.csv
  scripts/ report_generator.py, automation.py
  reports/ weekly_report_YYYYMMDD.pdf, chart.png
  logs/ automation.log
```

Notas:
- Los nombres de archivos indicados arriba reflejan la implementación actual del repositorio.
- Si se desea cambiar nombres de salida o rutas, actualizar primero los scripts correspondientes y luego este README.

