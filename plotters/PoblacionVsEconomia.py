import seaborn as sns
import seaborn.objects as so
from gapminder import gapminder
import numpy as np
import pandas as pd


def plot():

    paises_objetivo = []
    paises = gapminder[
        (gapminder.year >= 2004) & ~(gapminder.country.isin(paises_objetivo))
    ]

    figura = (
        (
            so.Plot(
                paises, "pop", y=paises["gdpPercap"] * paises["pop"], color="continent"
            )
            .add(so.Line(), so.PolyFit(1))
            .add(so.Dot())
            .label(title="PBI vs Poblacion", x="Poblacion", y="Producto Bruto Interno")
            .scale(x="log", y="log")
        )
        .share(y=False, x=False)
    )

    return dict(
        descripcion="Gran caso de la paradoja de Simpson. Si miramos la relacion del pbi con la poblacion de los paises en cada continente ,parece habe una correlacion casi directa entre los mismos. Sin embargo, contrario a lo que la intuicion nos diria, no hay una correlacion directa entre la poblacion y el tamaño de una economia a nivel global.Por ejemplo, india y china tienen casi 4 veces la poblacion de Estados Unidos, sin embargo si sumamos sus pbis y los comparamos al pais americano, no llegan a superarlo.",
        autor="Daniel Bustos",
        figura=figura,
    )
