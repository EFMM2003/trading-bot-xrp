# 📖 DOCUMENTACIÓN API

## Importar Módulos Principales

```python
from config.settings import Settings
from data.binance_connector import obtener_connector
from core.indicators import IndicadoresTecnicos
from core.signals import GeneradorSeñales
from ai.predictor import PredictorIA
from notifications.email_sender import EmailNotificador
from notifications.telegram_bot import TelegramNotificador
from notifications.webhook_handler import WebhookHandler
```

## Módulo: Trading Engine

### Obtener Connector de Binance

```python
from data.binance_connector import obtener_connector

binance = obtener_connector()

# Obtener velas
df = binance.obtener_velas('XRPUSDT', '1h', limite=100)

# Obtener precio actual
precio = binance.obtener_precio_actual('XRPUSDT')

# Obtener balance
balance = binance.obtener_balance()

# Crear orden
orden = binance.crear_orden_limit('XRPUSDT', 'BUY', 100, 1.10)

# Cancelar orden
binance.cancelar_orden('XRPUSDT', orden_id=123456)

# Órdenes abiertas
ordenes = binance.obtener_ordenes_abiertas('XRPUSDT')
```

## Módulo: Indicadores Técnicos

```python
from core.indicators import IndicadoresTecnicos
import pandas as pd

# Calcular todos los indicadores
df_con_indicadores = IndicadoresTecnicos.calcular_todos(df)

# Indicadores individuales
rsi = IndicadoresTecnicos.calcular_rsi(df['close'], periodo=14)
macd, signal, hist = IndicadoresTecnicos.calcular_macd(df['close'])
ema_9 = IndicadoresTecnicos.calcular_ema(df['close'], 9)
bb_up, bb_mid, bb_low = IndicadoresTecnicos.calcular_bandas_bollinger(df['close'])
```

## Módulo: Generador de Señales

```python
from core.signals import GeneradorSeñales

# Generar señal completa
señal = GeneradorSeñales.generar_señal(df_con_indicadores)

print(f"Recomendación: {señal['recomendacion']}")
print(f"Score: {señal['score']}/100")
print(f"Precio: ${señal['precio']:.4f}")
print(f"Confianza: {señal['confianza']}")

for señal_item in señal['señales']:
    print(f"  - {señal_item}")
```

## Módulo: Predicción IA

```python
from ai.predictor import PredictorIA, AnalizadorSentimiento

predictor = PredictorIA()

# Predicción a 4 horas
prediccion_4h = predictor.predecir_precio(df, horizonte_horas=4)
print(f"Precio predicho: ${prediccion_4h['precio_predicho']:.4f}")
print(f"Confianza: {prediccion_4h['confianza']}%")
print(f"Tendencia: {prediccion_4h['tendencia']}")

# Predicción a 24 horas
prediccion_24h = predictor.predecir_precio(df, horizonte_horas=24)

# Analizar patrón
patron = predictor.analizar_patron(df)
print(f"Volatilidad: {patron['volatilidad_anualizada']}%")
print(f"Riesgo: {patron['riesgo']}")

# Sentimiento
sentimiento = AnalizadorSentimiento.analizar_volumen(df)
print(f"Sentimiento: {sentimiento['sentimiento']}")
print(f"Ratio volumen: {sentimiento['ratio_volumen']}x")
```

## Módulo: Notificaciones

### Email

```python
from notifications.email_sender import EmailNotificador

email = EmailNotificador()

# Enviar alerta de señal
email.enviar_alerta_signal({
    'recomendacion': 'COMPRA FUERTE',
    'precio': 1.0998,
    'score': 75,
    'timestamp': datetime.now(),
    'señales': ['✓ RSI bajo', '✓ MACD positivo']
})

# Enviar alerta de error
email.enviar_alerta_error("Error conectando a BD")
```

### Telegram

```python
from notifications.telegram_bot import TelegramNotificador

telegram = TelegramNotificador()

# Enviar alerta
telegram.enviar_alerta_signal(signal_info)
telegram.enviar_alerta_error("Error del sistema")
```

### Webhooks

```python
from notifications.webhook_handler import WebhookHandler

webhook = WebhookHandler()

# Enviar señal a webhooks configurados
webhook.enviar_signal(signal_info)

# Enviar error
webhook.enviar_error("Error detectado")
```

## Módulo: Configuración

```python
from config.settings import Settings
from config.constants import RECOMENDACIONES, INDICADORES

settings = Settings()

print(f"Símbolo: {settings.TRADING_SYMBOL}")
print(f"Intervalo: {settings.TRADING_INTERVAL}")
print(f"BD: {settings.DATABASE_URL}")

# Validar
if settings.validar():
    print("Configuración OK")

# Mostrar
settings.mostrar()
```

## Flujo Completo de Trading

```python
from data.binance_connector import obtener_connector
from core.indicators import IndicadoresTecnicos
from core.signals import GeneradorSeñales
from ai.predictor import PredictorIA
from notifications.email_sender import EmailNotificador
from notifications.telegram_bot import TelegramNotificador
from datetime import datetime

# 1. Obtener datos
binance = obtener_connector()
df = binance.obtener_velas('XRPUSDT', '1h', 100)

# 2. Calcular indicadores
df = IndicadoresTecnicos.calcular_todos(df)

# 3. Generar señal
señal = GeneradorSeñales.generar_señal(df)

# 4. Predicción IA
predictor = PredictorIA()
prediccion = predictor.predecir_precio(df, 4)

# 5. Notificar
if señal['score'] >= 70:
    email = EmailNotificador()
    email.enviar_alerta_signal(señal)
    
    telegram = TelegramNotificador()
    telegram.enviar_alerta_signal(señal)

print(f"\n{señal['emoji']} {señal['recomendacion']}")
print(f"Score: {señal['score']}/100")
print(f"Predicción 4h: ${prediccion['precio_predicho']:.4f}")
```

## Manejo de Errores

```python
from config.logger_config import logger
from data.binance_connector import obtener_connector

try:
    binance = obtener_connector()
    if not binance.conectado:
        raise Exception("No se pudo conectar a Binance")
    
    df = binance.obtener_velas('XRPUSDT', '1h')
    if df is None:
        raise Exception("No se obtuvieron datos")
    
    # Procesar...
    
except Exception as e:
    logger.error(f"Error en flujo principal: {str(e)}")
    # Notificar error
```

## Configuración Avanzada

```python
from config.settings import Settings

# Cambiar parámetros temporalmente
settings = Settings()
settings.TRADING_SYMBOL = 'BTCUSDT'
settings.CANDLES_LIMIT = 200
settings.RSI_PERIOD = 21

# Esto no persiste, solo para sesión actual
```

## Acceso a Base de Datos

```python
from config.db_config import SessionLocal
from sqlalchemy import text

db = SessionLocal()

try:
    # Ejecutar query SQL crudo
    resultado = db.execute(text("""
        SELECT * FROM trades 
        WHERE timestamp > NOW() - INTERVAL 7 DAY
        ORDER BY timestamp DESC
    """))
    
    for fila in resultado:
        print(fila)
        
finally:
    db.close()
```

## Logging

```python
from config.logger_config import logger, audit_logger, trading_logger

# Logger general
logger.info("Información del sistema")
logger.warning("Advertencia")
logger.error("Error detectado")

# Logger de auditoría (seguridad)
audit_logger.info("LOGIN | User: EFMM2003 | IP: 192.168.1.1")
audit_logger.info("API_KEY_ROTATED | Antigua: xxx...")

# Logger de trading
trading_logger.info("ORDER_EXECUTED | BUY 100 XRP @ 1.10")
trading_logger.info("SIGNAL_CHANGE | Score: 68 -> 75 | 🟡->🟢")
```

---

Para más detalles, revisa el código fuente de cada módulo.
