"""
Sistema de Notificaciones por Email
Usa SendGrid para enviar alertas
"""

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from config.settings import Settings
from config.logger_config import logger, audit_logger
from datetime import datetime

class EmailNotificador:
    """Notificador por Email usando SendGrid"""
    
    def __init__(self):
        """Inicializa el notificador"""
        self.settings = Settings()
        self.cliente = None
        self._inicializar()
    
    def _inicializar(self):
        """Inicializa el cliente SendGrid"""
        try:
            if not self.settings.SENDGRID_API_KEY:
                logger.warning("⚠️  API Key SendGrid no configurada")
                return False
            
            self.cliente = SendGridAPIClient(self.settings.SENDGRID_API_KEY)
            logger.info("✓ Cliente SendGrid inicializado")
            return True
        except Exception as e:
            logger.error(f"❌ Error inicializando SendGrid: {str(e)}")
            return False
    
    def enviar_alerta_signal(self, signal_info: dict) -> bool:
        """
        Envía alerta de nueva señal
        
        Args:
            signal_info: Info de la señal
            
        Returns:
            True si se envió correctamente
        """
        try:
            if not self.cliente or not self.settings.EMAIL_ALERTS_ENABLED:
                return False
            
            asunto = f"🎯 Nueva Señal: {signal_info['recomendacion']}"
            
            contenido = f"""
            <h2>Nueva Señal de Trading Detectada</h2>
            <p><strong>Recomendación:</strong> {signal_info['recomendacion']}</p>
            <p><strong>Precio Actual:</strong> ${signal_info['precio']:.4f}</p>
            <p><strong>Score:</strong> {signal_info['score']}/100</p>
            <p><strong>Timestamp:</strong> {signal_info['timestamp']}</p>
            <hr>
            <h3>Señales Detalladas:</h3>
            <ul>
            {''.join([f'<li>{s}</li>' for s in signal_info['señales']])}
            </ul>
            """
            
            correo = Mail(
                from_email=self.settings.SENDGRID_FROM_EMAIL,
                to_emails=self.settings.SENDGRID_TO_EMAIL,
                subject=asunto,
                html_content=contenido
            )
            
            self.cliente.send(correo)
            logger.info(f"✓ Email de alerta enviado: {asunto}")
            audit_logger.info(f"EMAIL_SENT | Tipo: signal_alert | Destino: {self.settings.SENDGRID_TO_EMAIL}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Error enviando email: {str(e)}")
            return False
    
    def enviar_alerta_error(self, error_msg: str) -> bool:
        """
        Envía alerta de error
        
        Args:
            error_msg: Mensaje de error
            
        Returns:
            True si se envió correctamente
        """
        try:
            if not self.cliente or not self.settings.EMAIL_ALERTS_ENABLED:
                return False
            
            correo = Mail(
                from_email=self.settings.SENDGRID_FROM_EMAIL,
                to_emails=self.settings.SENDGRID_TO_EMAIL,
                subject="❌ Error en Sistema de Trading",
                html_content=f"<h2>Error Detectado</h2><p>{error_msg}</p><p>Timestamp: {datetime.now()}</p>"
            )
            
            self.cliente.send(correo)
            logger.info("✓ Email de error enviado")
            return True
            
        except Exception as e:
            logger.error(f"❌ Error enviando email: {str(e)}")
            return False

# Instancia global
email_notificador = EmailNotificador()
