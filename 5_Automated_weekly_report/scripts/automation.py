# scripts/automation.py
import schedule, time, os, logging
from datetime import datetime
from report_generator import generate_report

# Directorios base y rutas robustas (relativas al proyecto)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'cafe_sales_clean.csv')
REPORTS_DIR = os.path.join(BASE_DIR, 'reports')
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
os.makedirs(REPORTS_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)

# Configuración de logging
LOG_PATH = os.path.join(LOGS_DIR, 'automation.log')
logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def job():
    """Tarea programada para generar el reporte semanal."""
    output_path = os.path.join(REPORTS_DIR, f'weekly_report_{datetime.now():%Y%m%d}.pdf')
    try:
        logging.info('Inicio de generación de reporte semanal')
        generate_report(DATA_PATH, output_path)
        logging.info('Reporte generado correctamente: %s', output_path)
    except Exception as e:
        logging.exception('Fallo al generar el reporte: %s', e)


# Programación: cada lunes a las 09:00
schedule.every().monday.at("09:00").do(job)
logging.info('Scheduler iniciado. Esperando próxima ejecución...')

while True:
    schedule.run_pending()
    time.sleep(60)
