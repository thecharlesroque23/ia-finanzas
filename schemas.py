from pydantic import BaseModel
from datetime import datetime

class ActivoCrear(BaseModel):
    nombre: str
    simbolo: str
    tipo: str
    precio_compra: float
    cantidad: float

class ActivoRespuesta(BaseModel):
    id: int
    nombre: str
    simbolo: str
    tipo: str
    precio_compra: float
    cantidad: float
    fecha_creacion: datetime

    class Config:
        from_attributes = True