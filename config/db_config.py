"""
Configuración de Base de Datos
Configuraciones específicas para PostgreSQL
"""

from config.settings import Settings
from sqlalchemy import create_engine, event
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker, Session
from config.logger_config import logger

settings = Settings()

# Crear engine de SQLAlchemy
engine = create_engine(
    settings.DATABASE_URL,
    poolclass=QueuePool,
    pool_size=20,
    max_overflow=40,
    pool_recycle=3600,  # Reciclar conexiones cada hora
    pool_pre_ping=True,  # Verificar conexiones antes de usar
    echo=settings.DEBUG_MODE,  # Mostrar SQL en debug
    connect_args={
        'connect_timeout': settings.DB_TIMEOUT if hasattr(settings, 'DB_TIMEOUT') else 10,
        'application_name': 'xrp_trading_system'
    }
)

# Event listener para loguear errores de conexión
@event.listens_for(engine, 'connect')
def receive_connect(dbapi_conn, connection_record):
    """Se ejecuta cuando se abre una conexión"""
    logger.debug(f"📡 Conexión a BD abierta: {settings.DB_NAME}")

@event.listens_for(engine, 'close')
def receive_close(dbapi_conn, connection_record):
    """Se ejecuta cuando se cierra una conexión"""
    logger.debug("📡 Conexión a BD cerrada")

@event.listens_for(engine, 'detach')
def receive_detach(dbapi_conn, connection_record):
    """Se ejecuta cuando se desconecta"""
    logger.debug("📡 Conexión a BD desconectada")

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db() -> Session:
    """Dependency para obtener sesión de BD"""
    db = SessionLocal()
    try:
        return db
    except Exception as e:
        logger.error(f"❌ Error al obtener sesión de BD: {str(e)}")
        db.close()
        raise

def verificar_conexion_bd() -> bool:
    """Verifica que la conexión a BD esté activa"""
    try:
        with engine.connect() as connection:
            result = connection.execute("SELECT 1")
            logger.info("✓ Conexión a BD verificada correctamente")
            return True
    except Exception as e:
        logger.error(f"❌ No se pudo conectar a la BD: {str(e)}")
        return False

def crear_todas_las_tablas():
    """Crea todas las tablas en la BD"""
    try:
        from models.database_models import Base
        Base.metadata.create_all(bind=engine)
        logger.info("✓ Todas las tablas creadas correctamente")
    except Exception as e:
        logger.error(f"❌ Error al crear tablas: {str(e)}")
        raise

class DatabaseConfig:
    """Configuración de BD centralizada"""
    
    # Configuración de tablas
    TABLAS = {
        'usuarios': 'Tabla de usuarios',
        'trades': 'Tabla de trades ejecutados',
        'signals': 'Tabla de señales generadas',
        'analisis': 'Tabla de análisis técnicos',
        'predicciones': 'Tabla de predicciones IA',
        'alertas': 'Tabla de alertas enviadas',
        'auditoría': 'Tabla de auditoría',
        'configuración': 'Tabla de configuración del sistema'
    }
    
    # Índices recomendados
    INDICES = {
        'trades': ['usuario_id', 'timestamp', 'simbolo'],
        'signals': ['timestamp', 'simbolo', 'score'],
        'analisis': ['timestamp', 'simbolo'],
        'alertas': ['usuario_id', 'timestamp', 'tipo'],
        'auditoría': ['usuario_id', 'timestamp', 'accion']
    }
    
    # Retención de datos (días)
    RETENCION_DATOS = {
        'trades': 730,  # 2 años
        'signals': 365,  # 1 año
        'analisis': 365,  # 1 año
        'alertas': 90,   # 3 meses
        'auditoría': 180  # 6 meses
    }
