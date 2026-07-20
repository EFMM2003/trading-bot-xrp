# 🚀 Sistema Inteligente de Trading XRP/USDT

## Descripción

Sistema profesional de trading semi-automático para el par XRP/USDT en Binance Spot. Combina análisis técnico avanzado con inteligencia artificial para generar señales de compra y venta precisas.

## Características Principales

### 📊 Análisis Técnico
- **RSI** (Índice de Fuerza Relativa)
- **MACD** (Convergencia Divergencia de Medias Móviles)
- **Medias Móviles Exponenciales** (EMA 9, 21, 50)
- **Bandas de Bollinger**
- **Análisis de Volumen**

### 🤖 Inteligencia Artificial
- Modelo Ensemble (Prophet + LSTM + XGBoost)
- Predicción de precios a 4h y 24h
- Análisis de sentimiento
- Detección de patrones avanzados

### 📱 Notificaciones
- ✉️ Alertas por Email (SendGrid)
- 💬 Alertas por Telegram Bot
- 🔗 Webhooks configurables
- 📊 Dashboard en tiempo real

### 🛡️ Seguridad
- Encriptación AES-256
- JWT para autenticación
- Rate limiting
- Auditoría completa de acciones
- IP Whitelist

### 📈 Gestión de Datos
- PostgreSQL para persistencia
- Redis para caché
- Backups automáticos
- Histórico completo de operaciones

## Requisitos

- Python 3.9+
- PostgreSQL 12+
- Redis 6+
- pip (gestor de paquetes)

## Instalación

### 1. Clonar repositorio

```bash
git clone https://github.com/EFMM2003/trading-bot-xrp.git
cd trading-bot-xrp
```

### 2. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

```bash
cp .env.example .env
# Editar .env con tus credenciales
```

### 5. Inicializar base de datos

```bash
python -m scripts.setup_db
```

### 6. Ejecutar el sistema

```bash
python main.py
```

## Configuración

### Variables de Entorno Críticas

```env
# Binance API
BINANCE_API_KEY=tu_api_key
BINANCE_API_SECRET=tu_api_secret

# Base de Datos
DB_HOST=localhost
DB_USER=trading_user
DB_PASSWORD=secure_password
DB_NAME=xrp_trading_db

# Email
SENDGRID_API_KEY=tu_sendgrid_key
SENDGRID_TO_EMAIL=tu_email@gmail.com

# Telegram
TELEGRAM_BOT_TOKEN=tu_bot_token
TELEGRAM_CHAT_ID=tu_chat_id
```

## Uso

### Menú Principal

```
[1] 📊 ANÁLISIS DETALLADO
[2] ⏱️  MONITOREO CONTINUO
[3] ⚡ MODO AGRESIVO (1min)
[4] ⚙️  CONFIGURACIÓN AVANZADA
[5] 📈 HISTÓRICO & ESTADÍSTICAS
[6] 💾 GESTIONAR ALERTAS
[7] 🛡️  SEGURIDAD & API
[8] 🔌 ESTADO DEL SISTEMA
[9] ❌ SALIR
```

### Ejemplos de Uso

#### Análisis Rápido
```python
from core.trading_engine import TradingEngine

engine = TradingEngine()
resultado = engine.analizar_ahora()
print(f"Recomendación: {resultado['recommendation']}")
```

#### Monitoreo Continuo
```python
from core.trading_engine import TradingEngine

engine = TradingEngine()
engine.iniciar_monitoreo(intervalo_minutos=5)
```

## Indicadores de Rendimiento

- **Score de Trading**: 0-100 (Recomendación consolidada)
- **Confianza IA**: Porcentaje de certeza de la predicción
- **Riesgo**: Bajo, Medio, Alto
- **P&L**: Ganancia/Pérdida acumulada

## Seguridad

⚠️ **IMPORTANTE:**
- Nunca compartas tus API Keys
- Usa credenciales diferentes para testnet y producción
- Activa 2FA en tu cuenta de Binance
- Restringe permisos API solo a lectura y trading
- No transfirencias fondos desde las credenciales del bot

## Estructura de Carpetas

```
trading-bot-xrp/
├── config/              # Configuración
├── core/                # Motor de trading
├── ai/                  # Modelos IA/ML
├── data/                # Gestión de datos
├── security/            # Seguridad
├── notifications/       # Alertas
├── ui/                  # Interfaz usuario
├── logs/                # Archivos de log
├── tests/               # Tests
└── main.py              # Punto de entrada
```

## Roadmap

- [ ] Integración con más exchanges
- [ ] API REST pública
- [ ] Aplicación web (frontend)
- [ ] Trading completamente automático
- [ ] Backtest engine mejorado
- [ ] Copy trading
- [ ] Social trading

## Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## Licencia

Propietaria - Todos los derechos reservados

## Soporte

Para soporte y reportar bugs, abre un issue en GitHub.

## Aviso Legal

⚠️ **RIESGO FINANCIERO:**
Este software se proporciona "tal cual" sin garantías. El trading con criptomonedas conlleva riesgos significativos. No inviertas dinero que no puedas permitirte perder. Los resultados pasados no garantizan resultados futuros.

---

**Versión**: 2.0.0  
**Última actualización**: 2026-07-20  
**Autor**: Arquitecto de Software Principal + Quant Developer
