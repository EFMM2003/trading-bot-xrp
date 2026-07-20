"""
Configuración Global del Sistema
Gestión centralizada de parámetros y variables
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from typing import Optional

# Cargar variables de entorno
load_dotenv()

class Settings:
    """Clase de configuración centralizada"""
    
    # Rutas
    PROJECT_ROOT = Path(__file__).parent.parent
    LOGS_DIR = PROJECT_ROOT / "logs"
    DATA_DIR = PROJECT_ROOT / "data_storage"
    
    # Asegurar que los directorios existan
    LOGS_DIR.mkdir(exist_ok=True)
    DATA_DIR.mkdir(exist_ok=True)
    
    # ============= ENVIRONMENT =============
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"
    TIMEZONE = os.getenv("TIMEZONE", "UTC")
    
    # ============= LOGGING =============
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE_SYSTEM = LOGS_DIR / "system.log"
    LOG_FILE_ERRORS = LOGS_DIR / "errors.log"
    LOG_FILE_AUDIT = LOGS_DIR / "audit.log"
    LOG_FILE_TRADING = LOGS_DIR / "trading.log"
    
    # ============= BINANCE API =============
    BINANCE_API_KEY = os.getenv("BINANCE_API_KEY", "")
    BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET", "")
    BINANCE_BASE_URL = "https://api.binance.com"
    BINANCE_TESTNET_URL = "https://testnet.binance.vision"
    USE_TESTNET = os.getenv("USE_TESTNET", "False").lower() == "true"
    BINANCE_TIMEOUT = 30  # segundos
    
    # ============= TRADING PARAMETERS =============
    TRADING_SYMBOL = "XRPUSDT"
    TRADING_INTERVAL = "1h"  # 1m, 5m, 15m, 1h, 4h, 1d
    CANDLES_LIMIT = 100
    
    # RSI Parameters
    RSI_PERIOD = 14
    RSI_OVERBOUGHT = 70
    RSI_OVERSOLD = 30
    
    # MACD Parameters
    MACD_FAST = 12
    MACD_SLOW = 26
    MACD_SIGNAL = 9
    
    # Bollinger Bands Parameters
    BB_PERIOD = 20
    BB_STD_DEV = 2
    
    # Signal Thresholds
    SIGNAL_BUY_THRESHOLD = 60
    SIGNAL_SELL_THRESHOLD = 40
    SIGNAL_NEUTRAL_RANGE = (40, 60)
    
    # Risk Management
    MAX_ORDER_SIZE_USDT = float(os.getenv("MAX_ORDER_SIZE_USDT", "500"))
    MAX_ORDERS_PER_HOUR = int(os.getenv("MAX_ORDERS_PER_HOUR", "50"))
    STOP_LOSS_PERCENTAGE = float(os.getenv("STOP_LOSS_PERCENTAGE", "2.0"))
    TAKE_PROFIT_PERCENTAGE = float(os.getenv("TAKE_PROFIT_PERCENTAGE", "5.0"))
    
    # ============= DATABASE =============
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", "5432"))
    DB_USER = os.getenv("DB_USER", "trading_user")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "secure_password")
    DB_NAME = os.getenv("DB_NAME", "xrp_trading_db")
    DB_DRIVER = "postgresql"
    
    @property
    def DATABASE_URL(self):
        """URL de conexión a PostgreSQL"""
        return f"{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    # ============= REDIS CACHE =============
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "")
    REDIS_DB = 0
    
    @property
    def REDIS_URL(self):
        """URL de conexión a Redis"""
        if self.REDIS_PASSWORD:
            return f"redis://:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"
    
    # ============= EMAIL (SendGrid) =============
    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", "")
    SENDGRID_FROM_EMAIL = os.getenv("SENDGRID_FROM_EMAIL", "noreply@trading.com")
    SENDGRID_TO_EMAIL = os.getenv("SENDGRID_TO_EMAIL", "usuario@gmail.com")
    EMAIL_ALERTS_ENABLED = os.getenv("EMAIL_ALERTS_ENABLED", "True").lower() == "true"
    
    # ============= TELEGRAM =============
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
    TELEGRAM_ALERTS_ENABLED = os.getenv("TELEGRAM_ALERTS_ENABLED", "True").lower() == "true"
    
    # ============= WEBHOOKS =============
    WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "tu_webhook_secret")
    WEBHOOK_URLS = os.getenv("WEBHOOK_URLS", "").split(",")
    WEBHOOK_TIMEOUT = 30
    WEBHOOK_RETRIES = 3
    WEBHOOK_ALERTS_ENABLED = os.getenv("WEBHOOK_ALERTS_ENABLED", "True").lower() == "true"
    
    # ============= AI/ML =============
    MODEL_TRAINING_DATA_DAYS = int(os.getenv("MODEL_TRAINING_DATA_DAYS", "365"))
    PREDICTION_INTERVAL_HOURS = [4, 24]  # Predicciones a 4h y 24h
    IA_CONFIDENCE_THRESHOLD = float(os.getenv("IA_CONFIDENCE_THRESHOLD", "0.65"))
    MODEL_UPDATE_INTERVAL_HOURS = 24  # Actualizar modelo cada 24 horas
    
    # ============= MONITORING =============
    HEALTH_CHECK_INTERVAL = 60  # segundos
    METRICS_UPDATE_INTERVAL = 30  # segundos
    SYSTEM_CHECK_ENABLED = True
    
    # ============= SECURITY =============
    ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY", "").encode() if os.getenv("ENCRYPTION_KEY") else None
    JWT_SECRET = os.getenv("JWT_SECRET", "tu_jwt_secret_key_cambiar_en_produccion")
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRATION_HOURS = 24
    
    # ============= RATE LIMITING =============
    API_RATE_LIMIT_CALLS = 1200
    API_RATE_LIMIT_PERIOD = 60  # segundos (por minuto)
    
    # ============= BACKUP =============
    BACKUP_ENABLED = True
    BACKUP_INTERVAL_HOURS = 24
    BACKUP_RETENTION_DAYS = 30
    
    @classmethod
    def validar(cls) -> bool:
        """Valida que la configuración sea correcta"""
        errores = []
        
        # Validar API Keys
        if not cls.BINANCE_API_KEY:
            errores.append("⚠️  BINANCE_API_KEY no configurada")
        if not cls.BINANCE_API_SECRET:
            errores.append("⚠️  BINANCE_API_SECRET no configurada")
        
        # Validar BD
        if not cls.DB_HOST:
            errores.append("⚠️  DB_HOST no configurada")
        
        if errores:
            for error in errores:
                print(error)
            return False
        
        return True
    
    @classmethod
    def mostrar(cls):
        """Muestra la configuración actual"""
        print("\n" + "="*80)
        print("CONFIGURACIÓN DEL SISTEMA")
        print("="*80)
        print(f"Ambiente:                  {cls.ENVIRONMENT}")
        print(f"Debug Mode:                {cls.DEBUG_MODE}")
        print(f"Timezone:                  {cls.TIMEZONE}")
        print(f"\nTradding Symbol:           {cls.TRADING_SYMBOL}")
        print(f"Trading Interval:          {cls.TRADING_INTERVAL}")
        print(f"\nBD Host:                   {cls.DB_HOST}:{cls.DB_PORT}")
        print(f"BD Name:                   {cls.DB_NAME}")
        print(f"\nRedis:                     {cls.REDIS_HOST}:{cls.REDIS_PORT}")
        print(f"Email Alerts:              {'✓ Activadas' if cls.EMAIL_ALERTS_ENABLED else '✗ Desactivadas'}")
        print(f"Telegram Alerts:           {'✓ Activadas' if cls.TELEGRAM_ALERTS_ENABLED else '✗ Desactivadas'}")
        print(f"Webhook Alerts:            {'✓ Activadas' if cls.WEBHOOK_ALERTS_ENABLED else '✗ Desactivadas'}")
        print("="*80 + "\n")

# Crear instancia global
settings = Settings()
