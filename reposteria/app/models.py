from flask_appbuilder import Model
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    Numeric
)
from sqlalchemy.orm import relationship


class Categoria(Model):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    descripcion = Column(String(250), nullable=True)
    activo = Column(Boolean, default=True, nullable=False)

    ingredientes = relationship(
        "Ingrediente",
        back_populates="categoria"
    )

    def __repr__(self):
        return self.nombre


class Ingrediente(Model):
    __tablename__ = "ingredientes"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    costo = Column(Numeric(10, 2), default=0)
    activo = Column(Boolean, default=True, nullable=False)

    categoria_id = Column(
        Integer,
        ForeignKey("categorias.id"),
        nullable=False
    )

    categoria = relationship(
        "Categoria",
        back_populates="ingredientes"
    )

    def __repr__(self):
        return self.nombre