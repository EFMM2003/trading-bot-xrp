"""
Encriptación y Seguridad
Manejo de credenciales y datos sensibles
"""

from cryptography.fernet import Fernet
from config.settings import Settings
from config.logger_config import logger
import os
import base64

class EncriptadorAES:
    """Encriptador AES-256 para datos sensibles"""
    
    def __init__(self):
        """Inicializa el encriptador"""
        self.settings = Settings()
        self._inicializar_clave()
    
    def _inicializar_clave(self):
        """Inicializa o carga la clave de encriptación"""
        try:
            if self.settings.ENCRYPTION_KEY:
                self.cipher = Fernet(self.settings.ENCRYPTION_KEY)
                logger.debug("✓ Clave de encriptación cargada")
            else:
                logger.warning("⚠️  Generando nueva clave de encriptación")
                clave = Fernet.generate_key()
                self.cipher = Fernet(clave)
                logger.info(f"Guardar esta clave en ENCRYPTION_KEY: {clave.decode()}")
        except Exception as e:
            logger.error(f"❌ Error inicializando encriptación: {str(e)}")
    
    def encriptar(self, datos: str) -> str:
        """
        Encripta un string
        
        Args:
            datos: String a encriptar
            
        Returns:
            String encriptado en base64
        """
        try:
            datos_bytes = datos.encode()
            encriptado = self.cipher.encrypt(datos_bytes)
            return base64.b64encode(encriptado).decode()
        except Exception as e:
            logger.error(f"❌ Error encriptando datos: {str(e)}")
            return None
    
    def desencriptar(self, datos_encriptados: str) -> str:
        """
        Desencripta un string
        
        Args:
            datos_encriptados: String encriptado
            
        Returns:
            String desencriptado
        """
        try:
            datos_bytes = base64.b64decode(datos_encriptados.encode())
            desencriptado = self.cipher.decrypt(datos_bytes)
            return desencriptado.decode()
        except Exception as e:
            logger.error(f"❌ Error desencriptando datos: {str(e)}")
            return None

class APIKeyManager:
    """Gestor seguro de credenciales API"""
    
    def __init__(self):
        """Inicializa el gestor de credenciales"""
        self.encriptador = EncriptadorAES()
        self.settings = Settings()
    
    def verificar_credenciales(self) -> bool:
        """
        Verifica que las credenciales estén configuradas
        
        Returns:
            True si las credenciales son válidas
        """
        try:
            if not self.settings.BINANCE_API_KEY:
                logger.error("❌ BINANCE_API_KEY no configurada")
                return False
            
            if not self.settings.BINANCE_API_SECRET:
                logger.error("❌ BINANCE_API_SECRET no configurada")
                return False
            
            logger.info("✓ Credenciales verificadas")
            return True
            
        except Exception as e:
            logger.error(f"❌ Error verificando credenciales: {str(e)}")
            return False
    
    def obtener_api_key_encriptada(self) -> str:
        """
        Obtiene la API Key encriptada
        
        Returns:
            API Key encriptada
        """
        return self.encriptador.encriptar(self.settings.BINANCE_API_KEY)
    
    def obtener_api_secret_encriptado(self) -> str:
        """
        Obtiene la API Secret encriptada
        
        Returns:
            API Secret encriptada
        """
        return self.encriptador.encriptar(self.settings.BINANCE_API_SECRET)

# Crear instancia global
encriptador_global = EncriptadorAES()
