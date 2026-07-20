"""
Cálculo de Indicadores Técnicos
Implementación de RSI, MACD, EMA, Bollinger Bands
"""

import pandas as pd
import numpy as np
from typing import Tuple
from config.constants import INDICADORES
from config.logger_config import logger

class IndicadoresTecnicos:
    """Clase para calcular indicadores técnicos"""
    
    @staticmethod
    def calcular_rsi(precios: pd.Series, periodo: int = 14) -> pd.Series:
        """
        Calcula el RSI (Relative Strength Index)
        
        Args:
            precios: Series de precios
            periodo: Período del RSI (default 14)
            
        Returns:
            Series con valores de RSI
        """
        try:
            delta = precios.diff()
            ganancia = (delta.where(delta > 0, 0)).rolling(window=periodo).mean()
            pérdida = (-delta.where(delta < 0, 0)).rolling(window=periodo).mean()
            rs = ganancia / pérdida
            rsi = 100 - (100 / (1 + rs))
            return rsi
        except Exception as e:
            logger.error(f"❌ Error calculando RSI: {str(e)}")
            return None
    
    @staticmethod
    def calcular_macd(precios: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9) -> Tuple:
        """
        Calcula MACD (Moving Average Convergence Divergence)
        
        Args:
            precios: Series de precios
            fast: Período EMA rápido
            slow: Período EMA lento
            signal: Período de línea signal
            
        Returns:
            Tupla (MACD, Signal, Histogram)
        """
        try:
            ema_fast = precios.ewm(span=fast, adjust=False).mean()
            ema_slow = precios.ewm(span=slow, adjust=False).mean()
            macd = ema_fast - ema_slow
            macd_signal = macd.ewm(span=signal, adjust=False).mean()
            macd_hist = macd - macd_signal
            return macd, macd_signal, macd_hist
        except Exception as e:
            logger.error(f"❌ Error calculando MACD: {str(e)}")
            return None, None, None
    
    @staticmethod
    def calcular_ema(precios: pd.Series, periodo: int) -> pd.Series:
        """
        Calcula EMA (Exponential Moving Average)
        
        Args:
            precios: Series de precios
            periodo: Período de la EMA
            
        Returns:
            Series con valores de EMA
        """
        try:
            return precios.ewm(span=periodo, adjust=False).mean()
        except Exception as e:
            logger.error(f"❌ Error calculando EMA: {str(e)}")
            return None
    
    @staticmethod
    def calcular_bandas_bollinger(precios: pd.Series, periodo: int = 20, desviaciones: float = 2) -> Tuple:
        """
        Calcula Bandas de Bollinger
        
        Args:
            precios: Series de precios
            periodo: Período de la media móvil
            desviaciones: Número de desviaciones estándar
            
        Returns:
            Tupla (Banda Superior, Banda Media, Banda Inferior)
        """
        try:
            sma = precios.rolling(window=periodo).mean()
            std = precios.rolling(window=periodo).std()
            banda_superior = sma + (desviaciones * std)
            banda_inferior = sma - (desviaciones * std)
            return banda_superior, sma, banda_inferior
        except Exception as e:
            logger.error(f"❌ Error calculando Bollinger: {str(e)}")
            return None, None, None
    
    @staticmethod
    def calcular_todos(df: pd.DataFrame) -> pd.DataFrame:
        """
        Calcula todos los indicadores en un DataFrame
        
        Args:
            df: DataFrame con OHLCV
            
        Returns:
            DataFrame con indicadores agregados
        """
        try:
            if df is None or len(df) < 50:
                logger.warning("⚠️  Datos insuficientes para calcular indicadores")
                return None
            
            # RSI
            df['rsi'] = IndicadoresTecnicos.calcular_rsi(df['close'])
            
            # MACD
            df['macd'], df['macd_signal'], df['macd_hist'] = IndicadoresTecnicos.calcular_macd(df['close'])
            
            # EMAs
            df['ema_9'] = IndicadoresTecnicos.calcular_ema(df['close'], 9)
            df['ema_21'] = IndicadoresTecnicos.calcular_ema(df['close'], 21)
            df['ema_50'] = IndicadoresTecnicos.calcular_ema(df['close'], 50)
            
            # Bollinger Bands
            df['bb_upper'], df['bb_middle'], df['bb_lower'] = IndicadoresTecnicos.calcular_bandas_bollinger(df['close'])
            
            # Volumen promedio
            df['vol_ma'] = df['volume'].rolling(window=20).mean()
            
            logger.debug("✓ Indicadores calculados correctamente")
            return df
            
        except Exception as e:
            logger.error(f"❌ Error calculando indicadores: {str(e)}")
            return None
