from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "postgresql://postgres:irene@localhost:5433/ai_finanzas"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def probar_conexion():
    with engine.connect() as conn:
        resultado = conn.execute(text("SELECT version()"))
        print(resultado.fetchone())