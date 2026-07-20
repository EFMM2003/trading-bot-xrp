"""
Sistema de Notificaciones por Telegram
Usa Telegram Bot API
"""

from telegram import Bot
from config.settings import Settings
from config.logger_config import logger, audit_logger
from datetime import datetime
import asyncio

class TelegramNotificador:
    """Notificador por Telegram Bot"""
    
    def __init__(self):
        """Inicializa el notificador"""
        self.settings = Settings()
        self.bot = None
        self._inicializar()
    
    def _inicializar(self):
        """Inicializa el bot de Telegram"""
        try:
            if not self.settings.TELEGRAM_BOT_TOKEN or not self.settings.TELEGRAM_CHAT_ID:
                logger.warning("⚠️  Credenciales Telegram no configuradas")
                return False
            
            self.bot = Bot(token=self.settings.TELEGRAM_BOT_TOKEN)
            logger.info("✓ Bot Telegram inicializado")
            return True
        except Exception as e:
            logger.error(f"❌ Error inicializando Telegram: {str(e)}")
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
            if not self.bot or not self.settings.TELEGRAM_ALERTS_ENABLED:
                return False
            
            mensaje = f"""
{signal_info['emoji']} <b>{signal_info['recomendacion']}</b>

📊 <b>Análisis XRP/USDT</b>
Precio: <code>${signal_info['precio']:.4f}</code>
Score: <code>{signal_info['score']}/100</code>
Timestamp: <code>{signal_info['timestamp']}</code>

🔍 Señales:
{''.join([f'{s}\n' for s in signal_info['señales']])}
            """
            
            # Ejecutar de forma asíncrona
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(
                self.bot.send_message(
                    chat_id=self.settings.TELEGRAM_CHAT_ID,
                    text=mensaje,
                    parse_mode='HTML'
                )
            )
            loop.close()
            
            logger.info(f"✓ Mensaje Telegram enviado: {signal_info['recomendacion']}")
            audit_logger.info(f"TELEGRAM_SENT | Tipo: signal_alert | Chat: {self.settings.TELEGRAM_CHAT_ID}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Error enviando Telegram: {str(e)}")
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
            if not self.bot:
                return False
            
            mensaje = f"❌ <b>Error en Sistema</b>\n\n{error_msg}\n\nTimestamp: {datetime.now()}"
            
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(
                self.bot.send_message(
                    chat_id=self.settings.TELEGRAM_CHAT_ID,
                    text=mensaje,
                    parse_mode='HTML'
                )
            )
            loop.close()
            
            logger.info("✓ Alerta de error enviada por Telegram")
            return True
            
        except Exception as e:
            logger.error(f"❌ Error enviando Telegram: {str(e)}")
            return False

# Instancia global
telegram_notificador = TelegramNotificador()
