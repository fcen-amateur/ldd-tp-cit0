import seaborn.objects as so
import seaborn as sns
import numpy as np
from gapminder import gapminder

def plot():
    figura = (
        so.Plot(
            data = gapminder.groupby(['year', 'continent'])['gdpPercap'].median().reset_index(),
            x="year",
            y="gdpPercap",
        )
        .add(so.Line(), color = "continent")
        .add(so.Line(color = "black", linewidth = 3),
             so.PolyFit(1),
             label = "Ajuste lineal del mediano mundial"
        )
        .label(
            title="Mediano del GDP perCapita por continente",
            x="Año",
            y="GDP per Capita",
            color="Continente",
        )
    )
    return dict(
        descripcion="Mediano del GDP per capita por continente a lo largo del tiempo",
        autor="Santiago Chen",
        figura=figura,
    )