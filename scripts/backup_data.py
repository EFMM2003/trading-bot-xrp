"""
Script para generar respaldo de datos
Backup automático de base de datos
"""

import sys
from pathlib import Path
import subprocess
from datetime import datetime
import gzip
import shutil

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from config.settings import Settings
from config.logger_config import logger

def crear_backup():
    """
    Crea un backup de la base de datos
    """
    try:
        settings = Settings()
        logger.info("💾 Iniciando backup de base de datos...")
        
        # Crear directorio de backups
        backup_dir = PROJECT_ROOT / "data_storage" / "backups"
        backup_dir.mkdir(parents=True, exist_ok=True)
        
        # Nombre del archivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = backup_dir / f"backup_{timestamp}.sql"
        
        # Ejecutar pg_dump
        logger.info(f"📮 Dumpeando base de datos a {backup_file}...")
        
        cmd = [
            "pg_dump",
            "-h", settings.DB_HOST,
            "-U", settings.DB_USER,
            "-d", settings.DB_NAME,
            "-f", str(backup_file)
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            logger.error(f"❌ Error en pg_dump: {result.stderr}")
            return False
        
        # Comprimir
        logger.info("🗄 Comprimiendo backup...")
        backup_compressed = f"{backup_file}.gz"
        with open(backup_file, 'rb') as f_in:
            with gzip.open(backup_compressed, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        # Eliminar archivo sin comprimir
        backup_file.unlink()
        
        logger.info(f"✓ Backup creado: {backup_compressed}")
        return True
        
    except Exception as e:
        logger.error(f"❌ Error en backup: {str(e)}")
        return False

def limpiar_backups_antiguos(dias_retencion: int = 30):
    """
    Limpia backups más antiguos que el período de retención
    
    Args:
        dias_retencion: Días para conservar backups
    """
    try:
        from datetime import timedelta
        import time
        
        settings = Settings()
        backup_dir = PROJECT_ROOT / "data_storage" / "backups"
        
        if not backup_dir.exists():
            return
        
        ahora = datetime.now()
        limite = ahora - timedelta(days=dias_retencion)
        
        archivos_eliminados = 0
        for archivo in backup_dir.glob("backup_*.sql.gz"):
            timestamp_archivo = datetime.fromtimestamp(archivo.stat().st_mtime)
            if timestamp_archivo < limite:
                archivo.unlink()
                logger.info(f"🗑️  Backup antiguo eliminado: {archivo.name}")
                archivos_eliminados += 1
        
        if archivos_eliminados > 0:
            logger.info(f"✓ {archivos_eliminados} backups antiguos eliminados")
        
    except Exception as e:
        logger.error(f"❌ Error limpiando backups: {str(e)}")

def main():
    """
    Función principal
    """
    print("\n" + "="*60)
    print("💾 GENERADOR DE BACKUPS")
    print("Sistema de Trading XRP/USDT")
    print("="*60 + "\n")
    
    if crear_backup():
        print("\n✓ Backup creado correctamente")
        
        # Limpiar backups antiguos
        settings = Settings()
        limpiar_backups_antiguos(
            settings.BACKUP_RETENTION_DAYS if hasattr(settings, 'BACKUP_RETENTION_DAYS') else 30
        )
        
        print("\n")
        return 0
    else:
        print("\n❌ Error creando backup\n")
        return 1

if __name__ == "__main__":
    sys.exit(main())
