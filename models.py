from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base

class Activo(Base):
    __tablename__ = "activos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    simbolo = Column(String, nullable=False, unique=True)
    tipo = Column(String, nullable=False)
    precio_compra = Column(Float, nullable=False)
    cantidad = Column(Float, nullable=False)
    fecha_creacion = Column(DateTime, default=func.now())