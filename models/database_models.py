"""
Modelos de Base de Datos SQLAlchemy
Definición de tablas y relaciones
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, JSON, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()

class Trade(Base):
    """Modelo de tabla trades"""
    __tablename__ = "trades"
    
    id = Column(Integer, primary_key=True, index=True)
    trade_id = Column(String(36), default=lambda: str(uuid.uuid4()), unique=True)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    
    # Parémetros del trade
    simbolo = Column(String(20), index=True)
    tipo = Column(String(10))  # BUY/SELL
    cantidad = Column(DECIMAL(20, 8))
    precio = Column(DECIMAL(20, 8))
    total = Column(DECIMAL(20, 8))
    
    # Estado
    estado = Column(String(20), default="PENDING")
    comision = Column(DECIMAL(20, 8), default=0)
    ganancia = Column(DECIMAL(20, 8), nullable=True)
    
    # Info adicional
    score = Column(Integer, nullable=True)
    recomendacion = Column(String(50), nullable=True)

class Signal(Base):
    """Modelo de tabla signals"""
    __tablename__ = "signals"
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    
    # Señal
    simbolo = Column(String(20), index=True)
    score = Column(Integer)
    recomendacion = Column(String(50))
    precio_actual = Column(DECIMAL(20, 8))
    
    # Indicadores
    rsi = Column(Float, nullable=True)
    macd = Column(Float, nullable=True)
    ema_9 = Column(Float, nullable=True)
    ema_21 = Column(Float, nullable=True)
    ema_50 = Column(Float, nullable=True)
    
    # IA
    prediccion_4h = Column(DECIMAL(20, 8), nullable=True)
    prediccion_24h = Column(DECIMAL(20, 8), nullable=True)
    confianza_ia = Column(Float, nullable=True)

class Alert(Base):
    """Modelo de tabla alerts"""
    __tablename__ = "alerts"
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    
    # Tipo de alerta
    tipo = Column(String(50), index=True)  # signal_change, error, etc
    mensaje = Column(String(500))
    
    # Estado
    enviado = Column(Boolean, default=False)
    enviado_email = Column(Boolean, default=False)
    enviado_telegram = Column(Boolean, default=False)
    enviado_webhook = Column(Boolean, default=False)
    
    # Datos adicionales
    datos_json = Column(JSON, nullable=True)

class AuditLog(Base):
    """Modelo de tabla audit_logs"""
    __tablename__ = "audit_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    
    # Acción
    accion = Column(String(100), index=True)
    descripcion = Column(String(500))
    
    # Usuario (para futuro)
    usuario_id = Column(Integer, nullable=True)
    ip_address = Column(String(45), nullable=True)
    
    # Detalles
    detalles_json = Column(JSON, nullable=True)
    
    # Estado
    estado = Column(String(20), default="SUCCESS")

class SystemConfig(Base):
    """Modelo de tabla system_config"""
    __tablename__ = "system_config"
    
    id = Column(Integer, primary_key=True, index=True)
    clave = Column(String(100), unique=True, index=True)
    valor = Column(String(500))
    descripcion = Column(String(200), nullable=True)
    actualizado = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
