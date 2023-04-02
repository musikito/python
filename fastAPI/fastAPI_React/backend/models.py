from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

# Importamos desde database.py la clase Base
from database import Base


class Autor(Base):
    __tablename__ = "autor_info"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    bio = Column(Text)

    citas = relationship("Citas", back_populates="autor")


class Citas(Base):
    # importamos el nombre de la tabla de la BD
    # El atributo __tablename__ le comunica a SQLAlchemy
    # cuales tablas de la BD vamos a usar para cada modelo
    __tablename__ = "cita_info"
    id = Column(Integer, primary_key=True, index=True)
    # TODO : Añadir columna de categorias desde la tabla categorias
    # category_id = Column(Integer)
    autor_id = Column(Integer, ForeignKey("autor_info.id"))
    mensaje = Column(Text)
    creado_en = Column(DateTime(), default=datetime.now())
    # TODO : añadir columna en la BD
    # is_featured = Column(Boolean)

    autor = relationship("Autor", back_populates="citas")
