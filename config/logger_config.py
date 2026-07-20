"""
Configuración del Sistema de Logging
Logs centralizados para todo el sistema
"""

import logging
import logging.handlers
from pathlib import Path
from datetime import datetime
from config.settings import Settings

def setup_logger(nombre_modulo: str) -> logging.Logger:
    """
    Configura un logger para un módulo específico
    
    Args:
        nombre_modulo: Nombre del módulo que usa el logger
        
    Returns:
        Logger configurado
    """
    settings = Settings()
    logger = logging.getLogger(nombre_modulo)
    logger.setLevel(logging.DEBUG if settings.DEBUG_MODE else logging.INFO)
    
    # Formato de logs
    formato = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Handler para archivo de sistema
    handler_sistema = logging.handlers.RotatingFileHandler(
        settings.LOG_FILE_SYSTEM,
        maxBytes=10*1024*1024,  # 10 MB
        backupCount=5
    )
    handler_sistema.setLevel(logging.DEBUG)
    handler_sistema.setFormatter(formato)
    logger.addHandler(handler_sistema)
    
    # Handler para archivo de errores
    handler_errores = logging.handlers.RotatingFileHandler(
        settings.LOG_FILE_ERRORS,
        maxBytes=10*1024*1024,
        backupCount=5
    )
    handler_errores.setLevel(logging.ERROR)
    handler_errores.setFormatter(formato)
    logger.addHandler(handler_errores)
    
    # Handler para consola
    handler_consola = logging.StreamHandler()
    handler_consola.setLevel(logging.INFO if not settings.DEBUG_MODE else logging.DEBUG)
    handler_consola.setFormatter(formato)
    logger.addHandler(handler_consola)
    
    return logger

def setup_audit_logger() -> logging.Logger:
    """
    Configura un logger específico para auditoría
    
    Returns:
        Logger de auditoría
    """
    settings = Settings()
    logger_auditoria = logging.getLogger('auditoria')
    logger_auditoria.setLevel(logging.INFO)
    
    # Formato detallado para auditoría
    formato_audit = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    handler_audit = logging.handlers.RotatingFileHandler(
        settings.LOG_FILE_AUDIT,
        maxBytes=20*1024*1024,  # 20 MB
        backupCount=10
    )
    handler_audit.setFormatter(formato_audit)
    logger_auditoria.addHandler(handler_audit)
    
    return logger_auditoria

def setup_trading_logger() -> logging.Logger:
    """
    Configura un logger específico para trading
    
    Returns:
        Logger de trading
    """
    settings = Settings()
    logger_trading = logging.getLogger('trading')
    logger_trading.setLevel(logging.INFO)
    
    formato_trading = logging.Formatter(
        '%(asctime)s | TRADING | %(levelname)-8s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    handler_trading = logging.handlers.RotatingFileHandler(
        settings.LOG_FILE_TRADING,
        maxBytes=20*1024*1024,
        backupCount=10
    )
    handler_trading.setFormatter(formato_trading)
    logger_trading.addHandler(handler_trading)
    
    return logger_trading

# Crear loggers globales
logger = setup_logger('sistema')
audit_logger = setup_audit_logger()
trading_logger = setup_trading_logger()
