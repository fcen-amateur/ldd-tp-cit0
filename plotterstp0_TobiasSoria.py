import seaborn.objects as so
from gapminder import gapminder
import pandas as pd


def plot():

    datos_2007 = gapminder[gapminder["year"].isin([2007])]

    # Creo la Series donde voy a almacenar los países de interés
    paises = pd.Series()

    for c in ["Americas","Europe"]:
        # Me quedo con los datos del continente
        datos_cont = datos_2007[datos_2007["continent"].isin([c])]
        # Tomo el mayor y menor pbi registrado
        max_gdp = max(datos_cont["gdpPercap"])
        min_gdp = min(datos_cont["gdpPercap"])
        # Me quedo con los datos de los países con mayor y menor pbi
        datos_paises = datos_cont[datos_cont["gdpPercap"].isin([max_gdp, min_gdp])]
        # Los agrego a la Series
        paises = pd.concat([paises, datos_paises["country"]])

    datos_paises_max_min_gdp = gapminder[gapminder["country"].isin(paises)]

    figura = (
        so.Plot(data = datos_paises_max_min_gdp, x = "year", y = "lifeExp")
        .add(so.Line(linewidth=2.2), group = "country", color = "country")
        .facet("continent")
        .label(x = "Año", y = "Expectativa de vida", color = "País")
        .layout(size = (10,6))
    )

    return dict(
        descripcion="El siguiente gráfico muestra la evolución de la expectativa de vida para los países de América y Europa con mayor y menor PBI per cápita registrado en el año 2007.",
        autor="Tobías Soria",
        figura=figura,
    )


plot()

