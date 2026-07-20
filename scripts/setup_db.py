"""
Script para configurar la Base de Datos
Crea las tablas necesarias
"""

import sys
from pathlib import Path

# Agregar raíz del proyecto al path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from config.db_config import engine, crear_todas_las_tablas, verificar_conexion_bd
from config.logger_config import logger
from sqlalchemy import text

def crear_tablas():
    """Crea todas las tablas en la base de datos"""
    try:
        logger.info("🔨 Creando estructura de base de datos...")
        
        # Verificar conexión
        if not verificar_conexion_bd():
            logger.error("❌ No se pudo conectar a la base de datos")
            return False
        
        # Crear tablas básicas (sin ORM para ahora)
        with engine.connect() as conn:
            # Tabla de trades
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS trades (
                    id SERIAL PRIMARY KEY,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    simbolo VARCHAR(20),
                    tipo VARCHAR(10),
                    cantidad DECIMAL(20,8),
                    precio DECIMAL(20,8),
                    total DECIMAL(20,8),
                    estado VARCHAR(20),
                    comisión DECIMAL(20,8)
                )
            """))
            
            # Tabla de señales
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS signals (
                    id SERIAL PRIMARY KEY,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    simbolo VARCHAR(20),
                    score INTEGER,
                    recomendacion VARCHAR(50),
                    precio_actual DECIMAL(20,8),
                    indicadores JSONB
                )
            """))
            
            # Tabla de alertas
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS alerts (
                    id SERIAL PRIMARY KEY,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    tipo VARCHAR(50),
                    mensaje TEXT,
                    enviado BOOLEAN DEFAULT FALSE
                )
            """))
            
            conn.commit()
            logger.info("✓ Tablas creadas correctamente")
            return True
        
    except Exception as e:
        logger.error(f"❌ Error creando tablas: {str(e)}")
        return False

def main():
    """Función principal"""
    print("\n" + "="*60)
    print("INICIALIZADOR DE BASE DE DATOS")
    print("Sistema de Trading XRP/USDT")
    print("="*60 + "\n")
    
    if crear_tablas():
        print("\n✓ Base de datos configurada correctamente\n")
        return 0
    else:
        print("\n❌ Error configurando base de datos\n")
        return 1

if __name__ == "__main__":
    sys.exit(main())
