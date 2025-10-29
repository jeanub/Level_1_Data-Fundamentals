# Importación de librerías necesarias
import pandas as pd, logging, os
from tqdm import tqdm  # (opcional, útil para agregar barras de progreso si se desea)

# 📁 Definición del directorio base del proyecto (un nivel arriba del script actual)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# 📂 Configuración del directorio y archivo de logs
log_dir = os.path.join(BASE_DIR, 'logs')  # Ruta a la carpeta de logs
os.makedirs(log_dir, exist_ok=True)       # Crea la carpeta si no existe
log_path = os.path.join(log_dir, 'cleaner.log')  # Ruta completa al archivo de log

# 📝 Inicialización del sistema de logging
logging.basicConfig(
    filename=log_path,  # Archivo donde se guardarán los logs
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato del mensaje
    level=logging.INFO  # Nivel de detalle (INFO = eventos generales)
)

# 📥 Función para cargar el dataset desde un archivo CSV
def load_data(path):
    df = pd.read_csv(path)  # Carga el archivo CSV en un DataFrame
    logging.info(f"Cargado: {df.shape}")  # Registra la forma del DataFrame (filas, columnas)
    return df

# 🧼 Función para estandarizar nombres de columnas
def standardize_columns(df):
    df.columns = (
        df.columns
        .str.strip()        # Elimina espacios al inicio y final
        .str.lower()        # Convierte a minúsculas
        .str.replace(' ', '_', regex=False)  # Reemplaza espacios por guiones bajos
    )
    return df

# 🧪 Función para limpiar y convertir tipos de datos
def clean_types(df):
    # Convierte fechas y valores numéricos, eliminando errores
    df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    df['price_per_unit'] = pd.to_numeric(df['price_per_unit'], errors='coerce')
    df['total_spent'] = pd.to_numeric(df['total_spent'], errors='coerce')

    # Elimina filas con valores nulos en columnas clave
    df = df.dropna(subset=['transaction_date', 'quantity', 'price_per_unit', 'total_spent'])
    return df

# ✅ Función para validar reglas de negocio
def validate(df):
    # Verifica que no haya valores negativos en columnas críticas
    assert df['quantity'].ge(0).all(), "Cantidad negativa detectada"
    assert df['price_per_unit'].ge(0).all(), "Precio negativo detectado"
    assert df['total_spent'].ge(0).all(), "Total negativo detectado"
    return df

# 📤 Función para exportar el DataFrame limpio a un nuevo archivo CSV
def export(df, path):
    df.to_csv(path, index=False)  # Guarda el archivo sin índice
    logging.info("Exportado con éxito")  # Registra el éxito de la operación

# 🚀 Punto de entrada principal del script
if __name__ == "__main__":
    # Define rutas de entrada y salida basadas en la estructura del proyecto
    data_path = os.path.join(BASE_DIR, 'data', 'dirty_cafe_sales.csv')
    output_path = os.path.join(BASE_DIR, 'output', 'cafe_sales_clean.csv')

    # Ejecuta el pipeline completo de limpieza
    raw = load_data(data_path)
    df = standardize_columns(raw)
    df = clean_types(df)
    df = validate(df)
    export(df, output_path)
