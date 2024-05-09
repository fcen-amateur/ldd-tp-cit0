import seaborn as sns
import seaborn.objects as so
from gapminder import gapminder
import numpy as np
import pandas as pd


def plot():

    paises_europa_este = [
        "Albania",
        "Belarus",
        "Bosnia and Herzegovina",
        "Bulgaria",
        "Croatia",
        "Czech Republic",
        "Estonia",
        "Hungary",
        "Kosovo",
        "Latvia",
        "Lithuania",
        "Moldova",
        "Montenegro",
        "North Macedonia",
        "Poland",
        "Romania",
        "Russia",
        "Serbia",
        "Slovakia",
        "Slovenia",
        "Ukraine",
    ]
    paises = gapminder[gapminder.continent == "Europe"].copy()
    paises["region"] = np.where(
        paises["country"].isin(paises_europa_este), "Este", "Oeste"
    )

    figura = (
        so.Plot(paises, "year", "lifeExp", color="region")
        .add(so.Line(), so.Agg("mean"))
        .label(
            title="Ex-Paises Sovieticos vs Occidentales",
            x="Año",
            y="Expectativa de vida Promedio",
        )
        .scale(
            color={"Este": "red", "Oeste": "blue"},
        )
    )

    return dict(
        descripcion="Expectativa de vida en Ex-Paises Sovieticos(Rojo) vs Occidentales(azul) en Europa: se observa que a pesar de que la union sovietica colapso hace ya mas de 30 años, las desigualdades regionales en el continente aun persisten",
        autor="Daniel Bustos",
        figura=figura,
    )
