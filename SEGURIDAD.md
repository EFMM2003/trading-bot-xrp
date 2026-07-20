# 🛡️ SEGURIDAD Y MEJORES PRÁCTICAS

## ⚠️ ADVERTENCIA CRÍTICA

**NUNCA:**
- ✗ Compartas tus API Keys
- ✗ Comitees el archivo `.env` a Git
- ✗ Uses las mismas credenciales en testnet y producción
- ✗ Habilites transfer/withdraw en permisos API
- ✗ Dejes dinero en la cuenta del bot sin protección

## 🔐 Configuración de Seguridad Binance

### 1. Restricción de IP

```
En Binance Account → API Management:
- Habilitar IP Whitelist
- Agregar solo tu IP actual
- Ejemplo: 192.168.1.100/32 (tu IP privada)
- O 203.0.113.45 (tu IP pública si es estática)
```

### 2. Permisos API (Lo Mínimo)

```
✓ Enable Reading
✓ Enable Spot & Margin Trading User Stream
✓ Disable IP restriction (opcional)
✗ DON'T enable withdrawals
✗ DON'T enable fund transfers
```

### 3. Activar 2FA

```
1. Ir a Account → Security
2. Habilitar Google Authenticator
3. Guardar códigos de backup en lugar seguro
4. Verificar con 2FA cada login
```

### 4. Crear API Key con Restricciones

```bash
# Parámetros recomendados:
- Trading enabled: YES
- Margin trading: NO
- Future trading: NO
- Withdrawals: NO
- Internal transfer: NO
- Sub-account transfer: NO
- IP restriction: YES (tu IP)
```

## 🔑 Gestión de Credenciales

### Archivo .env

```bash
# ✓ CORRECTO:
# .env en root, nunca commitear
# Permisos: chmod 600 .env

# ✗ INCORRECTO:
# Credenciales en código
# Credenciales en comentarios
# Compartir .env
```

### Rotación de Credenciales

```bash
# Cada 90 días:
1. Generar nueva API Key en Binance
2. Actualizar .env
3. Probar funcionamiento
4. Eliminar API Key antigua en Binance
```

## 🔒 Encriptación

El sistema encripta automáticamente:
- ✓ API Keys almacenadas en BD
- ✓ Tokens JWT
- ✓ Datos sensibles en logs

```python
from security.encryption import EncriptadorAES

encriptador = EncriptadorAES()
datos_encriptados = encriptador.encriptar("dato_sensible")
datos_original = encriptador.desencriptar(datos_encriptados)
```

## 📋 Auditoría y Logs

### Archivos de Log Automáticos

```
logs/
├── system.log       # Logs generales
├── errors.log       # Errores
├── audit.log        # Auditoría (logins, cambios)
└── trading.log      # Operaciones de trading
```

### Monitoreo de Auditoría

```bash
# Ver acciones críticas
tail -f logs/audit.log | grep "CRITICAL"

# Ver errores de API
tail -f logs/errors.log | grep "BINANCE"

# Ver todos los trades
tail -f logs/trading.log
```

## 🛡️ Rate Limiting

El sistema implementa:
- **API Binance**: 1200 llamadas/minuto (límite Binance)
- **Email**: 100/hora (SendGrid)
- **Telegram**: 30/minuto
- **Webhook**: 60/minuto

```python
from config.constants import RATE_LIMITS

print(RATE_LIMITS)
# {'API_BINANCE_CALLS_PER_MINUTE': 1200, ...}
```

## 🚨 Detección de Anomalías

El sistema alerta cuando:
- ✓ Múltiples fallos de API
- ✓ Cambios inesperados en precio (>10%)
- ✓ Órdenes rechazadas
- ✓ Conexión perdida a BD
- ✓ Uso anómalo de recursos

## 📱 Seguridad en Alertas

### Email
- ✓ Conexión TLS/SSL
- ✓ Verificación de origen
- ✓ No incluir credenciales en email

### Telegram
- ✓ Bot token protegido
- ✓ Chat ID privado
- ✓ Mensajes sin datos sensibles

### Webhooks
- ✓ HTTPS obligatorio
- ✓ Secret token para verificación
- ✓ Timeout de 30 segundos
- ✓ Reintentos con backoff exponencial

## 🔄 Backup y Recuperación

### Backup Automático Diario

```bash
# En 23:00 UTC se realiza automáticamente
# Archivos en: backups/

# Backup manual
python -m scripts.backup_data

# Restaurar
python -m scripts.restore_data --backup 2026-07-20-0000
```

### Retención de Datos

```
Trades:     730 días (2 años)
Signals:    365 días (1 año)
Alertas:    90 días (3 meses)
Auditoría:  180 días (6 meses)
```

## ✅ Checklist de Seguridad

Antes de usar en producción:

- [ ] .env configurado con credenciales reales
- [ ] .env en .gitignore
- [ ] Permisos API restringidos en Binance
- [ ] IP Whitelist activada
- [ ] 2FA activado en Binance
- [ ] PostgreSQL con contraseña fuerte
- [ ] Redis con contraseña (en producción)
- [ ] HTTPS habilitado (si expones interfaz)
- [ ] Backups configurados
- [ ] Logs monitoreados
- [ ] Alertas por email/Telegram activas
- [ ] Testnet probado antes de producción
- [ ] Cantidad inicial de prueba (no invertir todo)

## 🚀 Mejores Prácticas

1. **Ambiente de Testnet Primero**
   ```env
   USE_TESTNET=True
   ```
   Prueba todo antes de producción

2. **Posición Inicial Pequeña**
   ```env
   MAX_ORDER_SIZE_USDT=100
   ```
   Aumenta gradualmente cuando confíes

3. **Monitoreo Continuo**
   ```bash
   watch -n 5 'tail -20 logs/trading.log'
   ```

4. **Alertas Activas**
   - Email: Cambios de señal
   - Telegram: En tiempo real
   - Webhook: Integración externa

5. **Revisión Periódica**
   - Diaria: Logs de trading
   - Semanal: P&L y estadísticas
   - Mensual: Revisión de seguridad

## 📞 Soporte de Seguridad

Si detectas problema de seguridad:

1. **NO** lo publiques públicamente
2. Contacta a través de issues privadas
3. Incluye detalles sin exponer credenciales
4. Espera respuesta en 24 horas

---

**Recuerda**: Tu seguridad es responsabilidad tuya. Mantén vigilancia constante. 🛡️
