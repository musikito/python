from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

# Importamos nuestros paquetes/librerias que hemos creado
import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Buscamos los autores por el nombre, si no existe lo creamos
@app.post("/autores/", response_model=schemas.Autor)
def create_autor(autor: schemas.AutorCreate, db: Session = Depends(get_db)):
    db_autor = crud.get_autor_by_name(db, nombre=autor.name)
    # Si el autor existe, mostramos un mensaje
    if db_autor:
        raise HTTPException(status_code=400, detail="Autor existe")
    return crud.create_autor(db=db, autor=autor)


# Listamos los autores ya creados
@app.get("/autores/", response_model=list[schemas.Autor])
def read_autores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    autores = crud.get_autores(db, skip=skip, limit=limit)
    return autores


# Listamos autores usando el numero de id
@app.get("/autores/{autor_id}", response_model=schemas.Autor)
def read_autor(autor_id: int, db: Session = Depends(get_db)):
    db_autor = crud.get_autor(db, autor_id=autor_id)
    # Si no existes, mostramos mensaje de error
    if db_autor is None:
        raise HTTPException(
            status_code=404, detail="No se encontro este Autor")
    return db_autor


# Creamos la cita y la añadimos al autor
@app.post("/autores/{autor_id}/citas/", response_model=schemas.Cita)
def crea_cita_de_autor(autor_id: int, cita: schemas.CitaCreate, db: Session = Depends(get_db)):
    return crud.create_autor_citas(db=db, cita=cita, autor_id=autor_id)


# listamos las citas
@app.get("/citas/", response_model=list[schemas.Cita])
def read_citas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    citas = crud.get_citas(db, skip=skip, limit=limit)
    return citas


# TODO to be deleted


@app.get("/")
async def root():
    return {"mensaje": "Hola Mundo"}
