"""
Constantes del Sistema
Valores fijos y configuración estática
"""

# ============= INDICADORES TÉCNICOS =============
INDICADORES = {
    'RSI': {
        'nombre': 'Índice de Fuerza Relativa',
        'período': 14,
        'sobreventa': 30,
        'sobrecompra': 70,
        'neutral_min': 40,
        'neutral_max': 60
    },
    'MACD': {
        'nombre': 'Convergencia Divergencia de Medias Móviles',
        'fast': 12,
        'slow': 26,
        'signal': 9
    },
    'EMA': {
        'nombre': 'Media Móvil Exponencial',
        'periodos': [9, 21, 50]
    },
    'BOLLINGER': {
        'nombre': 'Bandas de Bollinger',
        'periodo': 20,
        'desviaciones': 2
    }
}

# ============= RECOMENDACIONES =============
RECOMENDACIONES = {
    'COMPRA_FUERTE': {
        'emoji': '🟢',
        'nombre': 'COMPRA FUERTE',
        'rango': (70, 100),
        'descripcion': 'Señal clara de compra con alta confianza'
    },
    'COMPRA': {
        'emoji': '🟡',
        'nombre': 'CONSIDERAR COMPRA',
        'rango': (60, 69),
        'descripcion': 'Señal de compra moderada'
    },
    'NEUTRAL': {
        'emoji': '⚪',
        'nombre': 'NEUTRAL',
        'rango': (40, 59),
        'descripcion': 'Sin tendencia clara, esperar confirmación'
    },
    'VENTA': {
        'emoji': '🟠',
        'nombre': 'CONSIDERAR VENTA',
        'rango': (31, 39),
        'descripcion': 'Señal de venta moderada'
    },
    'VENTA_FUERTE': {
        'emoji': '🔴',
        'nombre': 'VENTA FUERTE',
        'rango': (0, 30),
        'descripcion': 'Señal clara de venta con alta confianza'
    }
}

# ============= INTERVALOS DE VELAS =============
INTERVALOS_DISPONIBLES = {
    '1m': '1 minuto',
    '5m': '5 minutos',
    '15m': '15 minutos',
    '30m': '30 minutos',
    '1h': '1 hora',
    '4h': '4 horas',
    '1d': '1 día',
    '1w': '1 semana',
    '1M': '1 mes'
}

# ============= PARES DE TRADING =============
PARES_SOPORTADOS = [
    'XRPUSDT',
    'BTCUSDT',
    'ETHUSDT',
    'BNBUSDT',
    'ADAUSDT',
    'DOGEUSDT',
    'LITUSDT',
    'SOLUSDT'
]

# ============= TIPOS DE ÓRDENES =============
TIPOS_ORDENES = {
    'LIMIT': 'Orden limitada',
    'MARKET': 'Orden de mercado',
    'STOP_LOSS': 'Stop loss',
    'TAKE_PROFIT': 'Take profit'
}

# ============= ESTADOS DE ÓRDENES =============
ESTADOS_ORDENES = {
    'NEW': 'Nueva',
    'PARTIALLY_FILLED': 'Parcialmente ejecutada',
    'FILLED': 'Ejecutada',
    'CANCELED': 'Cancelada',
    'PENDING_CANCEL': 'Cancelación pendiente',
    'REJECTED': 'Rechazada',
    'EXPIRED': 'Expirada'
}

# ============= TIPOS DE ALERTAS =============
TIPOS_ALERTAS = {
    'SIGNAL_CHANGE': 'Cambio de señal',
    'PRICE_ALERT': 'Alerta de precio',
    'VOLUME_ALERT': 'Alerta de volumen',
    'TREND_CHANGE': 'Cambio de tendencia',
    'SYSTEM_ERROR': 'Error del sistema',
    'API_ERROR': 'Error de API',
    'DB_ERROR': 'Error de base de datos',
    'SCORE_THRESHOLD': 'Umbral de score alcanzado'
}

# ============= CANALES DE NOTIFICACIÓN =============
CANALES_NOTIFICACION = {
    'EMAIL': 'Correo electrónico',
    'TELEGRAM': 'Telegram Bot',
    'WEBHOOK': 'Webhook',
    'DASHBOARD': 'Dashboard'
}

# ============= NIVELES DE LOG =============
NIVELES_LOG = {
    'DEBUG': 10,
    'INFO': 20,
    'WARNING': 30,
    'ERROR': 40,
    'CRITICAL': 50
}

# ============= MENSAJES DEL SISTEMA =============
MENSAJES = {
    'BIENVENIDA': '¡Bienvenido al Sistema Inteligente de Trading XRP/USDT!',
    'INICIALIZANDO': '🚀 Inicializando sistema...',
    'INICIALIZADO': '✓ Sistema inicializado correctamente',
    'CONECTANDO_API': '📡 Conectando con API de Binance...',
    'API_CONECTADA': '✓ API de Binance conectada',
    'ERROR_API': '❌ Error al conectar con API de Binance',
    'ANALIZANDO': '📊 Analizando mercado...',
    'ANALISIS_COMPLETADO': '✓ Análisis completado',
    'MONITOREO_INICIADO': '▶️  Monitoreo iniciado',
    'MONITOREO_DETENIDO': '⏹️  Monitoreo detenido',
    'CONFIRMACION_COMPRA': '¿Confirmas ejecutar orden de COMPRA?',
    'CONFIRMACION_VENTA': '¿Confirmas ejecutar orden de VENTA?',
    'ORDEN_EJECUTADA': '✓ Orden ejecutada exitosamente',
    'ERROR_ORDEN': '❌ Error al ejecutar la orden',
    'SESION_CERRADA': '👋 Sesión cerrada. ¡Hasta pronto!',
    'ERROR_FATAL': '💥 Error fatal en el sistema'
}

# ============= COLORES (ANSI) =============
COLORES = {
    'VERDE': '\033[92m',
    'ROJO': '\033[91m',
    'AMARILLO': '\033[93m',
    'AZUL': '\033[94m',
    'MAGENTA': '\033[95m',
    'CIAN': '\033[96m',
    'BLANCO': '\033[97m',
    'GRIS': '\033[90m',
    'RESET': '\033[0m',
    'NEGRITA': '\033[1m',
    'SUBRAYADO': '\033[4m'
}

# ============= LÍMITES DE RATE LIMITING =============
RATE_LIMITS = {
    'API_BINANCE_CALLS_PER_MINUTE': 1200,
    'EMAIL_PER_HORA': 100,
    'TELEGRAM_POR_MINUTO': 30,
    'WEBHOOK_POR_MINUTO': 60
}

# ============= TIMEOUTS =============
TIMEOUTS = {
    'API_BINANCE': 30,
    'DATABASE': 10,
    'EMAIL': 30,
    'TELEGRAM': 30,
    'WEBHOOK': 30,
    'REDIS': 5
}

# ============= CONFIGURACIÓN DE PREDICCIÓN IA =============
PREDICCION_CONFIG = {
    'MODELOS': ['PROPHET', 'LSTM', 'XGBOOST'],
    'METODO_ENSEMBLE': 'PROMEDIO_PONDERADO',
    'PESOS_MODELOS': {
        'PROPHET': 0.35,
        'LSTM': 0.35,
        'XGBOOST': 0.30
    },
    'MIN_CONFIANZA': 0.65,
    'HORIZONTE_PREDICCION_4H': 4,
    'HORIZONTE_PREDICCION_24H': 24,
    'DATOS_ENTRENAMIENTO_MINIMO_DIAS': 90
}

# ============= CONFIGURACIÓN DE BACKUP =============
BACKUP_CONFIG = {
    'INTERVALO_HORAS': 24,
    'RETENCION_DIAS': 30,
    'COMPRESION': True,
    'ENCRIPTACION': True,
    'UBICACIONES': ['local', 'cloud']
}

# ============= UMBRAL DE RIESGO =============
RIESGO_PARAMETERS = {
    'RIESGO_BAJO': (0, 33),
    'RIESGO_MEDIO': (33, 66),
    'RIESGO_ALTO': (66, 100),
    'MAX_DRAWDOWN_PERMITIDO': 10,  # porcentaje
    'POSITION_SIZE_MAX': 5,  # porcentaje del capital
    'LEVERAGE_MAX': 1.0  # sin apalancamiento
}

# ============= ENDPOINTS API BINANCE =============
ENDPOINTS_BINANCE = {
    'KLINES': '/api/v3/klines',
    'TICKER': '/api/v3/ticker/24hr',
    'ACCOUNT': '/api/v3/account',
    'CREATE_ORDER': '/api/v3/order',
    'CANCEL_ORDER': '/api/v3/order',
    'ORDER_STATUS': '/api/v3/order',
    'OPEN_ORDERS': '/api/v3/openOrders',
    'ALL_ORDERS': '/api/v3/allOrders',
    'TRADES': '/api/v3/myTrades'
}

# ============= VERSIÓN DEL SISTEMA =============
VERSION_SISTEMA = "2.0.0"
VERSIÓN_API = "v3"
AUTOR = "Arquitecto de Software Principal + Quant Developer"
FECHA_CREACION = "2026-07-20"
LICENCIA = "Propietaria"

# ============= CONFIGURACIÓN DE AUDITORÍA =============
AUDITORIA = {
    'REGISTRAR_LOGINS': True,
    'REGISTRAR_OPERACIONES_CRITICAS': True,
    'REGISTRAR_CAMBIOS_CONFIGURACION': True,
    'REGISTRAR_ACCESO_API': True,
    'RETENCION_DIAS': 90,
    'ENCRIPTAR_LOGS_SENSIBLES': True
}
