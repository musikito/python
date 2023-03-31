# Importamos las partes de SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Creamos el URL de la base de datos para SQLAlchemy
# Cambia los parametros por los propios
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:admin@localhost:3306/cita"
# Estas dos lineas se usarian si vas a connectar a sqlite o postgresql
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# Creamos la "engine" de SQLAlchemy
# Si usas sqlite deberas agregar un argumento extra:
# SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
engine = create_engine(SQLALCHEMY_DATABASE_URL, )
# Creamos una session local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
