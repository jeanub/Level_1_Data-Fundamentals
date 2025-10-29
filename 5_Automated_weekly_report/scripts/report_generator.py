# scripts/report_generator.py
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime
import os

# Directorio base del proyecto (carpeta padre de scripts)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def generate_report(input_path, output_path):
    # Cargar datos
    df = pd.read_csv(input_path)

    # Calcular KPIs
    total_revenue = df['total_spent'].sum()
    total_transactions = df['transaction_id'].nunique()
    avg_ticket = total_revenue / total_transactions

    # Crear gráfico de ventas por ubicación
    plt.figure()
    df.groupby('location')['total_spent'].sum().plot(kind='bar', title='Ventas por Ubicación')
    plt.tight_layout()

    # Asegurar carpeta de reportes
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    chart_path = os.path.join(os.path.dirname(output_path), 'chart.png')
    plt.savefig(chart_path)

    # Crear PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt="Reporte Semanal de Ventas de Café", ln=True, align='C')

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Fecha: {datetime.now():%Y-%m-%d}", ln=True)
    pdf.cell(200, 10, txt=f"Total Revenue: ${total_revenue:,.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Total Transactions: {total_transactions}", ln=True)
    pdf.cell(200, 10, txt=f"Average Ticket: ${avg_ticket:,.2f}", ln=True)

    # Insertar gráfico
    pdf.image(chart_path, x=10, y=70, w=180)

    # Exportar PDF
    pdf.output(output_path)

# Ejecución directa
if __name__ == "__main__":
    input_path = os.path.join(BASE_DIR, 'data', 'cafe_sales_clean.csv')
    output_path = os.path.join(BASE_DIR, 'reports', f"weekly_report_{datetime.now():%Y%m%d}.pdf")
    generate_report(input_path=input_path, output_path=output_path)
