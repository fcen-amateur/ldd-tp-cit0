import seaborn.objects as so
from gapminder import gapminder
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def plot():
    datosPoblados = gapminder[gapminder["pop"] > 100000000]
    datosPoblados2007 = datosPoblados[datosPoblados["year"] == 2007]
    datosPoblados2007 = datosPoblados2007.sort_values(by='pop', ascending=False)

    figura = (
        so.Plot(
            datosPoblados2007,
            x="country",
            y="pop",
            color="country",
        )
        .add(so.Bars())
        .label(
            title="Los 10 países con más habitantes en el 2007",
            x="Países",
            y="Población",
            
        )
    )
    return dict(
        descripcion="Gráfico de barras que representa la población de los 10 países con más habitantes del mundo en el año 2007. En esta escala el 1.0 representa mil millones de habitantes.",
        autor="Paula Alvez",
        figura=figura,
    )

