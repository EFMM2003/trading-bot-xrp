"""
SISTEMA INTELIGENTE DE TRADING XRP/USDT
Punto de entrada principal de la aplicación
Versión: 2.0
Autor: Arquitecto de Software Principal + Quant Developer
"""

import sys
import os
from pathlib import Path

# Agregar raíz del proyecto al path
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

from config.settings import Settings
from config.constants import MENSAJES, COLORES
from config.logger_config import logger

def verificar_ambiente():
    """Verifica que el ambiente esté correctamente configurado"""
    logger.info("🔍 Verificando ambiente de ejecución...")
    
    # Verificar variables de entorno críticas
    env_requeridas = [
        'BINANCE_API_KEY',
        'BINANCE_API_SECRET',
        'DB_HOST',
        'DB_USER',
        'DB_PASSWORD'
    ]
    
    faltantes = []
    for var in env_requeridas:
        if not os.getenv(var):
            faltantes.append(var)
    
    if faltantes:
        logger.warning(f"⚠️  Variables de entorno faltantes: {', '.join(faltantes)}")
        logger.warning("Por favor, configura el archivo .env")
        return False
    
    logger.info("✓ Verificación completada")
    return True

def inicializar_sistema():
    """Inicializa todos los componentes del sistema"""
    logger.info("🚀 Inicializando Sistema de Trading XRP/USDT v2.0...")
    
    try:
        # Cargar configuración
        settings = Settings()
        logger.info(f"✓ Configuración cargada (Ambiente: {settings.ENVIRONMENT})")
        
        # Validar configuración
        if not settings.validar():
            logger.error("❌ Configuración inválida")
            return False, None
        
        return True, settings
        
    except Exception as e:
        logger.error(f"❌ Error durante inicialización: {str(e)}")
        return False, None

def mostrar_banner():
    """Muestra el banner de bienvenida"""
    print("\n")
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 78 + "║")
    print("║" + "🚀 SISTEMA INTELIGENTE DE TRADING XRP/USDT 🚀".center(78) + "║")
    print("║" + "Versión 2.0 | Arquitectura Profesional | Producción Ready".center(78) + "║")
    print("║" + " " * 78 + "║")
    print("║" + "Análisis Técnico + IA/ML + Trading Semi-Automático".center(78) + "║")
    print("║" + "Email + Telegram + Webhooks + Base de Datos Segura".center(78) + "║")
    print("║" + " " * 78 + "║")
    print("╚" + "═" * 78 + "╝")
    print()

def main():
    """Función principal"""
    
    # Verificar ambiente
    if not verificar_ambiente():
        print("\n❌ Por favor, configura las variables de entorno en .env")
        sys.exit(1)
    
    # Inicializar sistema
    exito, settings = inicializar_sistema()
    
    if not exito:
        print("\n❌ No se pudo inicializar el sistema. Revisa los logs para más detalles.")
        sys.exit(1)
    
    # Mostrar bienvenida
    mostrar_banner()
    print("✓ Sistema inicializado correctamente\n")
    print("Próximos pasos:")
    print("  1. Configura tu API Key de Binance en .env")
    print("  2. Configura tu base de datos PostgreSQL")
    print("  3. Ejecuta: python -m scripts.setup_db")
    print("  4. Ejecuta: python main.py (nuevamente)\n")
    
    # Mostrar configuración actual
    settings.mostrar()
    
    logger.info("Sistema inicializado y listo para usar")

if __name__ == "__main__":
    main()
