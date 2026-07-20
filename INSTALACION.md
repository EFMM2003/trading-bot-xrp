# 📚 INSTALACIÓN Y CONFIGURACIÓN

## Requisitos Previos

- **Python 3.9+**
- **PostgreSQL 12+**
- **Redis 6+**
- **pip** (gestor de paquetes Python)
- Cuenta en **Binance** con API habilitada

## Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/EFMM2003/trading-bot-xrp.git
cd trading-bot-xrp
```

## Paso 2: Crear Entorno Virtual

```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

## Paso 3: Instalar Dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Paso 4: Configurar Variables de Entorno

### Crear archivo .env

```bash
cp .env.example .env
```

### Editar .env con tus credenciales

```env
# ============= BINANCE API =============
BINANCE_API_KEY=tu_api_key_aqui
BINANCE_API_SECRET=tu_api_secret_aqui
USE_TESTNET=False

# ============= DATABASE PostgreSQL =============
DB_HOST=localhost
DB_PORT=5432
DB_USER=trading_user
DB_PASSWORD=tu_contraseña_segura
DB_NAME=xrp_trading_db

# ============= REDIS CACHE =============
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=

# ============= EMAIL ALERTS (SendGrid) =============
SENDGRID_API_KEY=tu_sendgrid_key_aqui
SENDGRID_FROM_EMAIL=alertas@tudominio.com
SENDGRID_TO_EMAIL=tu_email@gmail.com
EMAIL_ALERTS_ENABLED=True

# ============= TELEGRAM ALERTS =============
TELEGRAM_BOT_TOKEN=tu_bot_token_aqui
TELEGRAM_CHAT_ID=tu_chat_id_aqui
TELEGRAM_ALERTS_ENABLED=True

# ============= WEBHOOKS =============
WEBHOOK_URLS=https://tu-servidor.com/webhook,https://zapier.com/hooks/
WEBHOOK_ALERTS_ENABLED=True

# ============= SEGURIDAD =============
ENCRYPTION_KEY=tu_encryption_key_generada
JWT_SECRET=tu_jwt_secret_key_segura
```

## Paso 5: Obtener Credenciales

### 5.1 API Keys de Binance

1. Ir a https://www.binance.com/es/account/api-management
2. Crear nueva API Key
3. Configurar permisos:
   - ✓ Lectura de datos (Read only)
   - ✓ Spot trading
   - ✓ Lectura de órdenes
   - ✗ Transferencias (DESHABILITADO)
4. Copiar API Key y Secret al archivo .env
5. **Importante**: Activar restricción por IP

### 5.2 SendGrid (Alertas Email)

1. Crear cuenta en https://sendgrid.com
2. Ir a Settings → API Keys
3. Crear API Key (Full Access)
4. Copiar la clave a `SENDGRID_API_KEY` en .env

### 5.3 Telegram Bot

1. Hablar con @BotFather en Telegram
2. Comando: `/start`
3. Comando: `/newbot`
4. Seguir instrucciones y obtener token
5. Comando: `/getid` en tu bot para obtener Chat ID

### 5.4 Webhook URLs (Opcional)

Si usas Zapier, integración propia o similar:

1. Obtener URL del webhook
2. Configurar en `WEBHOOK_URLS` (separadas por comas)

## Paso 6: Configurar Base de Datos

### Con Docker Compose (Recomendado)

```bash
docker-compose up -d postgres redis
```

### Manualmente

#### PostgreSQL

```bash
# Ubuntu/Debian
sudo apt-get install postgresql postgresql-contrib
sudo systemctl start postgresql

# macOS
brew install postgresql
brew services start postgresql

# Crear usuario y base de datos
sudo -u postgres psql
CREATE USER trading_user WITH PASSWORD 'tu_contraseña';
CREATE DATABASE xrp_trading_db OWNER trading_user;
ALTER ROLE trading_user SET client_encoding TO 'utf8';
ALTER ROLE trading_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE trading_user SET default_transaction_deferrable TO on;
GRANT ALL PRIVILEGES ON DATABASE xrp_trading_db TO trading_user;
\q
```

#### Redis

```bash
# Ubuntu/Debian
sudo apt-get install redis-server
sudo systemctl start redis-server

# macOS
brew install redis
brew services start redis
```

## Paso 7: Inicializar Sistema

```bash
python -m scripts.initialize_system
```

Este script verifica:
- ✓ Ambiente y dependencias
- ✓ Variables de entorno
- ✓ Conexión a PostgreSQL
- ✓ Conexión a Redis
- ✓ Credenciales Binance

## Paso 8: Crear Tablas en BD

```bash
python -m scripts.setup_db
```

## Paso 9: Ejecutar el Sistema

```bash
python main.py
```

¡El sistema debería iniciarse y mostrar el menú principal!

---

## 🐳 Ejecución con Docker Compose

Alternativa simplificada:

```bash
# Copiar y configurar .env
cp .env.example .env
# Editar .env con tus credenciales

# Ejecutar todo (BD + Redis + App)
docker-compose up --build
```

---

## 🔧 Troubleshooting

### Error: "No module named 'binance'"
```bash
pip install -r requirements.txt --upgrade
```

### Error: "Could not connect to PostgreSQL"
```bash
# Verificar que PostgreSQL está corriendo
sudo systemctl status postgresql

# Verificar credenciales en .env
psql -U trading_user -h localhost -d xrp_trading_db
```

### Error: "BINANCE_API_KEY no configurada"
```bash
# Verificar que .env existe y tiene valores
cat .env | grep BINANCE
```

### Error de importación de módulos
```bash
# Verificar que estás en el directorio correcto
pwd

# Verificar que venv está activado
which python  # debe mostrar ruta con venv
```

---

## ✅ Verificación Final

Después de la instalación, verifica que todo funciona:

```bash
# Prueba de Python
python -c "from config.settings import Settings; print('✓ Config OK')"

# Prueba de Binance
python -c "from data.binance_connector import obtener_connector; c = obtener_connector(); print('✓ Binance OK')"

# Prueba de BD
python -c "from config.db_config import verificar_conexion_bd; print('✓ BD OK' if verificar_conexion_bd() else '✗ BD ERROR')"
```

Si todo sale bien, ejecuta:

```bash
python main.py
```

¡Listo para operar! 🚀
