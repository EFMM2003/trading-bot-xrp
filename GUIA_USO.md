# 🚀 GUÍA DE USO - SISTEMA DE TRADING XRP/USDT

## Inicio Rápido

```bash
# 1. Activar entorno virtual
source venv/bin/activate

# 2. Ejecutar el sistema
python main.py
```

## 📊 Pantalla Principal

Al ejecutar `python main.py` verás:

```
╔══════════════════════════════════════════════════════════════════════════╗
║  🚀 SISTEMA INTELIGENTE DE TRADING XRP/USDT v2.0                       ║
║     Análisis Técnico + IA | Email + Telegram + Webhooks                 ║
╚══════════════════════════════════════════════════════════════════════════╝

[1] 📊 ANÁLISIS TÉCNICO DETALLADO
[2] ⏱️  MONITOREO CONTINUO (5 min)
[3] ⚡ MODO AGRESIVO (1 min)
[4] ⚙️  CONFIGURACIÓN AVANZADA
[5] 📈 HISTÓRICO & ESTADÍSTICAS
[6] 💾 GESTIONAR ALERTAS
[7] 🛡️  SEGURIDAD & API
[8] 🔌 ESTADO DEL SISTEMA
[0] ❌ SALIR
```

## 🎯 Opciones Principales

### [1] Análisis Técnico Detallado

Muestra un análisis completo **una sola vez**:

```
✓ Indicadores calculados (RSI, MACD, EMA, Bollinger)
✓ Predicción IA para 4h y 24h
✓ Score de confianza (0-100)
✓ Recomendación: COMPRA / VENTA / NEUTRAL
✓ Niveles clave de resistencia y soporte
```

**Cuándo usar:**
- Análisis puntual antes de tomar decisión
- Verificar estado actual del mercado
- Confirmación antes de orden manual

### [2] Monitoreo Continuo (5 minutos)

Chequea cada **5 minutos** sin parar:

```
⏰ [14:35] Chequeo #47 | Precio: 1.0998 | Score: 68 | 🟡 CONSIDERAR COMPRA
⏰ [14:30] Chequeo #46 | Precio: 1.0996 | Score: 68 | 🟡 CONSIDERAR COMPRA
⏰ [14:25] Chequeo #45 | Precio: 1.0992 | Score: 67 | 🟡 CONSIDERAR COMPRA

[Presiona CTRL+C para detener]
```

**Cuándo usar:**
- Monitoreo de larga duración
- Dejar corriendo en background
- Alertas cada 5 minutos por Telegram

### [3] Modo Agresivo (1 minuto)

Chequea cada **1 minuto** (más rápido):

```
⏰ [14:36] Chequeo #63 | Precio: 1.0999 | Score: 69 | 🟡 CONSIDERAR COMPRA
⏰ [14:35] Chequeo #62 | Precio: 1.0998 | Score: 68 | 🟡 CONSIDERAR COMPRA
⏰ [14:34] Chequeo #61 | Precio: 1.0997 | Score: 68 | 🟡 CONSIDERAR COMPRA
```

**Cuándo usar:**
- Traders de corto plazo
- Volatilidad alta
- Estar cerca de la pantalla

### [4] Configuración Avanzada

Ajusta parámetros del sistema:

```
⚙️ PARÁMETROS DE TRADING:
  Símbolo: XRPUSDT
  Intervalo: 1H
  Cantidad velas: 100

⚙️ INDICADORES:
  RSI Período: 14
  MACD Fast: 12, Slow: 26, Signal: 9
  Bollinger: 20 período, 2 desv. estándar

⚙️ UMBRALES DE ALERTA:
  Score mínimo compra: 60
  Score máximo venta: 40
```

**Parámetros recomendados:**
- Traders principiantes: Mantener defaults
- Traders expertos: Ajustar según experiencia

### [5] Histórico & Estadísticas

Ve tu rendimiento histórico:

```
📊 ESTADÍSTICAS TRADING:
  Total de trades: 45
  Trades ganadores: 32 (71%)
  Trades perdedores: 13 (29%)
  
  Ganancia total: +$2,345.67
  Ganancia media: +$52.13
  Máxima ganancia: +$234.56
  Máxima pérdida: -$89.23
  
  Ratio de ganancias/pérdidas: 2.14
  Factor de beneficio: 1.89
  Drawdown máximo: 12.3%
```

### [6] Gestionar Alertas

Configura dónde recibir notificaciones:

```
📧 EMAIL: alertas@gmail.com ✓
  ☑ Cambios de señal
  ☑ Órdenes ejecutadas
  ☑ Errores del sistema

📱 TELEGRAM: @TuBot ✓
  ☑ Alertas en tiempo real
  ☑ Resumen diario
  ☑ Notificaciones críticas

🔗 WEBHOOK: https://tu-servidor.com ✓
  ☑ JSON con todos los datos
  ☑ Integración con otros sistemas
```

### [7] Seguridad & API

Gestión de credenciales:

```
🔐 ESTADO DE SEGURIDAD:
  Encriptación AES-256: ✓
  API Binance: ✓ Conectada
  IP Whitelist: ✓ Activa
  2FA Binance: ✓ Habilitado
  
🔑 CREDENCIALES:
  [🔄 Rotar API Keys]
  [🧪 Test Conexión]
  [📋 Ver Auditoría]
```

### [8] Estado del Sistema

Monitoreo de recursos:

```
💻 SISTEMA:
  CPU: 12.5% | Memoria: 34.2% | Disco: 45.8%
  
📡 CONECTIVIDAD:
  Binance API: ✓ OK (latencia: 245ms)
  PostgreSQL: ✓ OK
  Redis: ✓ OK
  SendGrid: ✓ OK
  Telegram: ✓ OK
```

## 📈 Interpretando las Señales

### Scores

```
🟢 COMPRA FUERTE (70-100)
   Compra con alta confianza
   RSI bajo + MACD positivo + Tendencia alcista

🟡 CONSIDERAR COMPRA (60-69)
   Señal moderada de compra
   Esperar confirmación adicional

⚪ NEUTRAL (40-59)
   Sin tendencia clara
   Esperar más información

🟠 CONSIDERAR VENTA (31-39)
   Señal moderada de venta
   Esperar confirmación adicional

🔴 VENTA FUERTE (0-30)
   Venta con alta confianza
   RSI alto + MACD negativo + Tendencia bajista
```

### Indicadores Clave

**RSI (Índice de Fuerza Relativa)**
```
< 30:  Sobreventa (posible rebote alcista)
30-70: Neutral
> 70:  Sobrecompra (posible corrección bajista)
```

**MACD (Moving Average Convergence Divergence)**
```
Si MACD > Signal: Momentum alcista
Si MACD < Signal: Momentum bajista
Cruce: Cambio de tendencia potencial
```

**EMA (Media Móvil Exponencial)**
```
EMA9 > EMA21 > EMA50: Tendencia alcista fuerte
EMA9 < EMA21 < EMA50: Tendencia bajista fuerte
Desordenadas: Sin tendencia clara
```

**Bollinger Bands**
```
Precio < Banda Inferior: Sobreventa
Precio > Banda Superior: Sobrecompra
Precio en medio: Precio justo
```

## 💡 Estrategia Recomendada

### Para Principiantes

```
1. Usa TESTNET primero
   USE_TESTNET=True en .env

2. Comienza con [1] Análisis puntual
   Aprende a leer los indicadores

3. Luego [2] Monitoreo continuo
   Observa patrones durante 1-2 semanas

4. Confirma con CONFIRMACIÓN MANUAL
   No uses automático todavía

5. Pequeñas inversiones
   MAX_ORDER_SIZE_USDT=50 USDT
```

### Para Traders Expertos

```
1. Usa [3] Modo agresivo
   Aprovecha volatilidad corto plazo

2. Integra webhooks a tu sistema
   Combina con tus propios indicadores

3. Aumenta posición gradualmente
   MAX_ORDER_SIZE_USDT=500+ USDT

4. Mantén monitoreo 24/7
   Alertas Telegram activas

5. Análisis post-trade
   Revisa logs diariamente
```

## 🎯 Ejemplo de Sesión de Trading

```bash
# 09:00 - Análisis inicial
$ python main.py
> Opción: 1
# Ver análisis completo: Score 68, 🟡 CONSIDERAR COMPRA

# 09:15 - Confirmar con monitoreo
> Opción: 2
# Monitoreo 5 min
# 09:15 - Score 68
# 09:20 - Score 70 ← Mejora
# 09:25 - Score 72 ← Sigue mejorando
# 09:30 - Score 75 - Ahora es 🟢 COMPRA FUERTE

# 09:31 - EJECUTAR COMPRA MANUAL EN BINANCE
# Cantidad: 100 XRP
# Precio límite: 1.1000

# 09:32 - Recibir alerta por Telegram/Email
# ✓ Orden ejecutada

# 10:00 - Monitorear ganancia
> Opción: 5
# Ver histórico y P&L

# 14:00 - EJECUTAR VENTA CUANDO GOAL SE ALCANCE
# Precio objetivo: 1.1150 (+1.36%)

# 14:05 - Orden ejecutada
# Ganancia: +$12.34
```

## ⚠️ Cosas Importantes

**NO es automático 100%**
- El sistema GENERA SEÑALES
- TÚ CONFIRMAS y EJECUTAS la orden en Binance
- El sistema monitorea pero no compra/vende

**Semi-automático significa:**
- ✓ Análisis automático
- ✓ Alertas automáticas
- ✓ Monitoreo automático
- ✗ Órdenes manuales en Binance

## 📞 Troubleshooting Rápido

```bash
# No conecta a Binance
> python -c "from data.binance_connector import obtener_connector; obtener_connector()"
# Verifica API Key y Secret en .env

# No recibe alertas
> Opción: 6 (Gestionar Alertas)
# Verifica que Email/Telegram están habilitados

# Score siempre igual
> Opción: 4 (Configuración)
# Aumenta cantidad de velas a 150-200

# Errores de base de datos
> python -m scripts.setup_db
# Reinicia las tablas
```

---

¡Listo para comenzar a operar! 🚀

Recuerda: **Operaciones seguras, rentabilidad a largo plazo**
