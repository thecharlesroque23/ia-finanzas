from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas

router = APIRouter(prefix="/activos", tags=["activos"])

@router.post("/", response_model=schemas.ActivoRespuesta)
def crear_activo(activo: schemas.ActivoCrear, db: Session = Depends(get_db)):
    db_activo = models.Activo(**activo.model_dump())
    db.add(db_activo)
    db.commit()
    db.refresh(db_activo)
    return db_activo

@router.get("/", response_model=list[schemas.ActivoRespuesta])
def listar_activos(db: Session = Depends(get_db)):
    return db.query(models.Activo).all()

@router.get("/{activo_id}", response_model=schemas.ActivoRespuesta)
def obtener_activo(activo_id: int, db: Session = Depends(get_db)):
    activo = db.query(models.Activo).filter(models.Activo.id == activo_id).first()
    if not activo:
        raise HTTPException(status_code=404, detail="Activo no encontrado")
    return activo

@router.delete("/{activo_id}")
def eliminar_activo(activo_id: int, db: Session = Depends(get_db)):
    activo = db.query(models.Activo).filter(models.Activo.id == activo_id).first()
    if not activo:
        raise HTTPException(status_code=404, detail="Activo no encontrado")
    db.delete(activo)
    db.commit()
    return {"mensaje": "Activo eliminado"}