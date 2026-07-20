"""
Script de inicialización del sistema
Configura todo antes de ejecutar
"""

import sys
from pathlib import Path
import os

# Agregar raíz del proyecto al path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from config.settings import Settings
from config.logger_config import logger
from config.api_config import validar_todas_las_apis
from config.db_config import verificar_conexion_bd
from security.api_key_manager import APIKeyManager

def verificar_ambiente():
    """Verifica el ambiente"""
    print("🔍 Verificando ambiente...")
    
    # Verificar .env
    if not Path(PROJECT_ROOT / '.env').exists():
        print("❌ Archivo .env no encontrado")
        print("   Ejecuta: cp .env.example .env")
        print("   Luego edita .env con tus credenciales")
        return False
    
    return True

def verificar_dependencias():
    """Verifica que las dependencias estén instaladas"""
    print("📦 Verificando dependencias...")
    
    try:
        import binance
        import pandas
        import numpy
        import sqlalchemy
        import redis
        print("✓ Dependencias verificadas")
        return True
    except ImportError as e:
        print(f"❌ Falta dependencia: {str(e)}")
        print("   Ejecuta: pip install -r requirements.txt")
        return False

def verificar_configuracion():
    """Verifica la configuración"""
    print("⚙️  Verificando configuración...")
    
    settings = Settings()
    
    if not settings.validar():
        print("❌ Configuración inválida")
        return False
    
    print("✓ Configuración verificada")
    return True

def verificar_conectividad():
    """Verifica conectividad con servicios externos"""
    print("🌐 Verificando conectividad...")
    
    # Verificar BD
    if not verificar_conexion_bd():
        print("⚠️  No se pudo conectar a PostgreSQL")
        return False
    
    # Verificar APIs
    if not validar_todas_las_apis():
        print("⚠️  Algunas APIs no están configuradas")
    
    print("✓ Conectividad verificada")
    return True

def main():
    """Función principal"""
    print("\n" + "="*70)
    print("INICIALIZADOR DEL SISTEMA DE TRADING XRP/USDT")
    print("="*70 + "\n")
    
    pasos = [
        ("Ambiente", verificar_ambiente),
        ("Dependencias", verificar_dependencias),
        ("Configuración", verificar_configuracion),
        ("Conectividad", verificar_conectividad),
    ]
    
    for nombre, funcion in pasos:
        print(f"\n[{nombre}]")
        if not funcion():
            print(f"\n❌ Inicialización fallida en: {nombre}\n")
            return 1
    
    print("\n" + "="*70)
    print("✓ SISTEMA INICIALIZADO CORRECTAMENTE")
    print("="*70)
    print("\nEjecuta: python main.py\n")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
