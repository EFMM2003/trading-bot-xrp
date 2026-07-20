"""
Generador de Señales de Trading
Lógica para generar señales basada en indicadores técnicos
"""

import pandas as pd
from typing import Dict
from config.constants import RECOMENDACIONES
from config.logger_config import logger, trading_logger
from core.indicators import IndicadoresTecnicos

class GeneradorSeñales:
    """Genera señales de trading basadas en indicadores"""
    
    @staticmethod
    def generar_señal(df: pd.DataFrame) -> Dict:
        """
        Genera una señal de trading completa
        
        Args:
            df: DataFrame con indicadores calculados
            
        Returns:
            Dict con análisis y recomendación
        """
        if df is None or len(df) == 0:
            logger.error("❌ DataFrame vacío para generar señal")
            return None
        
        try:
            ultima_vela = df.iloc[-1]
            
            # Calcular puntuación
            score = GeneradorSeñales._calcular_score(ultima_vela)
            
            # Generar recomendación
            recomendacion = GeneradorSeñales._obtener_recomendacion(score)
            
            # Recopilar señales individuales
            señales = GeneradorSeñales._obtener_señales_detalladas(ultima_vela)
            
            resultado = {
                'timestamp': ultima_vela['timestamp'],
                'precio': float(ultima_vela['close']),
                'score': score,
                'recomendacion': recomendacion['nombre'],
                'emoji': recomendacion['emoji'],
                'descripcion': recomendacion['descripcion'],
                'confianza': f"{score}%",
                'señales': señales,
                'indicadores': {
                    'rsi': float(ultima_vela['rsi']) if pd.notna(ultima_vela['rsi']) else None,
                    'macd': float(ultima_vela['macd']) if pd.notna(ultima_vela['macd']) else None,
                    'ema_9': float(ultima_vela['ema_9']) if pd.notna(ultima_vela['ema_9']) else None,
                    'ema_21': float(ultima_vela['ema_21']) if pd.notna(ultima_vela['ema_21']) else None,
                    'ema_50': float(ultima_vela['ema_50']) if pd.notna(ultima_vela['ema_50']) else None,
                }
            }
            
            trading_logger.info(f"Señal generada: {recomendacion['nombre']} (Score: {score})")
            return resultado
            
        except Exception as e:
            logger.error(f"❌ Error generando señal: {str(e)}")
            return None
    
    @staticmethod
    def _calcular_score(vela: pd.Series) -> int:
        """
        Calcula la puntuación final (0-100)
        
        Args:
            vela: Serie con datos de la última vela
            
        Returns:
            Score de 0 a 100
        """
        score = 50  # Base neutral
        
        # RSI (máximo ±20 puntos)
        if pd.notna(vela['rsi']):
            rsi = vela['rsi']
            if rsi < 30:
                score += 20
            elif rsi < 40:
                score += 10
            elif rsi > 70:
                score -= 20
            elif rsi > 60:
                score -= 10
        
        # MACD (máximo ±15 puntos)
        if pd.notna(vela['macd']) and pd.notna(vela['macd_signal']):
            if vela['macd'] > vela['macd_signal']:
                score += 15
            else:
                score -= 15
        
        # EMA Trend (máximo ±15 puntos)
        if pd.notna(vela['ema_9']) and pd.notna(vela['ema_21']) and pd.notna(vela['ema_50']):
            if vela['ema_9'] > vela['ema_21'] > vela['ema_50']:
                score += 15
            elif vela['ema_9'] < vela['ema_21'] < vela['ema_50']:
                score -= 15
        
        # Bollinger Bands (máximo ±10 puntos)
        if pd.notna(vela['bb_upper']) and pd.notna(vela['bb_lower']) and pd.notna(vela['close']):
            if vela['close'] < vela['bb_lower']:
                score += 10
            elif vela['close'] > vela['bb_upper']:
                score -= 10
        
        # Normalizar score entre 0 y 100
        score = max(0, min(100, score))
        return int(score)
    
    @staticmethod
    def _obtener_recomendacion(score: int) -> Dict:
        """
        Obtiene la recomendación basada en el score
        
        Args:
            score: Score de 0 a 100
            
        Returns:
            Dict con datos de recomendación
        """
        for key, recom in RECOMENDACIONES.items():
            if recom['rango'][0] <= score <= recom['rango'][1]:
                return recom
        
        return RECOMENDACIONES['NEUTRAL']
    
    @staticmethod
    def _obtener_señales_detalladas(vela: pd.Series) -> list:
        """
        Obtiene señales detalladas de cada indicador
        
        Args:
            vela: Serie con datos de la última vela
            
        Returns:
            Lista de señales
        """
        señales = []
        
        # RSI
        if pd.notna(vela['rsi']):
            if vela['rsi'] < 30:
                señales.append("✓ RSI en zona de sobreventa (< 30)")
            elif vela['rsi'] > 70:
                señales.append("✗ RSI en zona de sobrecompra (> 70)")
            else:
                señales.append(f"≈ RSI neutral ({vela['rsi']:.1f})")
        
        # MACD
        if pd.notna(vela['macd']) and pd.notna(vela['macd_signal']):
            if vela['macd'] > vela['macd_signal']:
                señales.append("✓ MACD arriba de línea signal (Compra)")
            else:
                señales.append("✗ MACD abajo de línea signal (Venta)")
        
        # EMA Trend
        if pd.notna(vela['ema_9']) and pd.notna(vela['ema_21']) and pd.notna(vela['ema_50']):
            if vela['ema_9'] > vela['ema_21'] > vela['ema_50']:
                señales.append("✓ Tendencia alcista confirmada")
            elif vela['ema_9'] < vela['ema_21'] < vela['ema_50']:
                señales.append("✗ Tendencia bajista confirmada")
            else:
                señales.append("≈ Tendencia mixta")
        
        return señales
