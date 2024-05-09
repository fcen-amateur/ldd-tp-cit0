import seaborn.objects as so
from gapminder import gapminder
import numpy as np

def proporcion(arr):
    return arr / sum(arr)

def plot():
    gapminder["total_gdp_M"] = gapminder["gdpPercap"] * gapminder["pop"] / 1000000
    gapminder["proporcion_de_gdp_mundial"] = np.zeros(gapminder["total_gdp_M"].shape)
    for year in gapminder["year"].unique():
        gapminder.loc[gapminder["year"] == year, "proporcion_de_gdp_mundial"] = proporcion(gapminder[gapminder["year"] == year]["total_gdp_M"])

    figura = (
        so.Plot(
            gapminder,
            x="year",
            y= gapminder["proporcion_de_gdp_mundial"], #gdp total por pais en todos los años
            color="continent",
        )
        .add(so.Line(), so.Agg(sum)) #sumo proporciones por continente
        .add(so.Dot(), so.Agg(sum))        
        .label(
            title="Proporción del PBI mundial por continente",
            x="Año",
            y="Proporción",
            color="País",
        )
    )
    return dict(
        descripcion="Proporción del PBI mundial por continente, a lo largo del tiempo",
        autor="Teo Nabot",
        figura=figura,
    )
