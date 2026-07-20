"""
Monitoreo del Sistema
Supervisión de salud y rendimiento
"""

import psutil
import threading
from datetime import datetime
from config.logger_config import logger
from config.settings import Settings
import time

class SystemMonitor:
    """Monitor de salud del sistema"""
    
    def __init__(self):
        """Inicializa el monitor"""
        self.settings = Settings()
        self.activo = False
        self.hilo_monitoreo = None
    
    def iniciar(self):
        """
        Inicia el monitoreo del sistema
        """
        if not self.settings.SYSTEM_CHECK_ENABLED:
            logger.info("ℹ️  Monitoreo del sistema deshabilitado")
            return
        
        self.activo = True
        self.hilo_monitoreo = threading.Thread(target=self._monitorear, daemon=True)
        self.hilo_monitoreo.start()
        logger.info("✓ Monitoreo del sistema iniciado")
    
    def detener(self):
        """
        Detiene el monitoreo del sistema
        """
        self.activo = False
        if self.hilo_monitoreo:
            self.hilo_monitoreo.join(timeout=5)
        logger.info("✓ Monitoreo del sistema detenido")
    
    def _monitorear(self):
        """
        Función de monitoreo continuo
        """
        while self.activo:
            try:
                stats = self._obtener_estadisticas()
                self._verificar_alertas(stats)
                time.sleep(self.settings.HEALTH_CHECK_INTERVAL)
            except Exception as e:
                logger.error(f"❌ Error en monitoreo: {str(e)}")
    
    def _obtener_estadisticas(self) -> dict:
        """
        Obtiene estadísticas del sistema
        
        Returns:
            Dict con estadísticas
        """
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memoria = psutil.virtual_memory()
            disco = psutil.disk_usage('/')
            
            return {
                'timestamp': datetime.now(),
                'cpu_percent': cpu_percent,
                'memoria_percent': memoria.percent,
                'memoria_disponible_mb': memoria.available / (1024**2),
                'disco_percent': disco.percent,
                'procesos_activos': len(psutil.pids())
            }
        except Exception as e:
            logger.error(f"❌ Error obteniendo estadísticas: {str(e)}")
            return None
    
    def _verificar_alertas(self, stats: dict):
        """
        Verifica si hay alertas críticas
        
        Args:
            stats: Estadísticas del sistema
        """
        if stats is None:
            return
        
        if stats['cpu_percent'] > 80:
            logger.warning(f"⚠️  CPU alta: {stats['cpu_percent']}%")
        
        if stats['memoria_percent'] > 85:
            logger.warning(f"⚠️  Memoria alta: {stats['memoria_percent']}%")
        
        if stats['disco_percent'] > 90:
            logger.warning(f"⚠️  Disco casi lleno: {stats['disco_percent']}%")
    
    @staticmethod
    def obtener_estado() -> dict:
        """
        Obtiene el estado actual del sistema
        
        Returns:
            Estado actual
        """
        try:
            return {
                'timestamp': datetime.now().isoformat(),
                'cpu': f"{psutil.cpu_percent()}%",
                'memoria': f"{psutil.virtual_memory().percent}%",
                'disco': f"{psutil.disk_usage('/').percent}%",
                'estado': '✓ Normal'
            }
        except Exception as e:
            logger.error(f"❌ Error obteniendo estado: {str(e)}")
            return None

# Crear instancia global
system_monitor = SystemMonitor()
