"""
Conectador a API de Binance
Gestión de conexiones y obtención de datos en tiempo real
"""

import requests
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
from config.settings import Settings
from config.constants import ENDPOINTS_BINANCE
from config.logger_config import logger
from datetime import datetime, timedelta
import pandas as pd
from typing import Dict, List, Optional
import time

class BinanceConnector:
    """Conector a Binance API"""
    
    def __init__(self):
        """Inicializa el conector"""
        self.settings = Settings()
        self.client = None
        self.conectado = False
        self._inicializar()
    
    def _inicializar(self):
        """Inicializa la conexión con Binance"""
        try:
            if not self.settings.BINANCE_API_KEY or not self.settings.BINANCE_API_SECRET:
                logger.error("❌ API Key o Secret de Binance no configuradas")
                return False
            
            self.client = Client(
                api_key=self.settings.BINANCE_API_KEY,
                api_secret=self.settings.BINANCE_API_SECRET,
                testnet=self.settings.USE_TESTNET
            )
            
            # Verificar conexión
            if self.verificar_conexion():
                self.conectado = True
                logger.info("✓ Conectado a Binance API")
                return True
            else:
                logger.error("❌ No se pudo verificar conexión con Binance")
                return False
                
        except Exception as e:
            logger.error(f"❌ Error al inicializar Binance: {str(e)}")
            return False
    
    def verificar_conexion(self) -> bool:
        """Verifica que la conexión esté activa"""
        try:
            self.client.get_account()
            logger.debug("✓ Conexión con Binance verificada")
            return True
        except BinanceAPIException as e:
            logger.error(f"❌ Error API Binance: {e.message}")
            return False
        except Exception as e:
            logger.error(f"❌ Error al verificar conexión: {str(e)}")
            return False
    
    def obtener_velas(self, simbolo: str, intervalo: str, limite: int = 100) -> pd.DataFrame:
        """
        Obtiene velas OHLCV de Binance
        
        Args:
            simbolo: Par de trading (ej: XRPUSDT)
            intervalo: Intervalo de vela (1m, 5m, 1h, etc)
            limite: Número de velas a obtener
            
        Returns:
            DataFrame con datos OHLCV
        """
        try:
            if not self.conectado:
                logger.error("❌ No conectado a Binance")
                return None
            
            logger.debug(f"📊 Obteniendo velas {simbolo} intervalo {intervalo}...")
            
            velas = self.client.get_klines(
                symbol=simbolo,
                interval=intervalo,
                limit=limite
            )
            
            # Procesar datos
            df = pd.DataFrame(velas, columns=[
                'open_time', 'open', 'high', 'low', 'close', 'volume',
                'close_time', 'quote_asset_volume', 'number_of_trades',
                'taker_buy_base', 'taker_buy_quote', 'ignore'
            ])
            
            # Convertir a tipos numéricos
            for col in ['open', 'high', 'low', 'close', 'volume']:
                df[col] = pd.to_numeric(df[col])
            
            df['timestamp'] = pd.to_datetime(df['open_time'], unit='ms')
            df = df[['timestamp', 'open', 'high', 'low', 'close', 'volume']]
            
            logger.debug(f"✓ Obtenidas {len(df)} velas de {simbolo}")
            return df
            
        except BinanceAPIException as e:
            logger.error(f"❌ Error API Binance: {e.message}")
            return None
        except Exception as e:
            logger.error(f"❌ Error al obtener velas: {str(e)}")
            return None
    
    def obtener_precio_actual(self, simbolo: str) -> Optional[float]:
        """
        Obtiene el precio actual de un símbolo
        
        Args:
            simbolo: Par de trading
            
        Returns:
            Precio actual
        """
        try:
            ticker = self.client.get_symbol_ticker(symbol=simbolo)
            precio = float(ticker['price'])
            logger.debug(f"💰 Precio actual {simbolo}: {precio}")
            return precio
        except Exception as e:
            logger.error(f"❌ Error al obtener precio: {str(e)}")
            return None
    
    def obtener_balance(self) -> Dict:
        """
        Obtiene el balance de la cuenta
        
        Returns:
            Dict con balances
        """
        try:
            if not self.conectado:
                logger.error("❌ No conectado a Binance")
                return None
            
            cuenta = self.client.get_account()
            balances = {}
            
            for asset in cuenta['balances']:
                if float(asset['free']) > 0 or float(asset['locked']) > 0:
                    balances[asset['asset']] = {
                        'libre': float(asset['free']),
                        'bloqueado': float(asset['locked']),
                        'total': float(asset['free']) + float(asset['locked'])
                    }
            
            logger.debug(f"✓ Balance obtenido: {len(balances)} activos")
            return balances
            
        except Exception as e:
            logger.error(f"❌ Error al obtener balance: {str(e)}")
            return None
    
    def crear_orden_limit(self, simbolo: str, lado: str, cantidad: float, precio: float) -> Optional[Dict]:
        """
        Crea una orden limitada
        
        Args:
            simbolo: Par de trading
            lado: BUY o SELL
            cantidad: Cantidad a comprar/vender
            precio: Precio límite
            
        Returns:
            Resultado de la orden
        """
        try:
            if not self.conectado:
                logger.error("❌ No conectado a Binance")
                return None
            
            logger.info(f"📝 Creando orden: {lado} {cantidad} {simbolo} @ {precio}")
            
            orden = self.client.order_limit(
                symbol=simbolo,
                side=lado,
                quantity=cantidad,
                price=precio
            )
            
            logger.info(f"✓ Orden creada: ID {orden['orderId']}")
            return orden
            
        except BinanceOrderException as e:
            logger.error(f"❌ Error en orden: {e.message}")
            return None
        except Exception as e:
            logger.error(f"❌ Error al crear orden: {str(e)}")
            return None
    
    def cancelar_orden(self, simbolo: str, orden_id: int) -> Optional[Dict]:
        """
        Cancela una orden existente
        
        Args:
            simbolo: Par de trading
            orden_id: ID de la orden
            
        Returns:
            Resultado de cancelación
        """
        try:
            if not self.conectado:
                logger.error("❌ No conectado a Binance")
                return None
            
            logger.info(f"🗑️  Cancelando orden {orden_id} en {simbolo}")
            
            resultado = self.client.cancel_order(
                symbol=simbolo,
                orderId=orden_id
            )
            
            logger.info(f"✓ Orden cancelada: {orden_id}")
            return resultado
            
        except Exception as e:
            logger.error(f"❌ Error al cancelar orden: {str(e)}")
            return None
    
    def obtener_ordenes_abiertas(self, simbolo: str = None) -> Optional[List[Dict]]:
        """
        Obtiene órdenes abiertas
        
        Args:
            simbolo: Par de trading (opcional)
            
        Returns:
            Lista de órdenes abiertas
        """
        try:
            if not self.conectado:
                logger.error("❌ No conectado a Binance")
                return None
            
            if simbolo:
                ordenes = self.client.get_open_orders(symbol=simbolo)
            else:
                ordenes = self.client.get_open_orders()
            
            logger.debug(f"✓ Obtenidas {len(ordenes)} órdenes abiertas")
            return ordenes
            
        except Exception as e:
            logger.error(f"❌ Error al obtener órdenes: {str(e)}")
            return None
    
    def obtener_historial_trades(self, simbolo: str, limite: int = 100) -> Optional[List[Dict]]:
        """
        Obtiene el historial de trades
        
        Args:
            simbolo: Par de trading
            limite: Número máximo de trades
            
        Returns:
            Lista de trades
        """
        try:
            if not self.conectado:
                logger.error("❌ No conectado a Binance")
                return None
            
            trades = self.client.get_my_trades(symbol=simbolo, limit=limite)
            
            logger.debug(f"✓ Obtenidos {len(trades)} trades de historial")
            return trades
            
        except Exception as e:
            logger.error(f"❌ Error al obtener historial: {str(e)}")
            return None

# Crear instancia global
binance_connector = None

def obtener_connector() -> BinanceConnector:
    """Obtiene la instancia global del conector"""
    global binance_connector
    if binance_connector is None:
        binance_connector = BinanceConnector()
    return binance_connector
