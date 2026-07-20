"""
Configuración de APIs Externas
Configuración de Binance, SendGrid, Telegram, etc.
"""

from config.settings import Settings
from config.logger_config import logger

settings = Settings()

class BinanceConfig:
    """Configuración de Binance API"""
    API_KEY = settings.BINANCE_API_KEY
    API_SECRET = settings.BINANCE_API_SECRET
    BASE_URL = settings.BINANCE_TESTNET_URL if settings.USE_TESTNET else settings.BINANCE_BASE_URL
    TIMEOUT = settings.BINANCE_TIMEOUT
    
    ENDPOINTS = {
        'klines': '/api/v3/klines',
        'ticker': '/api/v3/ticker/24hr',
        'account': '/api/v3/account',
        'create_order': '/api/v3/order',
        'cancel_order': '/api/v3/order',
        'open_orders': '/api/v3/openOrders'
    }
    
    @staticmethod
    def validar():
        """Valida que la configuración sea correcta"""
        if not BinanceConfig.API_KEY or not BinanceConfig.API_SECRET:
            logger.error("❌ API Key o Secret de Binance no configuradas")
            return False
        logger.info("✓ Configuración de Binance validada")
        return True

class SendGridConfig:
    """Configuración de SendGrid para emails"""
    API_KEY = settings.SENDGRID_API_KEY
    FROM_EMAIL = settings.SENDGRID_FROM_EMAIL
    TO_EMAIL = settings.SENDGRID_TO_EMAIL
    ENABLED = settings.EMAIL_ALERTS_ENABLED
    
    TEMPLATES = {
        'signal_alert': 'Nueva señal de trading detectada',
        'price_alert': 'Alerta de precio',
        'error_alert': 'Error en el sistema',
        'daily_summary': 'Resumen diario de trading'
    }
    
    @staticmethod
    def validar():
        """Valida que la configuración sea correcta"""
        if not SendGridConfig.API_KEY and SendGridConfig.ENABLED:
            logger.warning("⚠️  API Key de SendGrid no configurada")
            return False
        logger.info("✓ Configuración de SendGrid validada")
        return True

class TelegramConfig:
    """Configuración de Telegram Bot"""
    BOT_TOKEN = settings.TELEGRAM_BOT_TOKEN
    CHAT_ID = settings.TELEGRAM_CHAT_ID
    ENABLED = settings.TELEGRAM_ALERTS_ENABLED
    
    COMANDOS = {
        '/start': 'Iniciar bot',
        '/estado': 'Ver estado del mercado',
        '/analisis': 'Obtener análisis actual',
        '/alertas': 'Configurar alertas',
        '/help': 'Obtener ayuda'
    }
    
    @staticmethod
    def validar():
        """Valida que la configuración sea correcta"""
        if not TelegramConfig.BOT_TOKEN and TelegramConfig.ENABLED:
            logger.warning("⚠️  Token de Telegram no configurado")
            return False
        logger.info("✓ Configuración de Telegram validada")
        return True

class WebhookConfig:
    """Configuración de Webhooks"""
    SECRET = settings.WEBHOOK_SECRET
    URLS = settings.WEBHOOK_URLS
    ENABLED = settings.WEBHOOK_ALERTS_ENABLED
    TIMEOUT = settings.WEBHOOK_TIMEOUT
    RETRIES = settings.WEBHOOK_RETRIES
    
    EVENTOS = {
        'signal_change': 'Cambio de señal de trading',
        'order_executed': 'Orden ejecutada',
        'error_occurred': 'Error en el sistema',
        'analysis_completed': 'Análisis completado'
    }
    
    @staticmethod
    def validar():
        """Valida que la configuración sea correcta"""
        if not WebhookConfig.URLS and WebhookConfig.ENABLED:
            logger.warning("⚠️  URLs de Webhook no configuradas")
            return False
        logger.info("✓ Configuración de Webhooks validada")
        return True

def validar_todas_las_apis():
    """Valida todas las configuraciones de APIs"""
    logger.info("🔍 Validando configuraciones de APIs...")
    
    apis_ok = 0
    apis_total = 4
    
    if BinanceConfig.validar():
        apis_ok += 1
    if SendGridConfig.validar():
        apis_ok += 1
    if TelegramConfig.validar():
        apis_ok += 1
    if WebhookConfig.validar():
        apis_ok += 1
    
    logger.info(f"✓ Validación completa: {apis_ok}/{apis_total} APIs configuradas")
    return apis_ok == apis_total
