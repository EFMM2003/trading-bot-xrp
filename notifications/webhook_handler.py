"""
Manejador de Webhooks
Envía datos a endpoints externos
"""

import requests
import json
from config.settings import Settings
from config.logger_config import logger, audit_logger
from datetime import datetime
from typing import Dict, List

class WebhookHandler:
    """Manejador de Webhooks"""
    
    def __init__(self):
        """Inicializa el manejador"""
        self.settings = Settings()
    
    def enviar_signal(self, signal_info: dict) -> bool:
        """
        Envía una señal a todos los webhooks configurados
        
        Args:
            signal_info: Info de la señal
            
        Returns:
            True si se envió a al menos uno
        """
        try:
            if not self.settings.WEBHOOK_ALERTS_ENABLED or not self.settings.WEBHOOK_URLS:
                return False
            
            payload = {
                'evento': 'signal_change',
                'timestamp': datetime.now().isoformat(),
                'datos': signal_info,
                'secret': self.settings.WEBHOOK_SECRET
            }
            
            headers = {'Content-Type': 'application/json'}
            
            enviados = 0
            for url in self.settings.WEBHOOK_URLS:
                if not url.strip():
                    continue
                
                try:
                    respuesta = requests.post(
                        url.strip(),
                        json=payload,
                        headers=headers,
                        timeout=self.settings.WEBHOOK_TIMEOUT,
                        retries=self.settings.WEBHOOK_RETRIES
                    )
                    
                    if respuesta.status_code == 200:
                        logger.debug(f"✓ Webhook enviado a {url}")
                        enviados += 1
                        audit_logger.info(f"WEBHOOK_SENT | URL: {url} | Status: 200")
                    else:
                        logger.warning(f"⚠️  Webhook retornó {respuesta.status_code}: {url}")
                
                except requests.exceptions.Timeout:
                    logger.warning(f"⚠️  Timeout enviando webhook a {url}")
                except Exception as e:
                    logger.error(f"❌ Error enviando webhook a {url}: {str(e)}")
            
            return enviados > 0
            
        except Exception as e:
            logger.error(f"❌ Error en webhook handler: {str(e)}")
            return False
    
    def enviar_error(self, error_msg: str) -> bool:
        """
        Envía notificación de error
        
        Args:
            error_msg: Mensaje de error
            
        Returns:
            True si se envió
        """
        try:
            if not self.settings.WEBHOOK_ALERTS_ENABLED or not self.settings.WEBHOOK_URLS:
                return False
            
            payload = {
                'evento': 'error_occurred',
                'timestamp': datetime.now().isoformat(),
                'error': error_msg,
                'secret': self.settings.WEBHOOK_SECRET
            }
            
            headers = {'Content-Type': 'application/json'}
            
            for url in self.settings.WEBHOOK_URLS:
                if not url.strip():
                    continue
                
                try:
                    requests.post(
                        url.strip(),
                        json=payload,
                        headers=headers,
                        timeout=self.settings.WEBHOOK_TIMEOUT
                    )
                except Exception as e:
                    logger.error(f"❌ Error en webhook: {str(e)}")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Error enviando error por webhook: {str(e)}")
            return False

# Instancia global
webhook_handler = WebhookHandler()
