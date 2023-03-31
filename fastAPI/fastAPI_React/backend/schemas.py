from pydantic import BaseModel


class CitaBase(BaseModel):
    mensaje: str


class CitaCreate(CitaBase):
    pass


class Cita(CitaBase):
    id: int
    autor_id: int

    class Config:
        orm_mode = True


class AutorBase(BaseModel):
    name: str


class AutorCreate(AutorBase):
    bio: str


class Autor(AutorBase):
    id: int
    citas: list[Cita] = []

    class Config:
        orm_mode = True
