# 5) Reporte semanal automatizado

- Objetivo: generar y automatizar un reporte semanal en PDF con KPIs y gráfico.
- Entrada: `data/cafe_sales_clean.csv`
- Salidas: `reports/weekly_report_YYYYMMDD.pdf`, `reports/chart.png`
- Logs: `logs/automation.log`

Componentes
- Generación de reporte: `scripts/report_generator.py`
- Automatización (scheduler): `scripts/automation.py`

Cómo ejecutar
- Reporte inmediato: `python scripts/report_generator.py`
- Automatización (cada lunes 09:00): `python scripts/automation.py`
  - Usa rutas robustas relativas al proyecto y escribe logs en `logs/automation.log`.

Requisitos
- pandas, matplotlib, fpdf, schedule (ver `requirements.txt`).

Evidencias
- PDF generado y gráfico en `reports/`.
- Logs de ejecución en `logs/`.

