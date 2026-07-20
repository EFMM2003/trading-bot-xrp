"""
Predictor de IA/ML
Modelos de Machine Learning para predicción de precios
"""

import pandas as pd
import numpy as np
from typing import Dict, Tuple
from config.settings import Settings
from config.logger_config import logger
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import warnings
warnings.filterwarnings('ignore')

class PredictorIA:
    """Predictor de precios usando IA/ML"""
    
    def __init__(self):
        """Inicializa el predictor"""
        self.settings = Settings()
        self.scaler = StandardScaler()
        self.modelo = None
        self._entrenar_modelo_inicial()
    
    def _entrenar_modelo_inicial(self):
        """Entrena un modelo inicial"""
        try:
            self.modelo = RandomForestRegressor(
                n_estimators=100,
                max_depth=20,
                random_state=42,
                n_jobs=-1
            )
            logger.info("✓ Modelo RandomForest inicializado")
        except Exception as e:
            logger.error(f"❌ Error inicializando modelo: {str(e)}")
    
    def predecir_precio(self, df: pd.DataFrame, horizonte_horas: int = 4) -> Dict:
        """
        Predice el precio futuro
        
        Args:
            df: DataFrame con datos históricos
            horizonte_horas: Horas a predecir
            
        Returns:
            Dict con predicción
        """
        try:
            if df is None or len(df) < 50:
                logger.warning("⚠️  Datos insuficientes para predicción")
                return None
            
            # Obtener última vela
            ultima_vela = df.iloc[-1]
            precio_actual = float(ultima_vela['close'])
            
            # Calcular cambio promedio
            cambios = df['close'].pct_change().dropna()
            promedio_cambio = cambios.mean()
            volatilidad = cambios.std()
            
            # Predicción simple (puede mejorarse con LSTM/Prophet)
            precio_predicho = precio_actual * (1 + promedio_cambio * horizonte_horas)
            intervalo_confianza = precio_actual * volatilidad * 2
            
            confianza = min(0.95, 0.5 + (len(df) / 500))  # Aumenta con más datos
            
            tendencia = "↑ ALCISTA" if promedio_cambio > 0 else "↓ BAJISTA"
            
            return {
                'precio_predicho': precio_predicho,
                'precio_actual': precio_actual,
                'cambio_esperado': promedio_cambio * 100,
                'intervalo_superior': precio_predicho + intervalo_confianza,
                'intervalo_inferior': precio_predicho - intervalo_confianza,
                'confianza': round(confianza * 100, 2),
                'tendencia': tendencia,
                'horizonte_horas': horizonte_horas
            }
            
        except Exception as e:
            logger.error(f"❌ Error en predicción: {str(e)}")
            return None
    
    def analizar_patron(self, df: pd.DataFrame) -> Dict:
        """
        Analiza patrones en los datos
        
        Args:
            df: DataFrame con datos
            
        Returns:
            Análisis de patrones
        """
        try:
            if df is None or len(df) < 20:
                return None
            
            # Calcular volatilidad
            retornos = df['close'].pct_change()
            volatilidad = retornos.std() * np.sqrt(252) * 100  # Anualizada
            
            # Calcular correlación precio-volumen
            cambios_precio = df['close'].pct_change()
            cambios_volumen = df['volume'].pct_change()
            correlacion = cambios_precio.corr(cambios_volumen)
            
            # Detectar tendencia
            ema_9 = df['ema_9'].iloc[-1] if 'ema_9' in df.columns else None
            ema_50 = df['ema_50'].iloc[-1] if 'ema_50' in df.columns else None
            
            tendencia_direccion = "Alcista" if ema_9 and ema_50 and ema_9 > ema_50 else "Bajista"
            
            return {
                'volatilidad_anualizada': round(volatilidad, 2),
                'correlacion_precio_volumen': round(correlacion, 4),
                'tendencia': tendencia_direccion,
                'riesgo': 'Alto' if volatilidad > 50 else ('Medio' if volatilidad > 20 else 'Bajo')
            }
            
        except Exception as e:
            logger.error(f"❌ Error analizando patrón: {str(e)}")
            return None

class AnalizadorSentimiento:
    """Analiza sentimiento del mercado"""
    
    @staticmethod
    def analizar_volumen(df: pd.DataFrame) -> Dict:
        """
        Analiza el sentimiento basado en volumen
        
        Args:
            df: DataFrame con datos
            
        Returns:
            Análisis de sentimiento
        """
        try:
            if df is None or len(df) < 20:
                return None
            
            ultima_vela = df.iloc[-1]
            vol_promedio = df['volume'].rolling(20).mean().iloc[-1]
            vol_actual = ultima_vela['volume']
            
            ratio_volumen = vol_actual / vol_promedio if vol_promedio > 0 else 1
            
            if ratio_volumen > 1.5:
                sentimiento = "Muy Alcista"
                intensidad = "Muy Alta"
            elif ratio_volumen > 1.2:
                sentimiento = "Alcista"
                intensidad = "Alta"
            elif ratio_volumen < 0.5:
                sentimiento = "Bajista"
                intensidad = "Alta"
            else:
                sentimiento = "Neutral"
                intensidad = "Normal"
            
            return {
                'sentimiento': sentimiento,
                'intensidad': intensidad,
                'ratio_volumen': round(ratio_volumen, 2),
                'confianza': 60 + (min(ratio_volumen - 1, 2) * 20)
            }
            
        except Exception as e:
            logger.error(f"❌ Error analizando sentimiento: {str(e)}")
            return None

# Crear instancia global
predictor_ia = PredictorIA()
analizador_sentimiento = AnalizadorSentimiento()
