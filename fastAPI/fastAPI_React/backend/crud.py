from sqlalchemy.orm import Session

import models
import schemas


# Buscamos un solo autor
def get_autor(db: Session, autor_id: int):
    return db.query(models.Autor).filter(models.Autor.id == autor_id).first()


# Buscamos autor por nombre
def get_autor_by_name(db: Session, nombre: str):
    return db.query(models.Autor).filter(models.Autor.name == nombre).first()


# Buscamos "varios" autores
def get_autores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Autor).offset(skip).limit(limit).all()


# Creamos autor(es). Esto debe de ser accesible solo a admin(s)
def create_autor(db: Session, autor: schemas.AutorCreate):
    db_autor = models.Autor(name=autor.name, bio=autor.bio)
    db.add(db_autor)
    db.commit()
    db.refresh(db_autor)
    return db_autor


# Buscamos citas
def get_citas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Citas).offset(skip).limit(limit).all()


# Creamos las citas
def create_autor_citas(db: Session, cita: schemas.CitaCreate, autor_id: int):
    db_cita = models.Citas(**cita.dict(), autor_id=autor_id)
    db.add(db_cita)
    db.commit()
    db.refresh(db_cita)
    return db_cita
