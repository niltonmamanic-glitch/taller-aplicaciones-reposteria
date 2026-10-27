from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface

from .models import Categoria, Ingrediente
from .extensions import appbuilder


class CategoriaView(ModelView):
    datamodel = SQLAInterface(Categoria)

    list_columns = [
        "id", "nombre", "descripcion", "activo"
    ]

    add_columns = [
        "nombre", "descripcion", "activo"
    ]

    edit_columns = add_columns
    show_columns = list_columns


class IngredienteView(ModelView):
    datamodel = SQLAInterface(Ingrediente)

    list_columns = [
        "id", "nombre", "costo",
        "categoria", "activo"
    ]

    add_columns = [
        "nombre", "costo", "categoria", "activo"
    ]

    edit_columns = add_columns
    show_columns = list_columns


appbuilder.add_view(
    CategoriaView,
    "Categorías",
    icon="fa-folder",
    category="Repostería"
)

appbuilder.add_view(
    IngredienteView,
    "Ingredientes",
    icon="fa-list",
    category="Repostería"
)